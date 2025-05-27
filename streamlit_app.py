import streamlit as st
import pandas as pd
from PIL import Image
import io

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Generic Dashboard", layout="centered")

# ---- TITLE ----
st.title("📊 Generic Dashboard")
st.write("This dashboard lets you upload data, view a table, trigger processing, and show results.")

# ---- MOCK DATA TABLE ----
st.subheader("Test Case Table")
data = {
    "Test ID": [1, 2, 3],
    "Description": ["Login test", "Checkout flow", "Search function"],
    "Status": ["Pending", "Pending", "Pending"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ---- FILE UPLOAD ----
st.subheader("📂 Upload a File")
uploaded_file = st.file_uploader("Choose a file (CSV, TXT, PNG...)", type=["csv", "txt", "png", "jpg", "jpeg"])

if uploaded_file:
    file_type = uploaded_file.type
    st.success(f"Uploaded file: `{uploaded_file.name}`")

    if file_type.startswith("image/"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    elif file_type.endswith("csv"):
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded CSV:")
        st.dataframe(df_uploaded)
    elif file_type.endswith("txt"):
        text = uploaded_file.read().decode("utf-8")
        st.text_area("Text Content", value=text, height=200)

# ---- ACTION BUTTON ----
st.subheader("🛠 Run a Process")
if st.button("Click to Process"):
    # Simulate logic or processing
    st.info("Processing...")
    # Fake result
    st.success("✅ Operation completed successfully!")

# ---- FOOTER ----
st.markdown("---")
st.caption("Streamlit Demo App • Customize as needed")

