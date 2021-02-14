#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
#from sklearn.externals import joblib
import joblib
from pandas_profiling import ProfileReport
import streamlit.components.v1 as components
import base64
import os
import cv2




img= cv2.imread('logo.png',-1)
st.image(img,channels="RGB",width=500)


st.markdown("<h1 style='text-align: center; color: Black;'>Analyze Your Data \n\n</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Green;'>(By Just Your Excel Importing File) \n\n</h4>", unsafe_allow_html=True)

option = st.selectbox('Select File Type:',('CSV', 'EXCEL'))
st.write('You selected:', option)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

uploaded_file = st.file_uploader("Choose a Excel File")
if uploaded_file is not None:
  if option == 'EXCEL':		
   	df = pd.read_excel(uploaded_file)
  elif option == 'CSV':
    df = pd.read_csv(uploaded_file)
  st.markdown("<h4 style='text-align: center; color: Black;'>Display Sample Data \n\n</h4>", unsafe_allow_html=True)

  st.write(df.head())

if st.button("Analyze Data"):

	profile = ProfileReport(df, title= "Profiling Report by Virtual Analyst")
	profile.to_file("report.html")
	HtmlFile = open('report.html', 'r', encoding='utf-8')
	source_code = HtmlFile.read() 
	#st.write(source_code)
	components.html(source_code,width=1000, height=1000, scrolling=True)
	st.markdown(get_binary_file_downloader_html('report.html'), unsafe_allow_html=True)