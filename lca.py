import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="LCA Europa Dashboard", layout="wide")

# Add title and description
st.title("LCA Europa Dashboard")
st.markdown("This dashboard visualizes Life Cycle Assessment (LCA) data from Europa.")