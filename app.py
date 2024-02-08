from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# fun to get the response from apne gemini pro ka api
model = genai.GenerativeModel("gemini-pro")  #use gemini-pro-vision for images
def getGemini_response(question):
    response = model.generate_content(question)  #generate_content is function which gives us the response.
    return response.text



# STREAMLIT APPLICATION

st.set_page_config(page_title="Atharv's LLM application")
st.header("Atharv Gemini LLM app")

input=st.text_input("Input: " , key="input")
submit = st.button("Get Response")

# jab submit button ko click kare tab....
if submit:
    response = getGemini_response(input)
    st.subheader("Response to your question is ")
    st.write(response)