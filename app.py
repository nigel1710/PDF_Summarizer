import PyPDF2 as pdf
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import Document
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

def get_summarization(pdf_content):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=GOOGLE_API_KEY,temperature=0.5)
    prompt_template = "Write a concise summary of the following context:\\n\\n{context}"  
    prompt = PromptTemplate(  
        input_variables=["context"], template=prompt_template  
    )
    documents = [Document(page_content=pdf_content)]
    chain=create_stuff_documents_chain(llm, prompt)
    result = chain.invoke({"context": documents})
    return result

### Streamlit App

st.set_page_config(page_title="SummarizeIt")
st.header("SummarizeIt: Quick, Clear, Concise PDF Summaries in Seconds")
uploaded_file=st.file_uploader("Upload PDF to Summarize",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit = st.button("Summarize")

if submit:
    if uploaded_file is not None:
        pdf_content=input_pdf_text(uploaded_file)
        response=get_summarization(pdf_content)
        st.subheader("The summary of the uploaded file is:")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
