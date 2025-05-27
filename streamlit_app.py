import streamlit as st
import pandas as pd
from PIL import Image
import io

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Selenium Dashboard", layout="centered")

# ---- TITLE ----
st.title("📊 Selenium Dashboard")
st.write("This dashboard lets you trigger Test Runs, show results of the Test Runs and download their results")

# ---- ACTION BUTTON ----
st.subheader("🛠 Run an automated Test")
if st.button("Run Test: IFS.T.A. 1"):
    # Simulate logic or processing
    st.info("Processing...")
    # Fake result
    st.success("✅ Test completed successfully!")
if st.button("Run Test: IFS.T.A. 2"):
    # Simulate logic or processing
    st.info("Processing...")
    # Fake result
    st.success("✅ Test completed successfully!")
if st.button("Run Test: IFS.T.A. 3"):
    # Simulate logic or processing
    st.info("Processing...")
    # Fake result
    st.error("❌ Test Failed")
if st.button("Run Test: IFS.T.A. 4"):
    # Simulate logic or processing
    st.info("Processing...")
    # Fake result
    st.warning("⚠️ Pass with Condition")
    st.warning("Test Completed, but Data Quality issue")

# ---- MOCK DATA TABLE ----
st.subheader("📝 Test Case Table")
data = {
    "Test ID": ["IFS.T.A. 1","IFS.T.A. 2","IFS.T.A. 3","IFS.T.A. 4"],
    "Description": ["Login test", "Checkout flow", "Checkout flow 2","Search function"],
    "Status": ["✅ Passed", "✅ Passed", "❌ Failed","⚠️ Passed with Condition"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.subheader("📊 Test Results Overview")

# Example data: test outcomes
data = pd.DataFrame({
    "Results": [1, 1, 2]  
}, index=["2.Fail❌", "3.Conditional ⚠️", "1.Pass✅"])
# index=["✅ 1.Passed", "❌ 2.Failed", "⚠️ 3.Conditional Pass"])

# Show small bar chart
st.bar_chart(data)

# ---- Download Test Results ----
st.subheader("📂 Test Case Results")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download as CSV", csv, "results.csv", "text/csv")

# ---- FOOTER ----
st.markdown("---")
st.caption("Streamlit Demo App • Only for KVI Showcase")

