import streamlit as st
import cv2
import pytesseract

# Function to extract text from an image
def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Streamlit app
def main():
    st.title("Image OCR")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Read image and extract text
        image_path = uploaded_image.name
        with open(image_path, "wb") as f:
            f.write(uploaded_image.read())
        extracted_text = extract_text_from_image(image_path)

        # Display extracted text
        st.text_area("Extracted Text:", extracted_text)

if __name__ == "__main__":
    main()