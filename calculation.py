import streamlit as st
import requests
import csv
import pandas as pd

# Load Google Sheet as CSV
sheet_url = "https://docs.google.com/spreadsheets/d/1OMN8Fdby7qCugZeNg1Ix6IL6_abSuIuszGvi7Qrj2w8/pub?gid=0&single=true&output=csv"
response = requests.get(sheet_url)
data = response.content.decode('utf-8')

# Parse CSV data
csv_data = list(csv.reader(data.splitlines()))
df = pd.DataFrame(csv_data)
df=df.drop(index=1)
df = df.drop(index=0)
# Extract non-null product names from column 13 (12th index)
products = df.iloc[:, 12].dropna().tolist()

# Optionally, if the column may contain empty strings that need to be excluded:
products = [x for x in products if x.strip() != '']


def is_numeric(value):
    """Utility function to check if a value can be converted to a float or int."""
    try:
        float(value)  # Try converting to a float
        return True
    except ValueError:
        return False

def total_pieces(total):
    global df
    total_sum = 0
    for idx, row in df.iterrows():

        from_val = row.iloc[4]  
        to_val = row.iloc[5]  

        if is_numeric(from_val) and is_numeric(to_val):
            from_val = int(from_val)
            to_val = int(to_val)
            grade_range = float(row.iloc[6])  

            if from_val <= total <= to_val: 
                total_sum += grade_range  
                # st.write(f"{grade_range} G")
                break 
        else:
            st.write("Out of range (non-numeric 'From' or 'To')")

    return total_sum


def gold_weight(gold_wt):
    global df
    total_sum = 0
    for idx, row in df.iterrows():

        gold_weight_from = row.iloc[0]  
        gold_weight_to = row.iloc[1]   

    
        if is_numeric(gold_weight_from) and is_numeric(gold_weight_to):
            gold_weight_from = float(gold_weight_from)
            gold_weight_to = float(gold_weight_to)
            grade_range = float(row.iloc[2])  
            if gold_weight_from <= gold_wt <= gold_weight_to: 
                total_sum += grade_range  
             
                break  
        else:
            st.write("Out of range (non-numeric gold weight)")

    return total_sum

def Sur(S_area):
    global df
    total_sum = 0
    for idx, row in df.iterrows():

        gold_weight_from = row.iloc[8] 
        gold_weight_to = row.iloc[9]   

    
        if not is_numeric(gold_weight_from) or not is_numeric(gold_weight_to):
            st.write("Out of range (gold weight)")
        else:
            gold_weight_from = float(gold_weight_from)
            gold_weight_to = float(gold_weight_to)
            grade_range = float(row.iloc[10])  
            
            if gold_weight_from <= S_area <= gold_weight_to:  
                total_sum += grade_range  
                # st.write(f"{grade_range} G")
                break 

    return total_sum

def jewel_type(total,gold_wt,j_type,mode):

    for idx, row in df.iterrows():
        # st.write(row.iloc[13:14])
        # Check if the jewelry type matches the current row
        if row.iloc[12] == j_type:  
            if mode == "Array":
                # st.write(total)
                
                return int(total) * int(row.iloc[13])/100 , float(gold_wt)*int(row.iloc[13])/100
            elif mode == "Mirror":
                # Multiply total and gold weight for Mirror mode
                return int(total) * int(row.iloc[14]) /100 , float(gold_wt)*int(row.iloc[14])/100
            else:
                return int(total),float(gold_wt)
    return 0,0


