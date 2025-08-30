from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

promt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question:{question}")
    ]
)


## Streamlit

st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter your question:")

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
output_parser = StrOutputParser()
chain = promt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
