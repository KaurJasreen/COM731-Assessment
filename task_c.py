#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# task c
import matplotlib.pyplot as plt
import pandas as pd
import csv

def task_c1(df):
    
    edu = input("Enter Education Level (e.g. Graduate): ").strip().lower()
    try:
        filtered = df[df['Education_Level'].str.lower() == edu]
        counts = filtered['Card_Category'].value_counts()
        plt.figure(figsize=(6,6))
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
        plt.title(f"Card Type Proportion for Education Level: {edu.title()}")
        plt.show()
    except Exception as e:
        print("Error:", e)



def task_c2(df):

    # Ensure date column is in datetime format
    df['Week_Start_Date'] = pd.to_datetime(df['Week_Start_Date'], errors='coerce')

    # Create 'Month' column in YYYY-MM format
    df['Month'] = df['Week_Start_Date'].dt.to_period('M').astype(str)

    # Group by Month and Card Type
    monthly_interest = df.groupby(['Month', 'Card_Category'])['Interest_Earned'].mean().unstack()

    # Plotting
    monthly_interest.plot(kind='line', marker='o', figsize=(8, 6))
    plt.title('Monthly Trend of Average Interest Earned by Card Type')
    plt.xlabel('Month')
    plt.ylabel('Average Interest Earned')
    plt.xticks(rotation=45)
    plt.legend(title='Card Type',loc= 'upper right',bbox_to_anchor=(1.5,1))
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def task_c3(df):
    try:
        grouped = df.groupby('Card_Category')[['Annual_Fees', 'Customer_Acq_Cost']].mean()
        grouped.plot(kind='bar', figsize=(8,6))
        plt.title("Avg Annual Fees & Acquisition Cost by Card Type")
        plt.ylabel("Amount ($)")
        plt.xlabel("Card Type")
        plt.grid(True)
        plt.legend(title='metrics',loc= 'upper right',bbox_to_anchor=(1.5,1))
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)

def task_c4(df):
    try:
        # Example: Total Transaction Amount by Education Level
        grouped = df.groupby('Education_Level')['Total_Trans_Amt'].mean()
        grouped.plot(kind='bar', figsize=(8,6), color='skyblue')
        plt.title("Avg Transaction Amount by Education Level")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)

