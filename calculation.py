import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np  


def total_peices(total,count):
    total_sum=0
    if 0 <= total <= 10:
        total_sum+= 0.1
    elif 10 < total <= 20:
        total_sum+= 0.25
    elif 20 < total <= 30:
        total_sum+= 0.4
    elif 30 < total <= 40:
        total_sum+= 0.55
    elif 40 < total <= 50:
        total_sum+= 0.55
    elif 50 <= total <= 60:
        total_sum+= 0.7
    elif 60 < total <= 80:
        total_sum+= 0.85
    elif 80 < total <= 100:
        total_sum+= 1
    elif 101 <= total <= 120:
        total_sum+= 1.15
    elif 121 <= total <= 140:
        total_sum+= 1.3
    elif 141 <= total <= 150:
        total_sum+= 1.45
    elif 151 <= total <= 160:
        total_sum+= 1.6
    elif 161 <= total <= 170:
        total_sum+= 1.75
    elif 171 <= total <= 180:
        total_sum+= 1.9
    elif 181 <= total <= 190:
        total_sum+= 2.05
    elif 191 <= total <= 200:
        total_sum+= 2.2
    elif 201 <= total <= 210:
        total_sum+= 2.35
    elif 211 <= total <= 220:
        total_sum+= 2.5
    elif 221 <= total <= 250:
        total_sum+= 2.65
    elif 251 <= total <= 300:
        total_sum+= 2.8
    elif total > 300:
        total_sum+= 2.95
    # else:
    #     total_sum+= "Out of range"
    count+=1
    return total_sum, count


def gold_Weight(gold_wt,count):
    total_sum=0
    if 0 <= gold_wt<= 1.99:
        total_sum+= 0.2
    elif 2 <= gold_wt<= 3.99:
        total_sum+= 0.4
    elif 4 <= gold_wt<= 5.99:
        total_sum+= 0.6
    elif 6 <= gold_wt<= 7.99:
        total_sum+= 0.8
    elif 8 <= gold_wt<= 9.99:
        total_sum+= 1
    elif 10 <= gold_wt<= 11.99:
        total_sum+= 1.2
    elif 12 <= gold_wt<= 13.99:
        total_sum+= 1.4
    elif 14 <= gold_wt<= 15.99:
        total_sum+= 1.6
    elif 16 <= gold_wt<= 19.99:
        total_sum+= 1.8
    elif 20 <= gold_wt<= 23.99:
        total_sum+= 2
    elif 24 <= gold_wt<= 27.99:
        total_sum+= 2.2
    elif 28 <= gold_wt<= 31.99:
        total_sum+= 2.4
    elif 32 <= gold_wt<= 35.99:
        total_sum+= 2.6
    elif 36 <= gold_wt<= 39.99:
        total_sum+= 2.8
    elif 40 <= gold_wt<= 49.99:
        total_sum+= 3
    elif 50 <= gold_wt<= 59.99:
        total_sum+= 3.2
    elif 60 <= gold_wt<= 69.99:
        total_sum+= 3.4
    elif 70 <= gold_wt<= 79.99:
        total_sum+= 3.6
    elif 80 <= gold_wt<= 89.99:
        total_sum+= 3.8
    elif 90 <= gold_wt<= 99.99:
        total_sum+= 4
    elif 100 <= gold_wt<= 5000:
        total_sum+= 4.2
    # else:
    #     return "Out of range"
    count+=1

    return total_sum,count


def Surface_area(S_area,count):
    total_sum=0
    if 1 <= S_area <= 499:
        total_sum+= 0.25
    elif 500 <= S_area <= 899:
        total_sum+= 0.35
    elif 900 <= S_area <= 1300:
        total_sum+= 0.45
    elif 1301 <= S_area <= 1500:
        total_sum+= 0.55
    elif 1501 <= S_area <= 1700:
        total_sum+= 0.65
    elif 1701 <= S_area <= 1800:
        total_sum+= 0.75
    elif 1801 <= S_area <= 2000:
        total_sum+= 0.85
    elif 2001 <= S_area <= 2200:
        total_sum+= 0.95
    elif 2201 <= S_area <= 2300:
        total_sum+= 1.05
    elif 2301 <= S_area <= 2500:
        total_sum+= 1.15
    elif 2501 <= S_area <= 2700:
        total_sum+= 1.25
    elif 2701 <= S_area <= 2900:
        total_sum+= 1.35
    elif 2901 <= S_area <= 3000:
        total_sum+= 1.45
    elif 3001 <= S_area <= 3100:
        total_sum+= 1.55
    elif 3101 <= S_area <= 3200:
        total_sum+= 1.65
    elif 3200 <= S_area <= 3300:
        total_sum+= 1.75
    elif 3301 <= S_area <= 3400:
        total_sum+= 1.85
    elif 3401 <= S_area <= 3500:
        total_sum+= 1.95
    elif 3501 <= S_area <= 3700:
        total_sum+= 2.05
    elif 3701 <= S_area <= 3900:
        total_sum+= 2.15
    elif 3901 <= S_area <= 4200:
        total_sum+= 2.25
    elif 4201 <= S_area <= 4500:
        total_sum+= 2.35
    elif 4501 <= S_area <= 4800:
        total_sum+= 2.45
    elif 4801 <= S_area <= 5000:
        total_sum+= 2.55
    elif S_area > 5000:
        total_sum+= 2.65
    # else:
    #     totalsum+= "Out of range"


    return total_sum,count
