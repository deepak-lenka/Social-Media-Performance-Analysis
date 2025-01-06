import streamlit as st
import pandas as pd
import plotly.express as px
from db_operations import SocialMediaAnalytics
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set page config
st.set_page_config(page_title="Social Media Performance Analysis", layout="wide")

# Title and description
st.title("Social Media Performance Analysis")
st.markdown("""
This dashboard analyzes engagement metrics across different types of social media posts.
Select a post type below to view detailed metrics and AI-generated insights.
""")

# Post type selection
st.subheader("Select Post Type")
post_type = st.selectbox(
    "Choose the type of posts to analyze:",
    ["All Types", "carousel", "reel", "static"]
)

try:
    # Initialize analytics
    analytics = SocialMediaAnalytics()
    metrics = analytics.get_engagement_metrics(post_type)
    
    if metrics:
        # Convert metrics to DataFrame for easier visualization
        df = pd.DataFrame(metrics)
        
        # Display metrics using columns
        st.subheader("Engagement Metrics")
        col1, col2, col3 = st.columns(3)
        
        # Likes chart
        with col1:
            fig_likes = px.bar(df, x='post_type', y='avg_likes', title='Average Likes by Post Type')
            st.plotly_chart(fig_likes, use_container_width=True)
        
        # Shares chart
        with col2:
            fig_shares = px.bar(df, x='post_type', y='avg_shares', title='Average Shares by Post Type')
            st.plotly_chart(fig_shares, use_container_width=True)
        
        # Comments chart
        with col3:
            fig_comments = px.bar(df, x='post_type', y='avg_comments', title='Average Comments by Post Type')
            st.plotly_chart(fig_comments, use_container_width=True)
        
        # Display raw metrics in a table
        st.subheader("Detailed Metrics")
        st.dataframe(df.round(2))
        
        # Generate insights using OpenAI
        st.subheader("AI-Generated Insights")
        with st.spinner("Generating insights..."):
            prompt = f"""Analyze these social media metrics and provide insights:
            {metrics}
            
            Provide:
            1. Engagement comparison between post types (percentage differences)
            2. Which type performs best for each metric
            3. Three specific, actionable recommendations for improving engagement
            
            Format the response with clear sections for insights and recommendations.
            """
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a social media analytics expert. Analyze the metrics and provide actionable insights and recommendations. Focus on practical, data-driven advice that can improve engagement rates."},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                insights = response.choices[0].message['content']
                st.markdown(insights)
            except Exception as e:
                st.warning("Could not generate AI insights. Please check your OpenAI API key.")
                st.error(f"Error: {str(e)}")
    else:
        st.warning("No data available for the selected post type.")

except Exception as e:
    st.error("Failed to connect to the database or retrieve metrics.")
    st.error(f"Error details: {str(e)}")
    st.info("""
    Please ensure:
    1. Your Astra DB connection is properly configured
    2. The environment variables are set correctly
    3. The database and collection exist
    """)

# Add footer with instructions
st.markdown("---")
st.markdown("""
### How to Use This Dashboard
1. Select a post type from the dropdown menu above
2. View the engagement metrics visualizations
3. Check the detailed metrics table
4. Read the AI-generated insights and recommendations

For custom analytics workflows, use the Langflow interface at http://localhost:7860
""") 