# from traceback import StackSummary
# from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import  tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch



OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="c2b494e74a28443eae0871353525e9bc.8m9ifltGKuc_jpR5v0cu5wLT")

llm = ChatOllama(model="gpt-oss:120b-cloud",temperature=0)
tools=[TavilySearch()]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job from linkedin in the field of AI security with details")})
    print(result)



if __name__ == "__main__":
    main()
