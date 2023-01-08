import csv
import random 
names = []
cousine = []
priceLevel = []
phone = []
address = []
rating = []
table_name = 'Business'
table_name2 = 'Estiasi'

loc = ['Βαλσαμάτα', 'Γριζάτα', 'Ζόλα', 'Διλινάτα', 'Αγία Ειρήνη', 'Καμιναράτα',\
    'Μιτικάτα','Μακρυώτικα', 'Τζανάτα','Φαρακλάτα', 'Πλάκα','Άδαμας','Περιστέρι'\
        ,'Χαλάνδρι','Κηφισιά','Γλυφάδα','Πειραιάς','Αγυιά','Κέντρο','Φάληρο','Φώκι']
xy = [ [10,10], [11,11], [16,1], [16,2],[1,1],[2,2],[1,2],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[6,5],[5,1],[3,5],[7,4],[9,3],[7,9],[7,8],[3,10]]
SqlInsertData = ''
SqlInsertData2 = ''

with open('restaurants.csv', 'r', encoding = 'utf-8') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        if row[0] == '': names.append('NULL')
        else: names.append(row[0].replace("'",""))

        if row[2] == '': cousine.append('NULL') 
        else: cousine.append(row[2])

        if row[-3] == '': phone.append('NULL')
        else: phone.append(row[-3])

        if row[-1] == '': rating.append('NULL')
        else: rating.append(row[-1])

        if row[-2] == '': address.append('NULL')
        else: address.append(row[-2].replace("'",""))

        if row[-4] == '': priceLevel.append('NULL')
        else: priceLevel.append(row[-4])
    
for i in range(1,501):
    ind = random.randint(0,20)
    xwrio = loc[i%21] 
    x = xy[i%21][0] + random.randint(0,999)/1000
    y = xy[i%21][1] + random.randint(0,999)/1000
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(i) +"', '"\
        + names[i] +"', '"\
        + "www.res" + str(i) + "food.gr" + "', '"\
        + xwrio+ "', '"\
        + priceLevel[i] + "', '"\
        + '0'+ "', '"\
        + '0'+ "', '"\
        + phone[i]+str(i)+ "', '"\
        + str(x) + "', '"\
        + str(y) + "');\n"

    SqlInsertData2 += " INSERT INTO '" + table_name2 + "' VALUES ('" \
        + str(i) +"', '"\
        + cousine[i] + "');\n"

with open('creatingbusiness.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)

with open('creatingrestaurants.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData2)