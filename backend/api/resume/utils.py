import os 
import openai
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

openai.api_key  = os.environ['OPENAI_API_KEY']

UPLOADS_DIR = "uploads"
     
def processor(file):
        file_path = os.path.join(UPLOADS_DIR, file.filename)

        with open(file_path, "wb") as pdf_file:
            pdf_file.write(file.file.read())
        if file.content_type == "application/pdf":
         loader = PyPDFLoader(file_path)
        if file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or file.content_type == "application/msword":
         loader = PyPDFLoader(file_path)

        document = loader.load()

        return document
    
def scanner(document):
    system_template = """
    You are a helpful AI bot. Your task is to Completely Scan the Resume of the user and generate the Short Summary of the Resume.
    By Scanning the Resume you need to extract the details containing informations like Phone ,Email, Linkedin URL, Github URL.
    By Scanning the Resume you also need to generate the Interview Question which can be asked on the basis of Resume.
    """
    answer = generator(document, system_template)

    return answer

def checker(document):
    system_template = """
    You are a helpful AI bot. Your task is to Completely Scan the Resume of the user and generate the Short Summary of the Resume.
    By Scanning the Resume you need to extract the details containing informations like Phone ,Email, Linkedin URL, Github URL.
    By Scanning the Resume you also need to generate the Interview Question which can be asked on the basis of Resume.
    """
    answer = generator(document, system_template)

    return answer

def generator(document, system_template):
    template = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", "{document}"),
    ])
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    # chain = load_qa_chain(llm, chain_type="stuff",verbose=True,prompt=template)
    chain = template | llm
    # answer =  chain.run()
    answer = chain.invoke({"document": document})
    return answer    