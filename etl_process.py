## ETL process
## extracting csv file

import pandas as pd
import logging

# setup the logging
logging.basicConfig(lcevel=logging.INFO)
logger = logging.getLogger(__name__)
input_file_path = "sales_data_sample.csv"  
output_file_path = "transformed_data.csv"
def extract_data("C:"):
    '''extract the data from csv file'''
    try:
        df = pd.read_csv(file_path)
        logger.info('Data extracted successfully!!')
        return df
    except Exception as e:
        logger.error(f'Error extracting data: {e}') 
        raise 
    
## transform data
    
def transform_data(df):
    try:
        df['total_price'] = df['quantity'] * df['unit_price']
        df['order_date'] = pd.to_datetime(df['order_date'])
        df = df.dropna()
        logger.info("Data transformation is successful!!")
        return df
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise
        
## load data

def load_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        logger.info('Data loading is successful!!')
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise
    
def etl():
    try:
        input_file_path = "sales_data_sample.csv" 
        output_file_path = "transformed_data.csv" 
        
        data = extract_data(input_file_path)
        data = transform_data(data)
        load_data(data, output_file_path)
        
        logger.info("ETL process completed successfully!!")
    except Exception as e:
        logger.error(f"Error: ETL process failed!!: {e}")
    
if __name__ == "__main__":
    etl()