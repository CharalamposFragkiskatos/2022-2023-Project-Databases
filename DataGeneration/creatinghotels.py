import random 
names = []
payrange = ['€€ - €€€','€','€€€€']
table_name = 'Business'
table_name2 = 'Accomodation'
loc = ['Βαλσαμάτα', 'Γριζάτα', 'Ζόλα', 'Διλινάτα', 'Αγία Ειρήνη', 'Καμιναράτα',\
    'Μιτικάτα','Μακρυώτικα', 'Τζανάτα','Φαρακλάτα', 'Πλάκα','Άδαμας','Περιστέρι'\
        ,'Χαλάνδρι','Κηφισιά','Γλυφάδα','Πειραιάς','Αγυιά','Κέντρο','Φάληρο','Φώκι']
xy = [ [10,10], [11,11], [16,1], [16,2],[1,1],[2,2],[1,2],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[6,5],[5,1],[3,5],[7,4],[9,3],[7,9],[7,8],[3,10]]
SqlInsertData = ''
SqlInsertData2 = ''

for l1 in "abcdef":
    for l2 in "abcdef":
        names.append("hotel"+l1+l2)
type = ['Ξενοδοχείο','Διαμέρισμα','Hostel','Βίλα']        
id = 500
for name in names:
    id += 1             #id
                        #name
    s = random.randint(0,20)
    phones = '222' + str(id) + '23456' #phone
    locs = loc[s] # location
    x = xy[s][0] + random.randint(0,999)/1000 #x
    y = xy[s][1] + random.randint(0,999)/1000 #y
    address = 'Address '+ str(id) + ' hotelstreet' #address
    range = payrange[s%3] #payrange
    Url = "www.hotel"+str(id)+"hotels.stay.gr" #url
    rating = 0;
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(id) +"', '"\
        + name +"', '"\
        + Url+ "', '"\
        + locs+ "', '"\
        + range+ "', '"\
        + '0'+ "', '"\
        + '0'+ "', '"\
        + phones+ "', '"\
        + str(x) + "', '"\
        + str(y) + "');\n" 

    SqlInsertData2 += " INSERT INTO '" + table_name2 + "' VALUES ('" \
        + str(id) +"', '"\
        + type[s%4] + "');\n" 

with open('creatingbusiness2.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)

with open('creatinghotels.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData2)
