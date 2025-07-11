

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os
load_dotenv()

generation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a twitter techie influencer assistant tasks with writing excellent twitter posts." 
    "Generate the best twitter post possible for the user's request."
    "if the user provides critique, respond with a revised version of your previous attempt."),
    MessagesPlaceholder(variable_name="messages")
])

reflection_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet." 
    "Always provide detailed recommendations, including requests for length, virality, style etc"),
    MessagesPlaceholder(variable_name="messages")
])
    
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm