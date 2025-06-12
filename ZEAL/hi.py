import streamlit as st
from new import get_response

st.title("Chatbot")

# Create a form to take user input
with st.form(key='user_input_form'):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button("Send")

    # Process the input when the form is submitted
    if submit_button:
        if user_input.lower() == "bye":
            st.text_area("Bot:", value="Goodbye! If you have more questions, feel free to ask.", height=100, key="bot_response")
        else:
            bot_response = get_response(user_input)
            st.text_area("Bot:", value=bot_response, height=100, key="bot_response")
