# -*- conding:utf-8 -*-

'''
The target:
Analysist the data.

'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# the data of file a path.
Data_path = ""

# save the result of the data
output_path = "./output"
if not os.path.exists(output_path):
    os.makedirs(output_path)


def collect_data():
    '''
       colloect the data.

    '''
    data_df = pd.read_csv(Data_path)
    return data_df

def process_data(data_df):
    '''
      process data.
    '''
    data_df.dropna(inplace = True)
    data_df.sort_values(['Humi','Temp'],ascending=[True,False],inplace=False)

    return data_df

def analyze_data(data_df):
    '''
       analyze data.
    '''

def save_show_results():
    '''
       display the results.

    '''
    pass


def main():
    '''
       mian.
    '''
    # collect the data
    data_df = collect_data()

    # process the data
    data_data_df = process_data(data_df)

    # analyze the data
     humi,temp = analyze_data(data_df)

    # display the result
    save_show_results(humi,temp)

if __name__ == '__main__':
    main()