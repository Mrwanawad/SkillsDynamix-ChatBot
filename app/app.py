
import os
import streamlit as st  #streamlit run app/app.py
from utils.system_prompt import SYSTEM_PROMPT
from retriever import get_relevant_chunks
from llm import LLM

llm = LLM(  )

st.set_page_config( 'Skills Dynamix Demo Chatbot', ':bar_chart:' ,  layout='wide')

row_1, row_2 = st.columns( 2 )

row_1.image("app/imgs/skillsdynamix.png", use_container_width=True, width= 'content')

row_2.markdown(  '<h1 style = "font-family:times new roman; font-size:65px;text-align:center;color:#FF5A00" >Skills Dynamix Demo Chatbot</h1>',
                 unsafe_allow_html=True)


user_query = st.text_area( 'Please provide your question here...' )

if st.button( 'Send' ) :
    
    relevant_chunks = get_relevant_chunks( user_query ) if len( user_query ) != 0 else 'Hi'
    SYSTEM_PROMPT = SYSTEM_PROMPT.format( str( relevant_chunks ) )

    model_response = llm.call_llm_and_gen_response( user_query, SYSTEM_PROMPT )
    
    st.markdown( model_response )  


