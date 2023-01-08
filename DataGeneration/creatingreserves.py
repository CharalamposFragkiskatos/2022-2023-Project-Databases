import random

table_name = 'Reserves'
SqlInsertData = ''
#30 tours
#500 users
t = []
tourIDl = [k for k in range(1,31)]
userIDl = [k for k in range(1,501)]
for item1 in userIDl:
    for item2 in tourIDl:
        t.append(((item1,item2)))
random.shuffle(t)
for i in range (1000):
    tourID = str(t[i][1])
    userID = str(t[i][0])
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + userID +"', '"\
        + tourID+ "');\n"

with open('creatingreserves.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)