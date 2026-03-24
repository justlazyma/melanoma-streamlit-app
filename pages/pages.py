import streamlit as st
from database import fetch_reports

st.title("📊 Reports")

data = fetch_reports()

if data:
    for row in data:
        st.write(f"ID: {row[0]}")
        st.write(f"Image: {row[1]}")
        st.write(f"Result: {row[2]}")
        st.write(f"Confidence: {row[3]*100:.2f}%")
        st.markdown("---")
else:
    st.info("No reports found")