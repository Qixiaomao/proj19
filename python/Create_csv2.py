import csv


with open('name.csv','w') as csvfile:
   filenames = ['first_name','last_name']
   writer = csv.DictWriter(csvfile,filenames)

   writer.writeheader()  
   writer.writerow({"first_name":"Baked","last_name":"Beans"})
   writer.writerow({"first_name":"Lovely","last_name":"Ben"})
   writer.writerow({"first_name":"Beatiful","last_name":"Boy"})