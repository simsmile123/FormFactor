import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai.api_key = OPEN_API_KEY

# Function to process the uploaded file and interact with OpenAI's API
def analyze_uploaded_file(text):
    # Assuming the file is a text file. Adjust accordingly for other types.
    try:

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

def csv_to_text(df):
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


# Set page configuration to wide layout
st.set_page_config(layout='wide')

# Set page title
st.title('Sweep AI')
st.subheader('Upload a CSV file to analyze its contents')

# File upload widget
file = st.file_uploader('Upload CSV', type=['csv'])

if file is not None:
    df = pd.read_csv(file)

    parsed_text = csv_to_text(df)
    final_text = analyze_uploaded_file(parsed_text)
    st.write(final_text)

    # Display the contents of the CSV file
    st.write('**CSV file contents:**')
    st.write(df)

    st.markdown('---')  # Add separator

    # Display analytics section
    st.subheader('Analytics')

    # Create columns for plots in a 2x2 grid layout
    col1, col2 = st.columns(2)

    # Line plot
    with col1:
        st.write('**Interactive Line Plot**')
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=x, y=y, mode='lines'))
        fig_line.update_layout(
            xaxis_title='X-axis',
            yaxis_title='Y-axis',
            template='plotly_white',
            hovermode='x',
            margin=dict(l=40, r=40, t=40, b=40),
            width=400,
            height=300,
        )
        st.plotly_chart(fig_line, use_container_width=True, align="center")

    # Bar graph
    with col2:
        st.write('**Bar Graph**')
        categories = ['A', 'B', 'C', 'D']
        values = [20, 30, 15, 35]
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(x=categories, y=values))
        fig_bar.update_layout(
            xaxis_title='Categories',
            yaxis_title='Values',
            template='plotly_white',
            hovermode='x',
            margin=dict(l=40, r=40, t=40, b=40),
            width=400,
            height=300,
        )

        st.plotly_chart(fig_bar, use_container_width=True, align="center")

    # Pie chart
    col3, col4 = st.columns(2)
    with col3:
        st.write('**Pie Chart**')
        fig_pie = go.Figure()
        fig_pie.add_trace(go.Pie(labels=categories, values=values))
        fig_pie.update_layout(
            template='plotly_white',
            margin=dict(l=40, r=40, t=40, b=40),
            width=400,
            height=300,
        )
        st.plotly_chart(fig_pie, use_container_width=True, align="center")

    # Scatter plot
    with col4:
        st.write('**Scatter Plot**')
        scatter_x = np.random.rand(50)
        scatter_y = np.random.rand(50)
        fig_scatter = go.Figure()
        fig_scatter.add_trace(go.Scatter(x=scatter_x, y=scatter_y, mode='markers'))
        fig_scatter.update_layout(
            xaxis_title='X-axis',
            yaxis_title='Y-axis',
            template='plotly_white',
            hovermode='closest',
            margin=dict(l=40, r=40, t=40, b=40),
            width=400,
            height=300,
        )
        st.plotly_chart(fig_scatter, use_container_width=True, align="center")

    st.markdown('---')
    st.subheader('Verdict')
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fermentum massa et sapien vehicula, sed lacinia ligula cursus. Quisque ut risus at est placerat vulputate. Nulla facilisi. Nam fringilla mi ac quam sollicitudin, nec tempor metus bibendum. Maecenas a quam velit. Donec sodales pharetra diam, sit amet malesuada magna.')

    st.markdown('---')

    # Centered text using HTML and CSS
    st.write('<div style="text-align: center;">Thank you for using <span style="font-size: 22px; font-weight: 800;">SweepAI</span>!</div>', unsafe_allow_html=True)
