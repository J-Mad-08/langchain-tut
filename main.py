import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
# from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    """Prompt for a search query and print the agent's response."""
    query = input("Enter your search query: ")
    response = agent.invoke({"messages": [HumanMessage(content=query)]})
    print(f"Search result: {response}")


if __name__ == "__main__":
    main()
