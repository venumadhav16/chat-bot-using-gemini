from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY "))


model=genai.GenerativeModel("gemini-pro")
def get_genai_response(question):
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="genai chatbot")
st.header("Gemini LLM Applictaion")
input=st.text_input("Input: ",key="input")
submit=st.button("get the response")

if submit:
    response=get_genai_response(input)
    st.subheader("The response is : ")
    st.write(response)
