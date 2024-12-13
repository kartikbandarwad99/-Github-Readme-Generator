from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
Gemini_API_Key = os.getenv('Gemini_API_Key')

class Summarizer:
    DEFAULT_TEMPLATE = """You are an expert Github specialist. The file name and the code is in dictionary format.
        Give a summary of the file based on whats executed in the file. Give the output in the key value format
        where key is the file name and value is the summary.
        GitHub file: {dictionary}
    """

    def __init__(self, template= None, llm= None):
        self.template = template if template is not None else self.DEFAULT_TEMPLATE
        if llm is not None:
            self.llm = llm
        else:                
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro",
                google_api_key=Gemini_API_Key
            )
            
        self.prompt = PromptTemplate(
            input_variables=["dictionary"],
            template=self.template
        )

    def summarize(self, code) -> str:
        chain =  self.prompt | self.llm
        response = chain.invoke({"dictionary": code})
        return response

class ReadmeGenerator(Summarizer):
    DEFAULT_README_TEMPLATE = """You are a specialist at writing github repo readme.
        You are given the key value pair of filename:summary where summary contains 
        the summary of the code executed in the file.
        
        Generate a professional README.md with the following sections:
        - Project Title
        - Description
        - File Structure
        - Installation
        - Usage
        - Contributing
        - License
        
        Use the following file summaries to create comprehensive documentation:
        {summaries}
    """

    def __init__(self, template = None, llm = None):
        super().__init__(llm=llm)
        self.template = template if template is not None else self.DEFAULT_README_TEMPLATE
        self.prompt = PromptTemplate(
            input_variables=["summaries"],
            template=self.template
        )

    def generate_readme(self, summaries) -> str:
        chain =  self.prompt | self.llm
        response = chain.invoke({"summaries": summaries})
        return response