import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

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
    
    total, gold_wt = None, None
    lines = extracted_text.split('\n')
    for line in lines:
        if 'Total' in line or 'TOTAL' in line:
            total = line.split()[-2] if len(line.split()) > 1 else None
        if 'Gold Wt' in line or 'Gold' in line:
            gold_wt = line.split()[-4] if len(line.split()) > 3 else None
        if m_on:
            if 'Total' in line or 'TOTAL' in line:
                S_area = line.split()[-4] if len(line.split()) > 1 else None

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
                
            #     st.write("**GRADE (pcs)**")

                count=0
                if 1 <= total <= 20:
                    total_sum+=0.2 ##0
                    count+=1
                    # st.write("0.2 G")
                elif 20 < total <= 40:
                    total_sum+=0.35
                    count+=1
            #         st.write("0.35 G")
                elif 40 < total <= 60:
                    total_sum+=0.45
                    count+=1
            #         st.write("0.45 G")
                elif 60 < total <= 150:
                    total_sum+=0.55
                    count+=1
            #         st.write("0.55 G")

            #     st.write("**GRADE (gold weight)**")
                if  gold_wt <= 3.0:
                    total_sum+=0.4
                    count+=1
            #         st.write("0.4 G")
                elif 3.0 < gold_wt <= 5.0:
                    total_sum+=0.5
                    count+=1
            #         st.write("0.5 G")
                elif 5.0 < gold_wt <= 7.0:
                    total_sum+=0.65
                    count+=1
            #         st.write("0.65 G")


            #     st.write("**GRADE (Surface area)**")
                if m_on:
                    if  S_area <= 200:
                        total_sum+=0.25
                        count+=1
                    #st.write("0.25 G")
                    elif 200 < S_area <= 400:
                        total_sum+=0.35
                        count+=1
                        #st.write("0.35 G")
                    elif 400 < S_area <= 1000:
                        total_sum+=0.45
                        count+=1
                        #         st.write("0.45 G")
                    elif 1000 < S_area <= 2000:
                        total_sum+=0.55
                        count+=1
                        #         st.write("0.55 G")

                st.write(f"**Grade** : \n\n {round((total_sum/count),2)}")

            except ValueError:
                st.write("Error: Unable to convert 'Total' or 'Gold Weight' to a number.")
        else:
            st.write("Could not find 'Total' or 'Gold Weight' in the image.")


if __name__ == "__main__":
    main()
