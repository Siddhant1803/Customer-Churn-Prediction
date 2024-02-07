#!/usr/bin/env python
# coding: utf-8

import PIL
from PIL import Image
import pandas as pd
import numpy as np
import streamlit as st
import lightgbm as ltb
import pickle
from pickle import dump
from pickle import load


 # loading the training model
pickle_in = open('LGBM.pkl','rb')
loaded_model = pickle.load(pickle_in)

def prediction(account_length,voice_plan,intl_plan,intl_calls,intl_charge,day_calls,day_charge,eve_calls,eve_charge,night_calls,night_charge,customer_calls):
    
    #preprocessing user input
    if voice_plan == 'yes':
        voice_plan = 1
    else:
        voice_plan = 0
        
    if intl_plan == 'yes':
        intl_plan = 1
    else:
        intl_plan = 0
        
    #making prediction
    prediction = loaded_model.predict([[account_length,voice_plan,intl_plan,intl_calls,intl_charge,day_calls,day_charge,eve_calls,eve_charge,night_calls,night_charge,customer_calls]])
    
    if prediction == 1:
        pred = st.subheader("Customer Will Churn:worried:")
    else:
        pred = st.subheader("Customer Will Not Churn:grin:")
    return st.markdown(f"**{pred}**")



# this is the main function in which we define our webpage  
def main():
    
    # Set up page.
    
    image_path = r"C:\Users\Siddhant Sonawane\OneDrive\Documents\ExcelR Project\DS Projects\Churn_Prediction Project\OIP.jpg"
    image = Image.open(image_path)
    # Set custom page title and icon
    PAGE_CONFIG = {
         "page_title": "Customer Churn Prediction",
        "page_icon": image,
        "layout": "centered"
        }
    st.set_page_config(**PAGE_CONFIG)
    
    #theme
    primaryColor="D0BDF0"
    backgroundColor="#BFB9FA"
    secondaryBackgroundColor="#D0BDF0"
    textColor="#001747"
    font="sans serif"
    
    #Title 
    st.title("Customer Churn Prediction🔄️")
    
    #following lines create boxes in which user can enter data required to make prediction
    
    # Tooltips also support markdown
    radio_markdown = '''Enter total weeks you have been availing services'''.strip()
    radio_markdown1 = '''Select **1** option according to your plan!'''.strip()
    radio_markdown2 = '''Enter total number of calls you make every month'''.strip()
    radio_markdown3 = '''Enter total charges you pay every month'''.strip()

    col1, col2, col3 = st.columns((1,1,1))
    with col1:
        
        account_length = st.number_input('Insert Account Length',help=radio_markdown)
        voice_plan = st.selectbox('voice_plan',('yes','no'),help=radio_markdown1)
        intl_plan = st.selectbox('intl_plan',('yes','no'),help=radio_markdown1)
    
    with col2:
        intl_calls = st.number_input('Insert International Calls',help=radio_markdown2)
        day_calls = st.number_input('Insert Day Calls',help=radio_markdown2)
        eve_calls = st.number_input('Insert Evening Calls',help=radio_markdown2)
        night_calls = st.number_input('Insert Night Calls',help=radio_markdown2)
        customer_calls = st.number_input('Insert Customer Calls',help=radio_markdown2)
    
    with col3:
        intl_charge = st.number_input('Input International Charge',help=radio_markdown3)
        day_charge = st.number_input('Inser Day Charge',help=radio_markdown3)
        eve_charge = st.number_input('Insert Evening Charge',help=radio_markdown3)
        night_charge = st.number_input('Insert Night Charge',help=radio_markdown3)
    
    result = ""
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(account_length,voice_plan,intl_plan,intl_calls,intl_charge,day_calls,day_charge,eve_calls,eve_charge,night_calls,night_charge,customer_calls) 
        st.success('Your {}'.format(result))
        
        
if __name__=='__main__':
    main()


# In[ ]:




