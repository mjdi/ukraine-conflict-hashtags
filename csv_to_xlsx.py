import pandas as pd
import openpyxl
import os

DATA_FOLDER_PATH = '.\\data\\'

TOP_HASHTAGS_PER_DAY_FOLDER_PATH =  DATA_FOLDER_PATH + "top_hashtags_per_day\\"
TOP_HASHTAGS_XLSX_PER_DAY_FOLDER_PATH =  DATA_FOLDER_PATH + "top_hashtags_per_day_xlsx\\"

for filename in os.listdir(TOP_HASHTAGS_PER_DAY_FOLDER_PATH):
    read_file = pd.read_csv(os.path.join(TOP_HASHTAGS_PER_DAY_FOLDER_PATH, filename))
    print("converting " + filename + " to xlsx") 
    
    filename_without_extension = filename.split('.')[0]
    filename = filename_without_extension + ".xlsx"
    read_file.to_excel (os.path.join(TOP_HASHTAGS_XLSX_PER_DAY_FOLDER_PATH, filename), index = None, header=True)