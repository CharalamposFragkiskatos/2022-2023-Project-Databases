'''import random
SqlInsertData = ''
table_name = 'covered_by'
TransID = [k for k in range(1,7)]
for DestID in range (1,23):
    numOfCov = random.randint(1,4)
    random.shuffle(TransID)
    for i in range(numOfCov):
        SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(TransID[i]) +"', '"\
        + str(DestID)+ "');\n"
with open('creatingcovers.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)'''

import random
SqlInsertData = ''
table_name = 'saved'
TransID = [k for k in range(1,7)]
for userID in range (1,501):
    numOfCov = random.choice([0,0,0,0,0,0,0,0,0,1,2,3,4])
    random.shuffle(TransID)
    for i in range(numOfCov):
        SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + str(userID) +"', '"\
        + str(TransID[i])+ "');\n"
with open('creatingsaves.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)