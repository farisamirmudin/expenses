
#!/usr/bin/env python3
from datetime import datetime, date
from pathlib import Path
import os
import pandas as pd

def create_new_sheets(sheet_name, df):
    writer = pd.ExcelWriter(sheet_name, engine='xlsxwriter') # Create excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False) # Convert data frame to excel
    writer.save()

def append_new_value(sheet_name, df):
    existing_df = pd.read_excel(sheet_name) # Read existing dataframes
    new_df = pd.concat([existing_df, df]) # Append new data to existing dataframe
    writer = pd.ExcelWriter(sheet_name, engine='xlsxwriter') 
    new_df.to_excel(writer, sheet_name='Sheet1', index=False) # Overwrite old excel file
    writer.save()

def main():
    '''
    Excel file will be saved at Documents/Expenses
    '''
    home = str(Path.home())
    # os.chdir(os.path.dirname(__file__)) # Get the directory name of the current script and change working directory to it
    work_dir = f'{home}/Documents/Expenses' # Change working directory to Documents/Expenses
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)
    os.chdir(work_dir)
    # second= datetime.now().second
    # minute = datetime.now().minute
    # hour = datetime.now().hour
    day = datetime.now().day # Current day
    month = datetime.now().month # Current Month
    year = datetime.now().year # Current year

    today = date.today().strftime(f"%d/%m/%Y") # Get today's date
    months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}
    sheet_name = f'{months[month]} {year}.xlsx' # Name of excel file
    ask = 'y' # Continue as long as the user has new input
    while ask == 'y':
        time = datetime.now().strftime("%H:%M:%S") # Current time
        value = float(input('Enter your new expense: ').replace(',', '.')) # Ask for value and convert it to float
        desc = input('Enter description: ') # Description of the new value
        df = pd.DataFrame({'Date':[today], 'Time':[time], 'Value':[value], 'Description':[desc]}) # Create new data frame consisting of date, time, value and description
        if os.path.exists(sheet_name): # Check if this is the first time the excel file is created
            append_new_value(sheet_name, df) # Append new value to existing excel
        else:
            create_new_sheets(sheet_name, df) # Create new excel file
        ask = input('Enter more? [y/n]: ') # Ask if the user wants to input new value

if __name__ == '__main__':
    main()
    

