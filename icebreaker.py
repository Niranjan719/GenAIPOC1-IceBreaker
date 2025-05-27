
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Tuple
from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name) # URL
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """
        given the Linkedin information {information} about a person from, I want you to create:
         1. Brief summary in about 100 Words. Make it 2 to 3 paragraphs.
         2. 5 interesting facts about them.
         \n {format_instructions}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
                                             partial_variables={
                                                 'format_instructions': summary_parser.get_format_instructions()})

    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke({'information': linkedin_data})

    # print(res)
    # print(res.content)

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()
    print("Ice-Breaker")
    ice_break_with(name='https://www.linkedin.com/in/bastyajayshenoy/')
