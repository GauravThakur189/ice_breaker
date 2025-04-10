from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from third_parties.linkedin import scrap_linkedin_profile
from agents.linkedin_lookup import lookup as linkedin_lookup
from output_parser import summary_parser, Summary
from typing import Tuple, Dict


def ice_break_with(name:str)->tuple[Summary, str]:
    linkedin_username = linkedin_lookup(name=name)
    linkedin_data = scrap_linkedin_profile(linkedin_profile_URL=linkedin_username)
    summary_template = """
      given the linkdin information {information} about the person from I want to create.
      1. a short summary of the person.
      2. two interesting facts about the person.
      Use the information from likedin profile to create the summary and facts.
      \n {format_instructions}
     """   
    
    summary_prompt_template = PromptTemplate(
      input_variables=["information"],
      template=summary_template,
      partial_variables={
          "format_instructions":summary_parser.get_format_instructions(),
      }
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain  = summary_prompt_template | llm | summary_parser
    linkdin_data = scrap_linkedin_profile(linkedin_profile_URL="https://www.linkedin.com/in/gaurav-singh189/", mock= True)
    res:Summary = chain.invoke(
    input={"information": linkdin_data},
    )
    return res, linkedin_data.get("photoUrl")
    

if __name__ == "__main__":
    print("Hello, Ice Breaker!")
    load_dotenv()
    ice_break_with(name="Gaurav Singh Bundelkhand University fullstack developer LinkedIn profile")
      

    