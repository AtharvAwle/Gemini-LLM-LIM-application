from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLR_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")  #use gemini-pro-vision for images
def getGemini_response(input,image):
    if input != "":  #if we give some input it will generate the content for text and img
      response = model.generate_content([input,image])  #generate_content is function which gives us the response.
    else:
        response = model.generate_content(image)  #if we dont give text it will generate it through img
    return response.text


st.set_page_config(page_title="Image + Text",page_icon="📸")
st.title("Generative AI LLM + LIM Project by Atharv Awle")
st.subheader("Text + Images")
st.sidebar.success("Select a page")
# st.header("Gemini Image & Text GPT by ATHARV AWLE")

input = st.text_input("Input prompt: " , key="input")

    
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        

submit = st.button("Tell me about this img")

if submit:
    response = getGemini_response(input,image)
    st.subheader("Response to your prompt....")
    st.write(response)
