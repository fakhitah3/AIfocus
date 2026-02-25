import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# 2. Dummy Data (You can replace this with a CSV later)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Revenue': [4500, 5200, 4800, 6100, 7000],
    'Orders': [45, 52, 44, 60, 72]
}
df = pd.DataFrame(data)

# 3. Dashboard UI
st.title("📊 Business Intelligence Dashboard")
st.markdown("Welcome to your live dashboard hosted on **Render**.")

# 4. Metrics
col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,}")
col2.metric("Total Orders", df['Orders'].sum())

# 5. Charts
fig = px.line(df, x='Month', y='Revenue', title="Revenue Growth", markers=True)
st.plotly_chart(fig, use_container_width=True)
