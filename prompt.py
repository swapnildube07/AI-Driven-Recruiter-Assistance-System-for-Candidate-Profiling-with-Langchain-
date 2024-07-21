from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

class PromptTemplates(StringPromptTemplate):
    '''Schema to represent a prompt for an LLM


       Exmaple:
          .. code-block:: python
          from langchain import PromptTemplate
          prompt = PromptTemplates(input_variables=["Foo"], template="say{foo}
          '''

    input_variables: List[str]
    '''A List of the Names of the Variables the prompt templates expect'''
    template: str
    '''The Prompt Template'''

    template_format: str = "f-string"
    '''The Format of the Script templates . options are the 'f-string','jinja2','''

    validate_template: bool = True
    '''Wheather or not To try Validating the Templates'''



