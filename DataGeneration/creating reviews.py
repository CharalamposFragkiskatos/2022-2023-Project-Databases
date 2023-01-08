import random

listtp = []
table_name = 'REVIEW'
SqlInsertData = ''
rate = ['1','1.5','2','2.5','3','3.5','4','4.5','5']
comment = ['Πολύ κακό', 'Κακό', 'Όχι καλό', 'Κάτω του μετρίου','Μέτριο', 'Άνω του μετρίου', 'Όχι κακό','Καλό','Πολύ καλό']
for bus_id in range(1,537):
    for user_id in range(1,501):
        listtp.append((bus_id,user_id))
random.shuffle(listtp)

for i in range (5000):
    s = random.randint(0,8)
    bus = str(listtp[i][0])
    us = str(listtp[i][1])
    if random.randint(1,100) == 51: continue
    SqlInsertData += " INSERT INTO '" + table_name + "' VALUES ('" \
        + us +"', '"\
        + bus +"', '"\
        + comment[s] +"', '"\
        + rate[s]+"', '"\
        + random.choice(['2021-','2022-','2020-','2019-']) + str(random.choice([k for k in range(1,13)])).zfill(2) +"-"+ str(random.choice([k for k in range(1,29)])).zfill(2)+ "');\n"

with open('creatingreviews.sql', 'w',encoding = 'utf-8') as f:
  # Write the string to the file
  f.write(SqlInsertData)
