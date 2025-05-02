#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# task a
import csv

def load_csv_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return []

def task_a1(data, card_type=None):
    if not card_type:
        card_type = input("Enter Card Type (e.g. Blue): ").strip().lower()

    header = data[0]
    rows = data[1:]
    found = False

    for row in rows:
        if row[header.index('Card_Category')].strip().lower() == card_type:
            print(f"Client: {row[header.index('Client_Num')]} | "
                  f"Gender: {row[header.index('Gender')]} | "
                  f"Education: {row[header.index('Education_Level')]} | "
                  f"Income: {row[header.index('Income')]}")
            found = True

    if not found:
        print(f"No customers found with card type '{card_type}'.")

def task_a2(data, state=None):
    if not state:
        state = input("Enter State Code (e.g. CA): ").strip().upper()

    header = data[0]
    rows = data[1:]
    found = False

    for row in rows:
        if row[header.index('state_cd')].strip().upper() == state:
            print(f"Age: {row[header.index('Customer_Age')]} | "
                  f"Gender: {row[header.index('Gender')]} | "
                  f"Income: {row[header.index('Income')]} | "
                  f"Card: {row[header.index('Card_Category')]}")
            found = True

    if not found:
        print(f"No customers found from state '{state}'.Please check your spelling")
def task_a3(data, status=None):
    if not status:
        status = input("Enter Marital Status (e.g. Married): ").strip().lower()

    header = data[0]
    rows = data[1:]
    found = False

    for row in rows:
        if row[header.index('Marital_Status')].strip().lower() == status:
            try:
                dependents = int(row[header.index('Dependent_Count')])
            except ValueError:
                continue
            if dependents > 3:
                print(f"Age: {row[header.index('Customer_Age')]} | "
                      f"Gender: {row[header.index('Gender')]} | "
                      f"Education: {row[header.index('Education_Level')]} | "
                      f"Job: {row[header.index('Customer_Job')]}")
                found = True

    if not found:
        print(f"No customers found who are '{status}' with more than 3 dependents.")

def task_a4(data):
    
    header = data[0]
    rows = data[1:]
    found = False

    for row in rows:
        house_owner = row[header.index('House_Owner')].strip().lower()
        if house_owner == 'no':  # renters
            try:
                credit_limit = float(row[header.index('Credit_Limit')])
            except ValueError:
                continue  # skip rows with invalid credit limit

            if credit_limit > 5000:
                print(f"Client: {row[header.index('Client_Num')]} | "
                      f"House Owner: {row[header.index('House_Owner')]} | "
                      f"Credit Limit: {row[header.index('Credit_Limit')]} | "
                      f"Income: {row[header.index('Income')]}")
                found = True

    if not found:
        print("No customers found who do not have house and have a credit limit over 5000.")

