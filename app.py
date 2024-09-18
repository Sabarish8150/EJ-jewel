import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def preprocess_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_table_data(image):
    h, w, _ = image.shape
    cropped_image = image[int(h * 0.75):h, int(w * 0.5):w]

    preprocessed_image = preprocess_image(cropped_image)

    extracted_text = pytesseract.image_to_string(preprocessed_image)

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
    st.title("Jewelry Data Extraction....!!!")

    uploaded_image = st.file_uploader("Upload an image---->>>>", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:  
        image = np.array(Image.open(uploaded_image))

        st.image(image, caption="Uploaded Image", use_column_width=True)

        total, gold_wt = extract_table_data(image)

        if total or gold_wt:
            st.write(f"**Total**     :   {total} PCS")
            st.write(f"**Gold Weight**   :   {gold_wt} g")
        else:
            st.write("Could not find 'Total' or 'Gold Weight' in the image.")


        total=float(total)
        gold_wt=float(gold_wt)


        st.write("**GRADE(pcs)**")
        if 1<=total<=20:
            st.write("0.4 G")
        elif 20<total<=40:
            st.write("0.5 G")
        elif 40<total<=100:
            st.write("0.65 G")

        st.write("**GRADE(gold_weight)**")
        if 1.0<=gold_wt<=3.0:
            st.write("0.4 G")
        elif 3.0<gold_wt<=5.0:
            st.write("0.5 G")
        elif 5.0<gold_wt<=7.0:
            st.write("0.65 G")

if __name__ == "__main__":
    main()
