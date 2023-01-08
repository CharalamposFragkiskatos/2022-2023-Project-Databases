import random
import string
import csv
table_name = 'User'
fnames = []
lnames = []
with open('names.csv', 'r', encoding = 'utf-8') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        if row[0].split()[0] == '': fnames.append('NULL')
        else: fnames.append(row[0].split()[0])
        if row[0].split()[1] == '': lnames.append('NULL')
        else: lnames.append(row[0].split()[1])
size = len(lnames)
SqlInsertData = ''
id = 0
for i in range(size):
    stri = ''.join(random.choices(string.ascii_letters, k=7))+'@gmail.com'
    id+=1
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(id) +"', '"\
        + fnames[i] +"', '"\
        + lnames[i] +"', '"\
        + fnames[i]+str(id)+"@gmail.com"+ "');\n"
with open('creatingusers.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)