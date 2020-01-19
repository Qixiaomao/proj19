#coding:utf-8
import pandas as pd
 
fileName = 'PythonBook.csv'
number = 1
 
books = []
book = {
 'title': 'Book',
 'author': 'Jack',
}
# 如果 book 条数足够多的话，pandas 会每次往文件中写 50 条数据。
books.append(book)
 
data = pd.DataFrame(books)
# 写入csv文件,'a+'是追加模式
try:
 if number == 1:
     csv_headers = ['BookName', 'Author']
     data.to_csv(fileName, header=csv_headers, index=False, mode='a+', encoding='utf-8')
 else:
     data.to_csv(fileName, header=False, index=False, mode='a+', encoding='utf-8')
     number = number + 1
except UnicodeEncodeError:
     print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
    
    