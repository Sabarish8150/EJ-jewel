import streamlit as st
import requests
import csv

# Load Google Sheet as CSV
sheet_url = "https://docs.google.com/spreadsheets/d/1OMN8Fdby7qCugZeNg1Ix6IL6_abSuIuszGvi7Qrj2w8/pub?gid=0&single=true&output=csv"
response = requests.get(sheet_url)
data = response.content.decode('utf-8')

# Parse CSV data
csv_data = list(csv.reader(data.splitlines()))
header = [col.strip() for col in csv_data[0]]  # Strip any extra spaces
rows = csv_data[1:]  # The remaining rows will be the data

# st.write(rows)
# Convert CSV data into a list of dictionaries
data_list = [dict(zip(header, row)) for row in rows]
st.write(data_list)
# Define validation logic based on the loaded CSV data
def total_pieces(total, count):
    total_sum = 0
    for row in data_list:
        st.write(row)
        from_val = int(row['From'])
        to_val = int(row['To'])
        grade_range = float(row['Grade Range'])
        
        if from_val <= total <= to_val:  # Check the range
            total_sum += grade_range  # Add the corresponding grade
            count += 1
            st.write(f"{grade_range} G")
            break
    return total_sum, count

def gold_weight(gold_wt, count):
    total_sum = 0
    for row in data_list:
        gold_weight_from = float(row['Gold Weight From'])
        gold_weight_to = float(row['Gold Weight To'])
        grade_range = float(row['Grade Range'])
        
        if gold_weight_from <= gold_wt <= gold_weight_to:
            total_sum += grade_range
            count += 1
            st.write(f"{grade_range} G")
            break
    return total_sum, count

# Streamlit app interface
st.title("Gold Weight and Pieces Validator")

# Inputs for total pieces and gold weight
total = st.number_input("Enter total pieces:", min_value=0)
gold_wt = st.number_input("Enter gold weight (in GRMS):", min_value=0.0)

count = 0
total_pieces(total, count)
gold_weight(gold_wt, count)
