from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLR_API_KEY"))