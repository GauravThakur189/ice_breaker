from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from third_parties.linkedin import scrap_linkedin_profile


# if __name__ == "__main__":
#    print("Hello, Ice Breaker!")
load_dotenv()

 
summary_template = """
     given the linkdin information {information} about the person from I want to create.
     1. a short summary of the person.
     2. two interesting facts about the person.
"""   
information = """
   
"""
summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template,
)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  

model  = summary_prompt_template | llm

linkdin_data = scrap_linkedin_profile(linkedin_profile_URL="https://www.linkedin.com/in/gaurav-singh189/", mock= True)
result = model.invoke(
   
    input={"information": linkdin_data},
)

print(result.content)