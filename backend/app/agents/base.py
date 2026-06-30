from abc import ABC
from typing import Type

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from app.core.gemini import llm
from app.core.prompts import load_prompt



class BaseAgent(ABC):

    prompt_file: str
    output_schema: Type[BaseModel]


    def __init__(self):

        prompt = load_prompt(self.prompt_file)

        self.chain = (
            ChatPromptTemplate.from_template(prompt) | llm.with_structured_output(self.output_schema)
        ) 

    def run(self, **kwargs):

        return self.chain.invoke(kwargs)
    
    #No JSON parsing.
    #No manual Pydantic validation.
    #LCEL does everything.