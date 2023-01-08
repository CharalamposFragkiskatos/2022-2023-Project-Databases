import random

table_name = 'guided_tour'
SqlInsertData = ''
#30 guided tours
id = 0
for i in range (30):
    id+=1
    cost = random.choice(['1.00','2.00','3.00','4.00','5.00','10.00','15.00','20.00','25.00'])
    duration = random.choice(['30min','1h','2h','3h'])
    date = '2023-'+ str(random.choice([k for k in range(1,13)])) +'-' +str(random.choice([k for k in range(1,29)]))
    time = str(random.choice([k for k in range(10,21)]))+':'+'00:00'
    language = random.choice(["Ελληνικά","Αγγλικά"])
    atrno = '0'
    name = 'Guided tour' + str(id) + 'xx'
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(id) +"', '"\
        + name +"', '"\
        + duration +"', '"\
        + date +"', '"\
        + time +"', '"\
        + language+"', '"\
        + cost+"', '"\
        + atrno+ "');\n"

with open('creatingguides.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)