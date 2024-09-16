import streamlit as st
import cv2
import pytesseract
import pandas as pd
from PIL import Image
import numpy as np

# Set up Tesseract path if necessary
pytesseract.pytesseract.tesseract_cmd = r'/Program Files/Tesseract-OCR/tesseract.exe'

def preprocess_image(image):
    """Preprocess image for better OCR results."""
    img = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_table_data(image):
    """Extract the table data from the processed image."""
    custom_config = r'--oem 3 --psm 6'
    processed_img = preprocess_image(image)
    text = pytesseract.image_to_string(processed_img, config=custom_config)
    
    # You will need to further refine this to extract the necessary data accurately
    lines = text.split("/n")
    
    # Example extraction logic based on common patterns
    sieve_sizes = []
    dia_wt_pc = []
    dia_mm = []
    dia_pcs = []
    dia_wt = []
    
    for line in lines:
        if "-" in line:
            data = line.split()
            if len(data) >= 5:
                sieve_sizes.append(data[0])
                
                dia_wt_pc.append(0)  # or handle it however you see fit, maybe append None or skip

                dia_mm.append(data[2])
                dia_pcs.append(data[3])
                dia_wt.append(data[4])
    
    table_data = {
        "SIEVE SIZE": sieve_sizes,
        "DIA WT/PC": dia_wt_pc,
        "DIA MM": dia_mm,
        "DIA PCS": dia_pcs,
        "DIA WT": dia_wt
    }
    
    return pd.DataFrame(table_data)

def calculate_totals(df):
    """Calculate the total pieces and total weight from the dataframe."""
    total_pieces = df["DIA PCS"].sum()
    total_weight = df["DIA WT"].sum()
    return total_pieces, total_weight

# Streamlit app layout
st.title("Jewelry Design Data Extractor")

st.write("""
Upload jewelry design images with tabular data, and the system will extract the 
total weight and total pieces from the design.
""")

uploaded_images = st.file_uploader("Choose or drag images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_images:
    total_pieces = 0
    total_weight = 0

    for img_file in uploaded_images:
        image = Image.open(img_file)
        st.image(image, caption=f"Uploaded Image: {img_file.name}", use_column_width=True)

        # Extract data
        df = extract_table_data(image)
        st.write("Extracted Table Data:", df)

        # Calculate totals
        pieces, weight = calculate_totals(df)
        total_pieces += int(pieces)
        total_weight += int(weight)

    st.write(f"**Total Pieces:** {total_pieces}")
    st.write(f"**Total Weight:** {total_weight:.4f} gm")
