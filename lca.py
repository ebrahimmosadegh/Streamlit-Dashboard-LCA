import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="LCA Europa Dashboard", layout="wide")

# Add title and description
st.title("LCA Europa Dashboard")
st.markdown("This dashboard visualizes Life Cycle Assessment (LCA) data from Europa.")

# Load and preprocess data
@st.cache_data
def load_data():
    # Replace with actual data loading from LCA Europa
    # This is just an example structure
    df = pd.DataFrame({
        'Product': ['Product A', 'Product B', 'Product C'],
        'Carbon_Footprint': [100, 150, 80],
        'Water_Usage': [500, 300, 400],
        'Energy_Consumption': [1000, 1200, 800]
    })
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_products = st.sidebar.multiselect(
    "Select Products",
    options=df['Product'].unique(),
    default=df['Product'].unique()
)

# Filter dataframe based on selection
filtered_df = df[df['Product'].isin(selected_products)]

# Create layout with columns
col1, col2 = st.columns(2)

with col1:
    # Carbon Footprint Chart
    fig_carbon = px.bar(
        filtered_df,
        x='Product',
        y='Carbon_Footprint',
        title='Carbon Footprint by Product'
    )
    st.plotly_chart(fig_carbon, use_container_width=True)
    
    # Energy Consumption Chart
    fig_energy = px.line(
        filtered_df,
        x='Product',
        y='Energy_Consumption',
        title='Energy Consumption by Product'
    )
    st.plotly_chart(fig_energy, use_container_width=True)