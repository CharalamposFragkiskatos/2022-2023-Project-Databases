import random
import string
table_name = 'a'
#           0         1          2                    3           4        
type = ['Συναυλία','Πανηγύρι', 'Υπαίθρια Αγορά', 'Φεστιβάλ', 'Παράσταση'] 


name = ['Πανηγύρι κρέατος', 'Κονσέρτο Κλασσικής Μουσικής', '3ο Φεστιβάλ κινηματογράφου', 'Χριστουγεννιάτικη αγορά', 'Αγορά μπαχαρικών',\
    'Συναυλία Σάκη Ρουβά', 'Ασπασία', 'Πανηγύρι κάτω χώρας', 'Παζάρι Αγ. Νικολάου', 'Φεστιβάλ Επιστήμης', 'Βέρθερος']
location = ['Πλάκα', 'Εκκλησάκι', 'Λιθόστροτο', 'Αμπελώνας', 'Παγώνι', 'Ιερέα', 'Σαρδήνου', 'Χαλαρι', 'Φωτίτσες', 'Θαλασσιά', 'Αλατερός', 'Κέντρο'] 
nametotype = [1, 0,3,2,2,0,4,1,1,3,4]
address =['Ποσειδώνος', 'Αρτέμιδος', 'Γεωργίου Α', 'Πάρη', 'Γρηγορίου', 'Νικολάου', 'Ισμήνης', 'Τριών Σμηναγών', 'Πειρατών', 'Γητευτή','Άννας']

timi = ['7.00', '5.00', '0.00', '12.00', '13.50', '4.00', '8.50', '10.00']
xr = [i for i in range(30,1900)]
xr2 = [i for i in range(1990,2020)]
eur = '€'
id = 923201
SqlInsertData = ''
for i in range(len(name)):
    id+=1
    id_i = str(id)
    name_i = name[i]
    type_i = type[nametotype[i]]
    if name[nametotype[i]] in ['Λίμνη','Πλατεία','Πάρκο','Παραλία']:
        timi_i ="0.00 €"
    else: timi_i = random.choice(timi)+" €"
    if name[nametotype[i]] in ['Λίμνη','Πλατεία','Πάρκο','Παραλία']:
        xr_i =  str(random.choice(xr)) 
    else: xr_i =  str(random.choice(xr2)) 
    url_i =  type[nametotype[i]].replace(" ","") + str(i) + "@gmail.com"
    SqlInsertData += " INSERT INTO " + table_name + " VALUES ('" \
        + id_i +"', '"\
        + name_i +"', '"\
        + type_i+ "', '"\
        + xr_i+ "', '"\
        + url_i+ "', '"\
        + timi_i + "');\n"

    print(SqlInsertData)

