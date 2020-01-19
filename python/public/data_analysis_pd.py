# -*- conding: utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import sqlite3



# 收集数据
def collect_data():
    df_arr_list = []
    conn = sqlite3.connect("humi.db")
    c = conn.cursor()
    #sql = "SELECT HUMI, TEMP from htdb;"
    sql = c.execute("SELECT HUMI, TEMP  from htdb")
    df_arr_list.append("HUMI")
    df_arr_list.append("TEMP")
    for row in sql:
      #print ("HUMI = ", row[0])
      #print ("TEMP = ", row[1])
      #print ("\n")
      df_arr_list.append(row)
    
    print(df_arr_list)
    #df_arr_list.append(df)  
    #print(type(df_arr_list))    
    
    
    
    
    

# 数据处理
def process_data(df_arr_list):
    #print(type(df_arr_list))
    i = 0
    for df_arr in df_arr_list:
       i = i+1
       print(i)
       print(type(df_arr))
       print(df_arr)

    return df_arr_list
    
    #pass
# 数据分析


# 数据展示
def save_data():
    pass

# 主函数
def main():
    
    

# 数据获取
    df_arr_list = collect_data()

# 数据处理
    #process_data(df_arr_list)

# 数据分析

# 结果展示


if __name__ == "__main__":
    main()