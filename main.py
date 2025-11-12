from traceback import StackSummary
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama
from openai import OpenAI


load_dotenv()

def main():
    # print("Hello from langchain-course!")
    information = """Elon Reeve Musk[b] (born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2021; as of October 2025, Forbes estimates his net worth to be around $500 billion.

Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; his Canadian citizenship is congenital, his mother having been born there. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.

    """

    stemplate = """ given the information {information}, create the following
    1 - a short summary (not more than 100 words)
    2 - two interesting facts about the person"""

    OLLAMA_BASE_URL = "http://localhost:11434/v1"
    ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="c2b494e74a28443eae0871353525e9bc.8m9ifltGKuc_jpR5v0cu5wLT")

    llm = ChatOllama(
            model="gpt-oss:120b-cloud",
            temperature=0)
    
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=stemplate)

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)

if __name__ == "__main__":
    main()
