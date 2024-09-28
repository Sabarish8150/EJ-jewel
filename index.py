import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np
from calculation import *

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_table_data(image,m_on):
    h, w, _ = image.shape
    cropped_image = image[int(h * 0.75):h, int(w * 0.5):w]
    preprocessed_image = preprocess_image(cropped_image)
    extracted_text = pytesseract.image_to_string(preprocessed_image)

    # Clean up the text
    extracted_text = extracted_text.replace("|", " ").strip()
    extracted_text = extracted_text.replace(";", " ").strip()
    
    total, gold_wt = None, None
    lines = extracted_text.split('\n')
    # st.write(lines)
    for line in lines:
        line_split = line.split()
        a=-2
        if 'Total' in line or 'TOTAL' in line:
            total = line.split()[-2] if len(line.split()) > 1 else None
        if 'Gold Wt' in line or 'Gold' in line:
            gold_wt = line.split()[-4] if len(line.split()) > 3 else None
        # if m_on:
        if 'Total' in line or 'TOTAL' in line:
            if len(line_split) >= 4:  # Ensure there are at least 4 elements
                S_area = line_split[-4]
                if not m_on:
                    st.write("**It's a mirror image**")
            else:
                S_area=0
                if m_on:
                    st.write("**It's not a mirror image**")

        

            
                

    # st.write(lines)


    return total, gold_wt, extracted_text, S_area if m_on else None

def main():
    st.title("Jewelry Data Extraction....!!!")

    uploaded_image = st.file_uploader("Upload an image---->>>>", type=["png", "jpg", "jpeg"])

    col1, col2 = st.columns([0.8, 0.2])  # Adjust the ratios for alignment
    
    with col2:
        m_on = st.toggle("Mirror")

    if uploaded_image is not None:
        image = np.array(Image.open(uploaded_image))
        st.image(image, caption="Uploaded Image", use_column_width=True)

        total, gold_wt, extracted_text, S_area = extract_table_data(image,m_on)
        
        # st.write(extracted_text)
        if total and gold_wt:
            total = int(total)
            gold_wt = float(gold_wt)
            if m_on:
                S_area=float(S_area)
            
            total_sum=0

            if m_on:
                total/=2
                gold_wt/=2
            st.write(f"**Total**  :  {int(total)} PCS")
            st.write(f"**Gold Weight**  :  {gold_wt} g")


            if m_on:
                st.write(f"**Surface Area** : {S_area} mm³")
    
            try:
                

                count=2
                total_sum+=total_pieces(total)
                total_sum+=gold_weight(gold_wt)
                if m_on:
                    total_sum+=Sur(S_area)
                    count+=1


                st.write(f"**Grade** : \n\n {round((total_sum/count),2)}")

            except ValueError:
                st.write("Error: Unable to convert 'Total' or 'Gold Weight' to a number.")
        else:
            st.write("Could not find 'Total' or 'Gold Weight' in the image.")


if __name__ == "__main__":
    main()
