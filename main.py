
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
from typing import Text
from PIL import Image
from sklearn.linear_model import LinearRegression

model= pickle.load(open(r"C:\Users\91961\surya.sav",'rb'))

img1 = Image.open(r"C:\Users\91961\OneDrive\Pictures\Saved Pictures\ht.jpg")
img1 = img1.resize((156,145))
st.image(img1,use_column_width=False)

# Define the function to make predictions
def predict_price(data):
    prediction = model.predict(data)
    return prediction
    
# Create the Streamlit app
st.title("Price Prediction App")
st.title('Hotel Room Rate Prediction')
st.write('Enter information below to get a predicted room rate.')

# Create a form to input the data
form = st.form(key='my_form')
form = st.form(key='my_text')
form = st.form(key='my_date')
sqft = form.number_input('Enter the square footage of the property')
bedrooms = form.number_input('Enter the number of bedrooms')
review = form.text_input('Enter the review text')
people = form.number_input('Enter the number of people')
review = form.number_input('Enter the review rating')
stay = form.number_input ('Enter the numbber of days')
#my_date = form.date_input('Enter the date for booking')
balcony = form.number_input('Enter the number of balconies')
bathrooms = form.number_input('Enter the number of bathrooms')
submit_button = form.form_submit_button(label='Predict')

# When the submit button is clicked, make a prediction
if submit_button:
    data = [[ bedrooms,review,review,balcony,bathrooms,stay,people]]
    prediction = predict_price(data)
    st.subheader("Estimated Price")
    
#prediction_str = np.array2string(np.array([prediction]), formatter={'float_kind':lambda x: "%.2f" % x})

st.write(f"${prediction:} hour")