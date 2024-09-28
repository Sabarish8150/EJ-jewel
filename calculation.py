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
        # Access the values by column index
        from_val = row.iloc[4]  # 'From' is in the 4th column
        to_val = row.iloc[5]    # 'To' is in the 5th column

        # Check if 'From' and 'To' are numeric
        if is_numeric(from_val) and is_numeric(to_val):
            from_val = int(from_val)
            to_val = int(to_val)
            grade_range = float(row.iloc[6])  # 'Grade Range' is in the 6th column

            if from_val <= total <= to_val:  # Check if total falls in the range
                total_sum += grade_range  # Add the corresponding grade
                st.write(f"{grade_range} G")
                break  # Exit after first match
        else:
            st.write("Out of range (non-numeric 'From' or 'To')")

    return total_sum

# Function to calculate gold weight
def gold_weight(gold_wt):
    global df
    total_sum = 0
    for idx, row in df.iterrows():
        # Access the values by column index
        gold_weight_from = row.iloc[0]  # 'Gold Weight From' is in the 0th column
        gold_weight_to = row.iloc[1]    # 'Gold Weight To' is in the 1st column

        # Check if 'Gold Weight From' and 'Gold Weight To' are numeric
        if is_numeric(gold_weight_from) and is_numeric(gold_weight_to):
            gold_weight_from = float(gold_weight_from)
            gold_weight_to = float(gold_weight_to)
            grade_range = float(row.iloc[2])  # 'Grade Range' is in the 2nd column

            if gold_weight_from <= gold_wt <= gold_weight_to:  # Check if gold_wt falls in the range
                total_sum += grade_range  # Add the corresponding grade
                st.write(f"{grade_range} G")
                break  # Exit after first match
        else:
            st.write("Out of range (non-numeric gold weight)")

    return total_sum

def Sur(gold_wt):
    global df
    total_sum = 0
    for idx, row in df.iterrows():
        # Access the values by column index
        gold_weight_from = row.iloc[8]  # 'Gold Weight From' is in the 8th column
        gold_weight_to = row.iloc[9]    # 'Gold Weight To' is in the 9th column

        # Check if values are numeric before proceeding
        if not is_numeric(gold_weight_from) or not is_numeric(gold_weight_to):
            st.write("Out of range (gold weight)")
        else:
            gold_weight_from = float(gold_weight_from)
            gold_weight_to = float(gold_weight_to)
            grade_range = float(row.iloc[10])  # 'Grade Range' is in the 10th column
            
            if gold_weight_from <= gold_wt <= gold_weight_to:  # Check if gold_wt falls in the range
                total_sum += grade_range  # Add the corresponding grade
                st.write(f"{grade_range} G")
                break  # Exit after first match

    return total_sum


