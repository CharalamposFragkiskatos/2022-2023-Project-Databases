import random
import string
table_name = 'a'
#           0         1         2         3        4        5         6         7         8          9
type = ['Μνημείο','Μουσείο', 'Γέφυρα', 'Ναός', 'Λίμνη', 'Παραλία', 'Μνημείο', 'Κτίριο', 'Πλατεία', 'Πάρκο'] 


name = ['Κόκκινη Γέφυρα', 'Δίας ο Χρυσός','Ναός Λύτρωσης','Απολλώνιο','Κίμη','Μελλίσια','Βιβλιοθήκη','Burdan','Σελήνιο',\
    'Πλατεία εξεγέρσεως','Ναός Θεοτώκου','Κιμ-Κομ','Νεκροταφείο των πεσόντων','Μουσείο Φυσικής Ιστορίας','Μουσείο Μοντέρνας Τέχνης','Μουσείο Ανθρωπολογίας',\
        'Μουσείο Επιστήμης','Μουσείο Απολλωνίου','Κοινοβούλιο των εθνών','Όπερα της Μονπάρτης','Αστεροσκοπείο','Δημαρχείο','Βασιλική Αγίου Παύλου',\
            'Πολεμικό Μουσείο','Ανώτατη Σχολή Επιστημών και Μηχανικής','Πλατεία Βασιλέως','Άγαλμα κυβερνήτη','Εθνικός Κήπος','Κήποι Ανακτόρων',\
                'Αυτοκρατορική πλατεία','Πάρκο Σεντραλ','Ναός Δωδεκάθεου','Μουσείο κλασσικής αρχιτεκτονικής','Πλατεία Ειρήνης']
nametotype = [2,  6,  3,  0,  4,  5,  7,  7,  0, 8, 3, 2, 0, 1, 1, 1, 1, 1, 7, 7, 7, 7, 3, 1, 7, 8, 6, 9,9,8,9,0,1,8]
timi = ['7.00', '5.00', '0.00', '12.00', '13.50', '4.00', '8.50', '10.00']
xr = [i for i in range(30,1900)]
location = ['Πλάκα', 'Εκκλησάκι', 'Λιθόστροτο', 'Αμπελώνας', 'Παγώνι', 'Ιερέα', 'Σαρδήνου', 'Χαλαρι', 'Φωτίτσες', 'Θαλασσιά', 'Αλατερός', 'Κέντρο'] 
address =['Ποσειδώνος', 'Αρτέμιδος', 'Γεωργίου Α', 'Πάρη', 'Γρηγορίου', 'Νικολάου', 'Ισμήνης', 'Τριών Σμηναγών', 'Πειρατών', 'Γητευτή','Άννας']
xr2 = [i for i in range(1990,2020)]
eur = '€'
id = 923201
SqlInsertData = ''
for i in range(len(name)):
    id+=1
    id_i = str(id)
    
    name_i = name[i]

    type_i = type[nametotype[i]]

    if type[nametotype[i]] in ['Λίμνη','Πλατεία','Πάρκο','Παραλία']:
        timi_i ="0.00 €"
    else: timi_i = random.choice(timi)+" €"

    if type[nametotype[i]] in ['Λίμνη','Πλατεία','Πάρκο','Παραλία']:
        xr_i =  str(random.choice(xr)) 
    else: xr_i =  str(random.choice(xr2)) 

    if type[nametotype[i]] in ['Λίμνη','Πλατεία','Πάρκο','Παραλία']:
        url_i =  "NULL"
    else: url_i =  "https://www."+type[nametotype[i]].replace(" ","") + str(i) + ".tourism.com"

    if type[nametotype[i]] in ['Λίμνη','Παραλία']:
        loc_i = name[i]
        add_i = 'NULL'
    else:
        loc_i = random.choice(location)
        add_i = random.choice(address)+" "+ str(random.choice([u for u in range(1,150)]))
    SqlInsertData += " INSERT INTO " + table_name + " VALUES ('" \
        + id_i +"', '"\
        + name_i +"', '"\
        + type_i+ "', '"\
        + loc_i+ "', '"\
        + add_i+ "', '"\
        + xr_i+ "', '"\
        + url_i+ "', '"\
        + timi_i + "');\n"

    print(SqlInsertData)

