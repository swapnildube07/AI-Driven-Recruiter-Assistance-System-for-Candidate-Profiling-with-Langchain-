from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import RateLimitError
from third_parties.linkdin import scrape_linkdin_profile

from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from typing import Tuple
from output_parser import  summary_parser


def ice_break_with(name:str) -> Tuple:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkdin_profile(linkedin_profile_url=linkedin_username, mock=True)

    summary_template = '''
              give the Linkdin  information {information} about a person I want to Create:
              1.a short Summary
              2.two interesting facts about them
              
         \n{format_instruction}   
      '''
    # Correcting the key name to 'input_variables'
    summary_prompt_template = PromptTemplate(
        input_variables=['information'],  # Corrected key name
        template=summary_template,
        partial_variables = {"format_instruction": summary_parser.get_format_instruction()}
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    from langchain.chains import LLMChain

    #chain = LLMChain(prompt=summary_prompt_template, llm=llm)
    chain = summary_prompt_template | llm | summary_parser
    res:Summary = chain.invoke(input={"information": linkedin_data})
    return  res, linkedin_data.get("profile_pic_url")





if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break_with(name='swapnil dube')

    # linkedin_data =scrape_linkdin_profile(linkedin_profile_url= "https://www.linkedin.com/in/swapnil077/")






    # Adjusting to use the proper chain class

