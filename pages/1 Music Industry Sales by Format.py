import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(layout="wide")

file_path = 'data/music_sales_clean.csv'
music_sales_df = pd.read_csv(file_path)


st.title('Music Industry Trends in Sales by Format and Year (1973 - 2019)')

if st.checkbox('Show raw data'):
    st.write(music_sales_df)



st.caption("""
**Source:** [kaggle](https://www.kaggle.com/datasets/thedevastator/music-sales-by-format-and-year)
  
**Data Curated by:** Charlie Hutcheson

""")





physical_formats = ['LP/EP', 'Cassette', 'CD', 'Vinyl Single']
digital_formats = ['Download Album', 'Download Single', 'Paid Subscription', 'On-Demand Streaming']

# Filter the dataset for physical and digital formats
filtered_df = music_sales_df[(music_sales_df['Format'].isin(physical_formats + digital_formats)) & 
                             (music_sales_df['Metric'].isin(['Units', 'Value']))]

# Reshape the data for easier plotting with Plotly Express
units_df = filtered_df[filtered_df['Metric'] == 'Units']
value_df = filtered_df[filtered_df['Metric'] == 'Value']

# Streamlit app structure

st.subheader("""
In this section we are going to explore trends in the music industry over the last four decades, focusing on the resurgence of vinyl records, the decline of CDs, and the rise of digital formats such as downloads and streaming.
""")

st.markdown("<br><br>", unsafe_allow_html=True)


# Tab layout for switching between Units Sold and Revenue
tab1, tab2 = st.tabs(["Units Sold", "Revenue"])

with tab1:
    st.header('Trend of Music Sales by Format Over Time (Units Sold)')
    st.markdown("""
    This visualization shows the number of units sold over time for different physical and digital formats. You can observe the decline in physical formats like CDs and the corresponding rise in digital formats, particularly streaming.
    """)
    
    fig1 = px.line(units_df, x='Year', y='Value (Actual)', color='Format', 
                   labels={'Value (Actual)': 'Units Sold (Millions)', 'Format': 'Music Format'},
                   #title='Trend of Music Sales by Format Over Time (Units Sold)',
                   line_dash='Format',
                   width=1200, height=600)  # Adjust width and height for full-width display
    fig1.update_layout(xaxis_title='')               
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.header('Trend of Music Sales by Format Over Time (Revenue)')
    st.markdown("""
    This visualization tracks the revenue generated by different formats over time. It highlights the dramatic growth in revenue from streaming services, which has largely replaced the revenue from physical formats like CDs.
    """)
    
    fig2 = px.line(value_df, x='Year', y='Value (Actual)', color='Format', 
                   labels={'Value (Actual)': 'Revenue Generated (Millions USD)', 'Format': 'Music Format'},
                   #title='Trend of Music Sales by Format Over Time (Revenue)',
                   line_dash='Format',
                   width=1200, height=600)  # Adjust width and height for full-width display
    fig2.update_layout(xaxis_title='')
    st.plotly_chart(fig2, use_container_width=True)
st.markdown("""
**Units Sold vs. Revenue**:
- **Units Sold**: This measures the number of physical or digital items sold, such as individual records, CDs, downloads, or subscriptions. It reflects consumer activity in purchasing or subscribing to music services.
- **Revenue**: This reflects the total income generated from sales of these units. It includes the price per unit and other factors like the cost of a streaming subscription, which may not directly correlate to the number of units sold.
""")
st.markdown("<br><br>", unsafe_allow_html=True)

# Visualization 3: The Rise of Digital Formats (Downloads and Streaming)
st.header('The Rise of Digital Formats (Downloads and Streaming)')
st.markdown("""
This visualization focuses on the rise of digital formats, including downloads and streaming, and their relationship with physical formats. As digital formats grew, particularly streaming, there was a significant decline in physical formats, especially CDs.
""")

# Filter the dataset for digital formats specifically
digital_df = filtered_df[filtered_df['Format'].isin(digital_formats)]

fig3 = px.line(digital_df[digital_df['Metric'] == 'Value'], x='Year', y='Value (Actual)', color='Format', 
               labels={'Value (Actual)': 'Revenue Generated (Millions USD)', 'Format': 'Digital Format'},
               title='The Rise of Digital Formats (Revenue)',
               width=1200, height=600)  # Adjust width and height for full-width display
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Key Insights**:
- **Streaming's Dominance**: Streaming has become the dominant revenue stream in the music industry, surpassing all other formats, including physical and digital downloads.
- **Impact on Physical Formats**: The rise of streaming, especially after 2010, coincides with the sharp decline in physical formats, particularly CDs.
- **Transition from Downloads**: Digital downloads, which were popular in the early 2000s, have also seen a decline as streaming services became more prevalent.
""")