from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.document_loaders import TextLoader
# from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from config import settings

# Define a request model
class QuestionRequest(BaseModel):
    question: str

# FastAPI instance
app = FastAPI(title="Accounting Assistant API", version="1.0")

# Custom Prompt Template
custom_prompt = PromptTemplate.from_template("""
You are a precise accounting information assistant for {firm_name}.
Use only the provided financial documentation to answer questions factually.
If information isn't available, respond professionally with:
"I don't have that specific information in our records - please contact our accounting team for assistance."

Answer requirements:
1. Provide only accounting/finance facts from the context
2. Never add conversational fluff or invitations to ask more
3. Quote exact figures/dates when available
4. Reference relevant forms/regulations where applicable
5. Keep answers under 3 sentences unless technical details require more

For unrelated questions:
"That question falls outside our accounting scope - please contact client services."

Context: {context}
Question: {question}
Concise accounting answer:""")

# Initialize Ollama LLM

llm = OllamaLLM(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)
memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=10)

# Load document
try:
    loader = TextLoader(settings.DATA_FILE)
except Exception as e:
    raise RuntimeError(f"Error loading data: {e}")

# Setup embeddings & vectorstore
embeddings = OllamaEmbeddings(model=settings.EMBEDDING_MODEL, base_url=settings.OLLAMA_BASE_URL)

# Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
documents = loader.load()
docs = text_splitter.split_documents(documents)

# Setup Chroma as vectorstore
persist_directory = "chroma_db"  # or any other persistent directory

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=persist_directory,
)

# (Optional) Persist to disk
vectorstore.persist()

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# Build chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": custom_prompt.partial(firm_name="GL")},
    verbose=False
)

# Endpoint to ask question
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        result = qa_chain.invoke({"question": request.question})
        return {"answer": result["answer"]}
    except Exception as e:
        return {"error": str(e)}
