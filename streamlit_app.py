import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Page titles for navigation
PAGES = {
    "Home": "streamlit_app.py",
    "Selangor": "pages/Selangor.py",
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Load the selected page
if selection == "Home":
    import page1
elif selection == "Data Analysis":
    import page2
