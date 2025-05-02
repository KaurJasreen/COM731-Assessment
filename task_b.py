#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# task b
import pandas as pd
import csv

def load_dataframe(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def task_b1(df):
    card = input("Enter Card Type (e.g. Blue): ").strip().lower()
    try:
        result = df[df['Card_Category'].str.lower() == card]
        result = result[result['Income'] > 100000]
        top_occupations = result['Customer_Job'].value_counts().head(3)
        print("\nTop 3 Occupations:")
        print(top_occupations)
    except Exception as e:
        print("Error:", e)

def task_b2(df):
    job = input("Enter customer job (e.g. Businessman): ").strip().lower()
    card = input("Enter Card Type (e.g. Blue): ").strip().lower()

    # Normalize the relevant columns
    df['job_lower'] = df['Customer_Job'].astype(str).str.lower().str.strip()
    df['card_lower'] = df['Card_Category'].astype(str).str.lower().str.strip()

    filtered = df[(df['job_lower'] == job) & (df['card_lower'] == card)]

    if filtered.empty:
        print("No matching records found for that job and card type.")
    else:
        try:
            avg_fee = filtered['Annual_Fees'].mean()
            avg_income = filtered['Income'].mean()
            print(f"\nAverage Annual Fee: ${avg_fee:.2f}")
            print(f"Average Income: ${avg_income:.2f}")
        except Exception as e:
            print("An error occurred during calculation:", e)

def task_b3(df):
    edu = input("Enter Education Level (e.g. Graduate): ").strip().lower()
    home = input("Enter Homeownership (Yes/No): ").strip().lower()
    try:
        income_threshold = float(input("Enter minimum income (e.g. 50000): "))
        filtered = df[(df['Education_Level'].str.lower() == edu) &
                      (df['House_Owner'].str.lower() == home) &
                      (df['Income'] > income_threshold)]
        result = filtered.groupby('Marital_Status')['Annual_Fees'].mean()
        print("\nAverage Annual Fee by Marital Status:")
        print(result)
    except Exception as e:
        print("Error:", e)

def task_b4(df):
    # Example: Find average interest earned by education level
    try:
        result = df.groupby('Education_Level')['Interest_Earned'].mean()
        print("Average Interest Earned by Education Level:")
        print(result)
    except Exception as e:
        print("Error:", e)

