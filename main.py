import streamlit as st

# functions to convert temperature scales
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# page config
st.set_page_config(page_title="Temperature converter",page_icon="🌡️",layout="centered")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("Welcome to the Temperature Converter App!")
st.sidebar.write("Select the temperature unit you have, either Celsius or Fahrenheit.")
st.sidebar.write("Enter the temperature value in the input field.")
st.sidebar.write("The app will then convert the temperature to the other unit.")

# main container
st.markdown("<h2 style='background-color:red;color:white;text-align:center;padding:10px;border-radius:10px;margin-bottom:20px;'>Temperature Converter App</h2>",unsafe_allow_html=True)
unit = st.radio("Select temperature unit:", ("Celsius", "Fahrenheit"))
temperature = st.number_input("Enter temperature:",value=0.0,step=0.1)
if unit == "Celsius":
    converted_temp = celsius_to_fahrenheit(temperature)
    if st.button("Convert now"):
        st.success(f"{temperature:.1f}°C is equal to {converted_temp:.1f}°F")
else:
    converted_temp = fahrenheit_to_celsius(temperature)
    if st.button("Convert now"):
        st.success(f"{temperature:.1f}°F is equal to {converted_temp:.1f}°C")