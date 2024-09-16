import streamlit as st
import pytesseract
from PIL import Image
import pandas as pd
from io import StringIO

# Streamlit app
st.title('Extract and Display Table Data from Image')

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpeg", "jpg"])
if uploaded_file is not None:
    # Open image and perform OCR
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image)

    # Display raw OCR text for debugging
    st.subheader("Raw OCR Output")
    st.text(text)

    # Attempt to convert text to DataFrame
    try:
        # Preprocess text by replacing multiple spaces with a single space
        # This step helps maintain column alignment by treating multiple spaces as a delimiter
        cleaned_text = '\n'.join([' '.join(row.split()) for row in text.splitlines()])

        # Display cleaned text for debugging
        st.subheader("Cleaned OCR Text")
        st.text(cleaned_text)

        # Convert cleaned text to DataFrame
        data = StringIO(cleaned_text)
        df = pd.read_csv(data, delim_whitespace=True, engine='python')

        st.subheader("Extracted Table Data")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error processing text to DataFrame: {e}")
