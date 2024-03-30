import streamlit as st
from openai import OpenAI
import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai.api_key = OPEN_API_KEY


def analyze_uploaded_file(text):
    system_prompt = "You are a dataset analyzer working to identify relationships in data. Data sets will belong to manufacturing plants and will always provide a column corresponding to scrap. No scrap will be indicated by a value of 0 and scrap will be indicated by a value of 1. You must mainly look for outliers and communicate what variables have a correlation with scrap values. When you provide a response, do not use words that imply tentativeness like would and could, instead use words like will that express certainty."

    # Initialize the conversation with the system prompt
    conversation = [{"role": "system", "content": system_prompt}]

    # Define the questions to be asked in sequence
    questions = [
        "Read the following dataset and ensure that it includes scrap:",
        "Analyze the additional columns for a correlation between whether there is scrap and the additional variable values. Additionally identify whether there is a positive or negative correlation. Save the correlation values and their sign for later use. Print them out.",
        "Now that you've analyzed the columns, use the numbers that we saved to communicate which three columns have the highest correlation coefficient. Do not provide the correlation coefficient, only what the columns are.",
        "Using the 3 columns you identified, look at the data and concretely describe with numbers what column values are most likely to create or avoid scrap. Provide concrete, detailed, and clear actionable steps to minimize overall scrap. Make sure to convey confidence in your message."
    ]

    output_message = ""

    for question in questions:
        # Assume 'text' variable contains dataset info or relevant context
        prompt_text = question + text
        message = {"role": "user", "content": prompt_text}

        conversation.append(message)
        completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=conversation)
        response_message = completion.choices[0].message.content

        #print(f"Assistant: {response_message}")

        # Update the conversation history with the model's response
        #conversation.append({"role": "assistant", "content": response_message})
        output_message += "Previous message: " + response_message

    return output_message

def csv_to_text(file_path):
    # Load the Excel file
    df = pd.read_csv(file_path)

    # Initialize a list to hold the text representation of each column
    text_columns = []

    # Iterate over the DataFrame columns
    for column in df.columns:
        # Convert each column to a string, joining cells with " | " as the delimiter
        column_text = " | ".join(map(str, df[column].values))
        text_columns.append(column + ":\n" + column_text + "\n")

    # Join all column texts into a single text string, using double newlines as separators
    full_text = "\n".join(text_columns)

    return full_text

st.set_page_config(
    page_title="Sweep",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Sweep")
st.write("Optimize manufacturing")
st.divider()
st.write("")
st.subheader("Video Upload 2")


uploaded_file = st.file_uploader("Upload your file", type=["csv"])
if uploaded_file is not None:
    parsed_text = csv_to_text(uploaded_file)
    final_text = analyze_uploaded_file(parsed_text)
    st.write(final_text)
    # Call the function to analyze the file
    #analysis_result = analyze_uploaded_file(uploaded_file)
    #st.text_area("Analysis Result", value=analysis_result, height=300)
