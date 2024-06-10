import streamlit as st

st.set_page_config(page_title="Simple Calculator")

st.header("Simple Calculator")

x1 = st.number_input("Enter value:")

x2 = st.number_input("Enter another value:")

operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division"))

def evaluate():
  if operation == "Addition":
    return x1 + x2
  if operation == "Subtraction":
    return x1-x2
  if operation == "Multiplication":
    return x1*x2
  if operation == "Division":
   try:
      return x1/x2
   except ZeroDivisionError:
     return "Error: Division by Zero"

val = evaluate()
  
#if st.button("Evaluate"):
st.write("The output is:", round(val,2))
  
