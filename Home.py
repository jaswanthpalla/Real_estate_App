import streamlit as st

def home_page():
    # Title and subtitle
    st.title("Welcome to the Land Price Prediction App! 🌍🏡")
    st.subheader("Your one-stop solution for land price analysis and recommendations")

    # Introduction
    st.markdown(
        """
        This app is designed to help users predict land prices, analyze market trends, and get personalized recommendations based on their location and preferences. 
        Here's what you can explore:
        """
    )

    # Features Overview
    st.markdown("### 📂 Features Overview")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### 🏠 Home")
    with col2:
        st.markdown(
            "An introduction to the app, guiding you through its purpose and features."
        )

    col3, col4 = st.columns([1, 2])
    with col3:
        st.markdown("#### 🔮 Predictions")
    with col4:
        st.markdown(
            "Predict land prices based on input parameters ."
        )

    col5, col6 = st.columns([1, 2])
    with col5:
        st.markdown("#### 📊 Analysis")
    with col6:
        st.markdown(
            "Dive deep into the market data with insightful charts and metrics."
        )

    col7, col8 = st.columns([1, 2])
    with col7:
        st.markdown("#### 💡 Recommendations")
    with col8:
        st.markdown(
            "Receive personalized recommendations to help you make informed decisions."
        )

    # Call to Action
    st.markdown("### 🚀 Get Started!")
    st.write(
        "Use the sidebar to navigate to different pages and explore the features in detail."
    )

if __name__ == "__main__":
    home_page()
