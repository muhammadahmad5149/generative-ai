from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults
from langchain_core.tools import tool
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

# result= llm.invoke("Give me today temperature about weather")
# print(result)
# @tool
# def multiply(input: str) -> str:
#     """Multiplies two numbers. Input should be in the format 'x,y'"""
#     x_str, y_str = input.split(",")
#     result = int(x_str.strip()) * int(y_str.strip())
#     return str(result)

# search_tool = TavilySearchResults(search_depth="basic", api_key=os.getenv("TAVILY_API_KEY"))
# tools = [search_tool, multiply]


# agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)
# result = agent.invoke("What is 3 multiply by 4?")
# print(result)

##########################################



generation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a twitter techie influencer assistant tasks with writing excellent twitter posts." 
    "Generate the best twitter post possible for the user's request."
    "if the user provides critique, respond with a revised version of your previous attempt."),
    MessagesPlaceholder(variable_name="messages")
])

