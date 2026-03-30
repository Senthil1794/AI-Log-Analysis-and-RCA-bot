# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 01:37:12 2026

@author: user
"""

import streamlit as st
from data_process import search
from data_process import process_docs


# Title
st.title("Log Analysis Bot")
placeholder = st.empty()

# Input box
text_input = st.text_area("Enter your queries: ")


if st.button("Process logs"):
    for status in process_docs(): 
        placeholder.text(status)


# Button
if st.button("RCA"):
    output_data = search(text_input)
    st.header("Answer:")
    st.write(output_data)