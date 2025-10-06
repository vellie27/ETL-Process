📦 ETL Process with Pandas

📝 Project Description

This project contains a simple, yet robust, ETL (Extract, Transform, Load) pipeline written in Python using the Pandas library for data manipulation. It is designed to read sales data from a CSV file, perform basic data cleaning and transformation (such as calculating a total price and converting a date column), and save the processed data to a new CSV file.


🛠️ Requirements

To run this script, you'll need Python and the pandas library.


Python (3.6+)


pandas


Installation

You can install pandas using pip:


Bash


pip install pandas

📂 Project Structure

For the script to run successfully, ensure your files are organized as follows:


etl_project/

├── etl_script.py         # The main ETL Python script (your code)

└── sales_data_sample.csv # The input CSV file (must be present)

Note: The script expects an input file named sales_data_sample.csv in the same directory. The output file, transformed_data.csv, will be created in the same directory upon successful execution.


🏃 How to Run

Save the Code: Save your provided Python code into a file named etl_script.py.


Prepare Input Data: Ensure you have your raw data file named sales_data_sample.csv in the same directory as etl_script.py.


The input CSV must contain at least the following columns for the transformation step to work: quantity, unit_price, and order_date.


Execute the script: Run the script from your terminal:


Bash


python etl_script.py

✅ Transformation Logic

The transform_data function performs the following steps:


Feature Engineering: A new column, total_price, is calculated by multiplying the quantity and unit_price columns:

df[’total_price’]=df[’quantity’]∗df[’unit_price’]


Data Type Conversion: The order_date column is converted to the proper datetime object type.


Data Cleaning: All rows containing any NaN (Not a Number) or null values are dropped using df.dropna().


⚙️ Logging


The script uses Python's built-in logging module to provide informative messages about the ETL process's status, including successful completion of each stage (Extract, Transform, Load) or any errors encountered. Messages are printed to the console.


🤝 Code Reference

Function	Purpose

extract_data(file_path)	Reads the CSV file specified by file_path into a Pandas DataFrame.

transform_data(df)	Performs data calculations, type conversions, and cleaning on the DataFrame.
load_data(df, output_path)	Writes the resulting DataFrame to a new CSV file at output_path.
etl()	Orchestrates the entire ETL process, calling the functions in sequence.
