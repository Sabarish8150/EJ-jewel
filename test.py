import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
import re

# Set up the path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Function to extract text from an image
def extract_text_from_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB
    
    # Preprocess the image if necessary (optional)
    processed_img = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Extract text using pytesseract
    text = pytesseract.image_to_string(processed_img)
    return text

# Function to extract specific data from the extracted text

def extract_details(text):
    text = text.replace("|", " ")
    # Extract total DIA PCS using regex
    dia_pcs_match = re.search(r'Total\s+(\d+)\s+PCS', text)
    dia_pcs = dia_pcs_match.group(1) if dia_pcs_match else 'Not found'
    
    # Extract total DIA WT using regex
    dia_wt_match = re.search(r'Total\s+\d+\s+PCS\s+(\d+\.\d+)', text)
    dia_wt = dia_wt_match.group(1) if dia_wt_match else 'Not found'
    
    # Extract Gold Weight using regex
    gold_wt_match = re.search(r'Gold Wt\s+(\d+\.\d+)\s+GM', text)
    gold_wt = gold_wt_match.group(1) if gold_wt_match else 'Not found'
    
    return dia_pcs, dia_wt, gold_wt


# Streamlit code for file upload and display
st.title("Jewelry Data Extraction")

# Upload an image file
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Convert the uploaded image to an OpenCV format
    image = Image.open(uploaded_image)
    img_array = np.array(image)
    
    # Display the uploaded image
    st.image(img_array, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded image temporarily
    image_path = 'uploaded_image.jpg'
    image.save(image_path)

    # Extract text from the uploaded image
    text = extract_text_from_image(image_path)

    # Extract specific details from the text
    dia_pcs, dia_wt, gold_wt = extract_details(text)

    # Display the extracted details in Streamlit
    st.subheader("Extracted Details")

    tex = text.split(" ")
    pcs = tex[-8]
    wt = tex[-4]
    text = text.replace("|", " ")

    st.text(text)
    st.text(f"Total PCS: {dia_pcs} PCS")
    # st.text(f"Total DIAWT: {dia_wt} GM")
    st.text(f"Gold Weight: {gold_wt} GM")
