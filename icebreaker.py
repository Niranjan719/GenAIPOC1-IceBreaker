import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name:str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """
        given the Linkedin information {information} about a person from, I want you to create:
         1. Brief summary in about 100 Words.
         2. 5 interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

    chain = summary_prompt_template | llm

    res = chain.invoke({'information': linkedin_data})

    print(res.content)

if __name__ == "__main__":
    load_dotenv()
    print("Ice-Breaker")
    ice_break_with(name='https://www.linkedin.com/in/niranjan-sai-koppisetti/')



