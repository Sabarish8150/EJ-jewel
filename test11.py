import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set up tesseract executable location (optional if Tesseract is not in the PATH)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Adjust as per your installation

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply some thresholding to make the table more visible
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_table_data(image):
    # Assuming table is in the bottom-right corner, crop that part
    h, w, _ = image.shape
    cropped_image = image[int(h * 0.75):h, int(w * 0.5):w]

    # Preprocess the image
    preprocessed_image = preprocess_image(cropped_image)

    # Perform OCR
    extracted_text = pytesseract.image_to_string(preprocessed_image)

    # Parse the extracted text to find 'Total' and 'Gold Wt'
    extracted_text = extracted_text.replace("|", " ")
    total, gold_wt = None, None
    lines = extracted_text.split('\n')
    for line in lines:
        if 'Total' in line:
            total = line.split()[-2]
        if 'Gold Wt' in line or 'Gold' in line:
            gold_wt = line.split()[-4]

    return total, gold_wt

def main():
    st.title("Extract Table Data from Image (Jewelry Design)")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Read the image
        image = np.array(Image.open(uploaded_image))

        # Show uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract table data
        total, gold_wt = extract_table_data(image)

        # Display the results
        if total or gold_wt:
            st.write(f"**Total**: {total}")
            st.write(f"**Gold Weight**: {gold_wt}")
        else:
            st.write("Could not find 'Total' or 'Gold Weight' in the image.")

if __name__ == "__main__":
    main()
