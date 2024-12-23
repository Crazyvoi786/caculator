import streamlit as st

# Function for calculator operations
def crazy_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Streamlit app layout
st.title("Crazy Calculator")
st.write("Welcome to the Crazy Calculator! Perform basic arithmetic operations easily.")

# Input fields
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)
operation = st.selectbox("Choose an operation:", ["+", "-", "*", "/"])

# Perform calculation on button click
if st.button("Calculate"):
    result = crazy_calculator(num1, num2, operation)
    st.success(f"Result: {result}")
