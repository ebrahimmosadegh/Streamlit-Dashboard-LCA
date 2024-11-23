import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="LCA Europe Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Apply custom CSS
# def load_css():
#     with open("static/style.css") as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load_css()

# Sidebar filters
st.sidebar.title("Filters")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(datetime.now() - timedelta(days=30), datetime.now())
)

# Country filter
countries = ["All", "Germany", "France", "Italy", "Spain", "UK"]
selected_country = st.sidebar.selectbox("Select Country", countries)

# Category filter
categories = ["All", "Transportation", "Energy", "Manufacturing", "Agriculture"]
selected_category = st.sidebar.selectbox("Select Category", categories)

# Impact filter
impact_metrics = ["Carbon Footprint", "Water Usage", "Energy Consumption", "Waste Generation"]
selected_metrics = st.sidebar.multiselect("Select Impact Metrics", impact_metrics)

# Main content
st.title("LCA Europe Dashboard")

# Top metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Carbon Footprint", value="2.5M tons", delta="-2%")
with col2:
    st.metric(label="Water Usage", value="1.2B liters", delta="+5%")
with col3:
    st.metric(label="Energy Consumption", value="850M kWh", delta="-1%")
with col4:
    st.metric(label="Waste Generation", value="450K tons", delta="-3%")

# Charts
col1, col2 = st.columns(2)

with col1:
    # Impact by Country
    fig1 = go.Figure(data=[
        go.Bar(name='Carbon Footprint', x=countries[1:], y=[300, 250, 200, 150, 100]),
        go.Bar(name='Water Usage', x=countries[1:], y=[250, 300, 150, 200, 180])
    ])
    fig1.update_layout(title='Environmental Impact by Country',
                      barmode='group',
                      template='plotly_white')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Time Series Chart
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='ME')
    values = [100, 120, 130, 125, 140, 160, 150, 170, 180, 175, 190, 200]
    
    fig2 = px.line(x=dates, y=values,
                   title='Environmental Impact Over Time',
                   labels={'x': 'Date', 'y': 'Impact Score'})
    fig2.update_layout(template='plotly_white')
    st.plotly_chart(fig2, use_container_width=True)

# Detailed Analysis
st.header("Detailed Analysis")

tab1, tab2, tab3 = st.tabs(["Impact Analysis", "Regional Comparison", "Recommendations"])

with tab1:
    st.subheader("Impact Analysis")
    # Add impact analysis content here
    
with tab2:
    st.subheader("Regional Comparison")
    # Add regional comparison content here
    
with tab3:
    st.subheader("Recommendations")
    # Add recommendations content here