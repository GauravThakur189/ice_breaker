import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
import sys
sys.path.append("c:/Users/GAURAV/OneDrive/Desktop/ice_breaker")
from tools.tools import get_profile_url_tavily


load_dotenv()
# This function looks up a person's LinkedIn profile URL using their name.
def lookup(name: str) ->str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = "given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. Your answer should be a link to the profile page. Do not add any other information."
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need the person Linkedin Page URL"
        )
    ]
    
    react_promt = hub.pull("hwchase17/react")
    agent  = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_promt,
    )
    agent_executer = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
    )
    result = agent_executer.invoke(
        input={"input":prompt_template.format(name_of_person=name)}
    )
    linkedin_profile_URL = result["output"]
    return linkedin_profile_URL

if __name__ == "__main__":
    # Example usage of the lookup function
    name = "Gaurav Singh Bundelkhand University LinkedIn profile" ,
    linkedin_profile_URL = lookup(name)
    print(linkedin_profile_URL)