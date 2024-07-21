import os

from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
   create_react_agent,
   AgentExecutor,
)

from langchain import hub
from tool.tools import get_profile_url_tavily
def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    template = ("give a full name {name_of_person} I want you to get it me a link to their Linkedin profile page"
                "Your answer should be url")

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linedin Profile page",
            func=get_profile_url_tavily ,
            description="useful for when you need get the linkedin Page url",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )


    linked_profile_url = result["output"]
    return linked_profile_url



if __name__ == "__main__":
    linkedin_url = lookup(name="Swapnil Dube")
    print(linkedin_profile_url)
