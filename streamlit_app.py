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

# ---- MOCK DATA TABLE ----
st.subheader("📝 Test Case Table")
data = {
    "Test ID": ["IFS.T.A. 1","IFS.T.A. 2","IFS.T.A. 3"],
    "Description": ["Login test", "Checkout flow", "Search function"],
    "Status": ["✅ Passed", "✅ Passed", "❌ Failed"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ---- Download Test Results ----
st.subheader("📂 Test Case Results")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download as CSV", csv, "results.csv", "text/csv")

# ---- FOOTER ----
st.markdown("---")
st.caption("Streamlit Demo App • Only for KVI Showcase")

