import os
import numpy as np
import chromadb
from typing import List, Tuple
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv;     load_dotenv()
import streamlit as st

st.secrets

class LLM :
    
    def __init__(self):     # Initialize the Large Language Model
        self.llm = genai.Client( api_key= st.secrets["GOOGLE_GEMINI_API_KEY"] )
        print( 'API KEY Found Successfully !' )
        print( 'Initialized LLM Successfully !' )

    def call_llm_and_gen_response( self, user_query: str, SYSTEM_PROMPT: str ) -> str :

        
        response = self.llm.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_query,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
        )
        return response.text


if __name__ == '__main__' :
    
    llm = LLM()
    print( f'API KEY Located ? : { load_dotenv() }' )

