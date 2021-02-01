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



#INITIALIZATION OF VARIABLES
# parameter_list=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
# parameter_input_values=[]
# parameter_description=['Number of times pregnant','Plasma glucose concentration over 2 hours in an oral glucose tolerance test','Diastolic blood pressure (mm Hg)','Triceps skin fold thickness (mm)','2-Hour serum insulin (mu U/ml)','Body mass index (weight in kg/(height in m)2)','Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)','Age (years)']
# parameter_default_values=['6','148','72','35','0','33.6','0.627','50','1']

#CREATING INTERFACE & UI INTERACTIONS

st.markdown("<h1 style='text-align: center; color: Black;'>Analyze Your Data \n\n</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Green;'>(By Just Your Excel Importing File) \n\n</h4>", unsafe_allow_html=True)



#filename = st.text_input('Enter a file path:')
#try:
#    with open(filename) as input:
#        st.text(input.read())
#except FileNotFoundError:
#    st.error('File not found.')

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


# def get_table_download_link(html):
    # """Generates a link allowing the data in a given panda dataframe to be downloaded
    # in:  dataframe
    # out: href string
    # """
    # #val = to_html(html)
    # b64 = base64.b64encode(html)  # val looks like b'...'
    # return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.html">Download html file</a>' # decode b'abc' => abc



uploaded_file = st.file_uploader("Choose a Excel File")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  st.markdown("<h4 style='text-align: center; color: Black;'>Display Sample Data \n\n</h4>", unsafe_allow_html=True)

  st.write(df.head())
  #st.write(uploaded_file)
  
  
  #profile.to_file("report.html")
  
  #components.html(profile)
  #HtmlFile = open('report.html', 'r', encoding='utf-8')
  #source_code = HtmlFile.read() 
  #st.write(source_code)
  #components.html(source_code,width=500, height=500)
  #'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'

  
   
    
  #print(profile)
  #components.iframe(components.html(profile))  
  #components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200)

  #st.markdown('<a href="data:file/html;html{profile}", download="myfilename.html">Download html file file</a>', unsafe_allow_html=True)
  #st.markdown(get_binary_file_downloader_html(profile, 'HTML'), unsafe_allow_html=True)


if st.button("Analyze Data"):

	profile = ProfileReport(df, title= "Profiling Report by Virtual Analyst")
	profile.to_file("report.html")
	HtmlFile = open('report.html', 'r', encoding='utf-8')
	source_code = HtmlFile.read() 
	#st.write(source_code)
	components.html(source_code,width=1000, height=1000, scrolling=True)
	st.markdown(get_binary_file_downloader_html('report.html'), unsafe_allow_html=True)
	
		
    #st.write('\n','\n')
    #DISPLAYING MODEL OUTPUT AND PREDICTION PROBABILITY 
    #st.write('Your Diabetes Prediction is:**',prediction,' **with **',prediction_proba,'** confidence')