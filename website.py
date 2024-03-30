import streamlit as st
from openai import OpenAI
import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai.api_key = OPEN_API_KEY

# Function to process the uploaded file and interact with OpenAI's API
def analyze_uploaded_file(text):
    # Assuming the file is a text file. Adjust accordingly for other types.
    try:

        # Initialize OpenAI API (ensure you've set your API key in your environment)
        openai.api_key = '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';

        # Crafting a prompt for the OpenAI model to analyze the causes of scrap from the content
        prompt_text = f"Read the following dataset and list the 3 most important factors contributing to scrap:" + text

        system_prompt = f"You are a dataset analyzer working to find relationships in data, mainly look for outliers and find what columns in the scrap rows cause it to be 1 "

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)  # For debugging purposes


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