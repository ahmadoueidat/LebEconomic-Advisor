import streamlit as st
from utils import load_data, analyze_question

# Page layout configuration
st.set_page_config(
    page_title="Lebanon Economic Advisor", 
    page_icon="🇱🇧", 
    layout="wide"
)

# Load dataset using utility module
df = load_data("data.json")

st.title("🇱🇧 Lebanon Economic Intelligence Platform")
st.markdown("An analytical framework tracking Lebanon's macroeconomic crisis (2009–2025) through structured dataset querying.")

# Navigation tabs
tab1, tab2 = st.tabs(["📊 Data & Visualizations", "🤖 Rule-Based Analyst Assistant"])

with tab1:
    st.subheader("Historical Economic Dataset")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("Macroeconomic Trends Overview")
    st.line_chart(df.set_index("year")[["inflation_cpi_pct_yoy", "exchange_rate_lbp_per_usd"]])

with tab2:
    st.subheader("Interactive Economic Query Selector")
    st.markdown("Select an analytical inquiry from the expanded list below to evaluate the dataset programmatically.")
    
    # Expanded list of 8 questions
    question_options = [
        "-- Select a question --",
        "What was the inflation percentage peak in Lebanon between 2009 and 2025, and in which year did it occur?",
        "How did the exchange rate (LBP per USD) evolve from 2019 to 2023?",
        "What were the negative inflation years recorded in the dataset?",
        "What is the overall trend summary of the economic crisis?",
        "What was the average inflation rate during the crisis years (2020-2025)?",
        "In which year did the exchange rate first break the 1,507.5 official peg?",
        "Compare inflation in 2009 versus the peak year 2023.",
        "Show me the records for the stable pre-crisis years (2009-2019)."
    ]
    
    selected_question = st.selectbox("Choose a query:", question_options)
    
    if selected_question != "-- Select a question --":
        st.markdown(f"**Selected Query:** {selected_question}")
        st.markdown("### Analysis Result:")
        
        answer, extra_data = analyze_question(df, selected_question)
        st.write(answer)
        
        # Display supplemental data structures contextually if returned
        if "inflation percentage peak" in selected_question and extra_data is not None:
            st.metric(label=f"Peak Year ({int(extra_data['year'])})", value=f"{extra_data['inflation_cpi_pct_yoy']}%")
        elif ("negative inflation years" in selected_question or "stable pre-crisis" in selected_question) and extra_data is not None:
            st.dataframe(extra_data, use_container_width=True)
        elif "exchange rate" in selected_question and "2019 to 2023" in selected_question:
            sub_df = df[(df["year"] >= 2019) & (df["year"] <= 2023)]
            st.dataframe(sub_df[["year", "exchange_rate_lbp_per_usd"]], use_container_width=True)
        elif "average inflation" in selected_question and extra_data is not None:
            st.dataframe(extra_data[["year", "inflation_cpi_pct_yoy"]], use_container_width=True)