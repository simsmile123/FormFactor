import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

# Set page configuration to wide layout
st.set_page_config(layout='wide')

# Set page title
st.title('Sweep AI')
st.subheader('Upload a CSV file and display its contents')

# File upload widget
file = st.file_uploader('Upload CSV', type=['csv'])

if file is not None:
    # Read the CSV file
    df = pd.read_csv(file)

    # Display the contents of the CSV file
    st.write('**CSV file contents:**')
    st.write(df)

    st.subheader('Analytics')

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

    # Update layout for better visual appearance
    fig.update_layout(
        title='Interactive Line Plot',
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        template='plotly_white',  # Set the plot background to white for a visually pleasing appearance
        hovermode='x',  # Display hover information along the x-axis
        margin=dict(l=40, r=40, t=40, b=40),  # Add margin for better visibility
        width=800,  # Set the plot width
        height=500,  # Set the plot height
    )

    # Display the plot using st.plotly_chart() for interactivity
    st.plotly_chart(fig, use_container_width=True)

    categories = ['A', 'B', 'C', 'D']
    values = [20, 30, 15, 35]
    scatter_x = np.random.rand(50)
    scatter_y = np.random.rand(50)

    # Create a Plotly bar graph
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=categories, y=values))
    fig_bar.update_layout(
        title='Bar Graph',
        xaxis_title='Categories',
        yaxis_title='Values',
        template='plotly_white',
        hovermode='x',
        margin=dict(l=40, r=40, t=40, b=40),
        width=800,
        height=400,
    )

    # Create a Plotly pie chart
    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(labels=categories, values=values))
    fig_pie.update_layout(
        title='Pie Chart',
        template='plotly_white',
        margin=dict(l=40, r=40, t=40, b=40),
        width=800,
        height=400,
    )

    # Create a Plotly scatter plot
    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(x=scatter_x, y=scatter_y, mode='markers'))
    fig_scatter.update_layout(
        title='Scatter Plot',
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        template='plotly_white',
        hovermode='closest',
        margin=dict(l=40, r=40, t=40, b=40),
        width=800,
        height=400,
    )

    # Display the plots using st.plotly_chart() for interactivity
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.plotly_chart(fig_scatter, use_container_width=True)


