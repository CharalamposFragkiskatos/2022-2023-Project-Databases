import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
import sqlite3
import time
import csv

root = tk.Tk()

OutputBox = tk.Text(root,bg = "white",fg = "black", height = 25, width = 130, insertofftime = 500, \
        insertontime = 500, insertwidth=0.5, cursor = "arrow",insertbackground = "white", state = 'disabled',wrap = tk.NONE)

class DataModel():
    '''Κλάση σύνδεσης με τη βάση δεδομένων και δημιουργίας δρομέα'''
    def __init__(self, filename):
        self.filename = filename
        try:
            self.con = sqlite3.connect(filename)
            self.con.row_factory = sqlite3.Row  # ώστε να πάρουμε τα ονόματα των στηλών του πίνακα
            self.cursor = self.con.cursor()
            print("Επιτυχής σύνδεση στη βάση δεδομένων", filename)
            sqlite_select_Query = "select sqlite_version();"
            self.cursor.execute(sqlite_select_Query)
            record = self.cursor.fetchall()
            for rec in record:
                print("SQLite Database Version is: ", rec[0])
        except sqlite3.Error as error:
            print("Σφάλμα σύνδεσης στη βάση δεδομένων sqlite", error)
    
    def close(self):
        self.con.commit()
        self.con.close()

    def insertRow(self, query):
        try:
            t1 = time.perf_counter()
            for statement in query.split(";"):
                self.cursor.execute(statement)
            self.con.commit()
            sql_time = time.perf_counter() - t1
            print(f'εκτέλεση εντολής σε {sql_time:.5f} sec')
            return True
        except sqlite3.Error as error:
            print(f"Σφάλμα εκτέλεσης εντολής εισαγωγής SQL", error)
            return False
    
    def executeSQL(self, query, show=False):
        try:
            t1 = time.perf_counter()
            for statement in query.split(";"):
                if statement.strip():
                    self.cursor.execute(statement)
                    sql_time = time.perf_counter() - t1
                    print(f'εκτέλεση εντολής {statement[:40]}... σε {sql_time:.5f} sec')
            if show:
                deleteTextBox(OutputBox)
                enterLine(" ".join(['{:<35}'.format(str(col[0]).upper())for col in self.cursor.description]), OutputBox)
                for row in self.cursor.fetchall():
                    enterLine(" ".join(['{:<35}'.format(str(item))for item in row]), OutputBox)
                    print(", ".join([str(item)for item in row]))
                    #print([item for item in row])
                
                

            self.con.commit()
            return True
        except sqlite3.Error as error:
            print(f"Σφάλμα εκτέλεσης εντολής SQL", error)
            return False

    def readTable(self, table):
        '''Φόρτωμα ενός πίνακα, όταν το προαιρετικό όρισμα machine πάρει τιμή, τότε επιστρέφει μόνο 
        τις εγγραφές που αφορούν τη συγκεκριμένη μηχανή'''
        try:
            query = f'''SELECT * FROM {table};'''
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            result = []
            for row in records:
                result.append(dict(row))
            return result
        except sqlite3.Error as error:
            print(f"Σφάλμα φόρτωσης πίνακα {table}", error)
    
    def _insertIntoTable(self, table, row_dict):
        ''' Εισαγωγή εγγραφής σε μορφή λεξικού σε πίνακα'''
        try:
            query_param = f"""INSERT INTO {table} ({",".join(row_dict.keys())}) VALUES ({", ".join((len(row_dict)-1) * ["?"])}, ?);"""
            data = tuple(row_dict.values())
            self.cursor.execute(query_param, data)
            self.con.commit()
            return True
        except sqlite3.Error as error:
            print(f"Σφάλμα εισαγωγής στοιχείων στον πίνακα {table}", error)
            return False
d = DataModel("final_bases.db")
def OnButton1Pressed():
    input = T.get(1.0,"end-1c")
    d.executeSQL(input,show=True)   

def OnButton2Pressed():
    sqlTxt = ''
    comboinput = combobox.get()
    filt = comboboxFilter.get()
    xwrio =comboboxLoc.get()
    loc = ['Βαλσαμάτα', 'Γριζάτα', 'Ζόλα', 'Διλινάτα', 'Αγία Ειρήνη', 'Καμιναράτα',\
    'Μιτικάτα','Μακρυώτικα', 'Τζανάτα','Φαρακλάτα', 'Πλάκα','Άδαμας','Περιστέρι'\
        ,'Χαλάνδρι','Κηφισιά','Γλυφάδα','Πειραιάς','Αγυιά','Κέντρο','Φάληρο','Φώκι']
    xy = [ ['10','10'], ['11','11'], ['16','1'], ['16','2'],['1','1'],['2','2'],['1','2'],['4','4'],['5','5'],['6','6']\
    ,['7','7'],['8','8'],['9','9'],['6','5'],['5','1'],['3','5'],['7','4'],['9','3'],['7','9'],['7','8'],['3','10']]
    x = 0
    y = 0
    for j in range(len(xy)):
        if loc[j] == xwrio:
            x = xy[j][0]
            y = xy[j][1]
            break

    state = checkbutton.getvar(checkbutton.cget("variable"))
    if comboinput == "Τουριστικοί Προορισμοί":
        sqlTxt = 'SELECT * FROM Destination'
    elif comboinput == "Εστιατόρια":
        sqlTxt = '''SELECT NAME,TYPE,price_range,rating FROM Estiasi AS E, BUSINESS AS B WHERE B.B_ID == E.e_ID '''
    elif comboinput == "Διαμονή":
        sqlTxt = 'SELECT NAME,TYPE,price_range,rating FROM Accomodation AS A, BUSINESS AS B WHERE B.B_ID == A.ac_ID '
    elif comboinput == "Δραστηριότητες":
        sqlTxt = '''SELECT a.type,d.title,a.cost FROM Activity as a, destination as d where
                        a.na_id == d.dest_id'''
    elif comboinput == "Ξεναγήσεις":
        sqlTxt = 'SELECT name, date, cost FROM Guided_tour'

    if state == '1' and (comboinput == "Εστιατόρια" or comboinput == "Διαμονή"):
        sqlTxt += ' AND (x-'+x+')*(x-'+x+') +(y-'+y+')*(y-'+y+')<1 '
    elif state == '1' and comboinput == "Τουριστικοί Προορισμοί":
        sqlTxt += ' WHERE (x-'+x+')*(x-'+x+') +(y-'+y+')*(y-'+y+')<1 '
    elif comboinput == "Ξεναγήσεις":
        sqlTxt += ' WHERE DATE > date("now")'

    if filt == 'Βαθμολογία' and comboinput in ["Διαμονή","Εστιατόρια"]:
        sqlTxt += ' ORDER BY rating desc'
    elif filt == 'Τιμή':
        if comboinput in ["Διαμονή","Εστιατόρια"]:
            sqlTxt += ''' ORDER BY
    CASE price_range
        WHEN '€' THEN 1
        WHEN '€€-€€€' THEN 2
        WHEN '€€€€' THEN 3
        ELSE 4
    END;'''
        elif comboinput == "Δραστηριότητες": sqlTxt += ' ORDER BY a.cost asc '
        else: sqlTxt += ' ORDER BY cost asc'
    print(sqlTxt)
    print(x,y)
    d.executeSQL(sqlTxt,show=True) 


def combobox_changed(event):
    comboinput = combobox.get()
    if comboinput == "Τουριστικοί Προορισμοί":
        comboboxFilter.config(state='readonly')
        comboboxFilter["values"] = [ "Τιμή"]

    elif comboinput == "Εστιατόρια":
        comboboxFilter.config(state='readonly')
        comboboxFilter["values"] = ["Βαθμολογία", "Τιμή"]

    elif comboinput == "Διαμονή":
        comboboxFilter.config(state='readonly')
        comboboxFilter["values"] = [ "Βαθμολογία", "Τιμή"]

    elif comboinput == "Δραστηριότητες":
        comboboxFilter.config(state='readonly')
        comboboxFilter["values"] = ["Τιμή"]

    elif comboinput == "Ξεναγήσεις":
        comboboxFilter.config(state='readonly')
        comboboxFilter["values"] = [ "Τιμή"]
    
def change_icon(text, window):
    ico = Image.open(text)
    photo = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(False, photo)

def enterWord(word):
    T.insert("insert", word)
    return

def enterLine(str,obj):
    obj.config(state='normal')
    obj.insert("insert", str + '\n')
    obj.config(state='disabled')
    return

def deleteTextBox(obj):
    obj.config(state='normal')
    obj.delete(1.0, tk.END)
    obj.config(state='disabled')
    return

def exitP():
    root.destroy()
    return

frame = tk.Frame(root,width = 700, height = 300,bg = "gray")
scrollbar = tk.Scrollbar(root)
scrollbar2 = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=OutputBox.xview)
T = tk.Text(root,bg = "black",fg = "white", height = 25, width = 50, insertofftime = 500, \
                                                                    insertontime = 500, insertwidth=0.5, cursor = "arrow",insertbackground = "white")
B1 = tk.Button(frame,activebackground = "black", activeforeground="#fff",command = OnButton1Pressed, \
                                                                    bg = "#f09",text = "run SQLite", fg = "black")
B2 = tk.Button(frame,activebackground = "gray", activeforeground="#fff",command = OnButton2Pressed, \
                                                                    bg = "white",text = "Αναζήτηση", fg = "black")
checkbutton = tk.Checkbutton(frame, text="Near me")




# Create a Label widget
label = tk.Label(frame, text="Τι ψάχνεις;")

# Create a Combobox widget
combobox = tk.ttk.Combobox(frame,state = 'readonly')

labelFilter = tk.Label(frame, text="Filter by")
comboboxFilter = tk.ttk.Combobox(frame,state = 'disabled')

labelLoc = tk.Label(frame, text="Πού Είσαι?")
comboboxLoc = tk.ttk.Combobox(frame,state = 'readonly')


# Add some options to the Combobox
combobox["values"] = ["Τουριστικοί Προορισμοί", "Εστιατόρια", "Διαμονή", "Δραστηριότητες", "Ξεναγήσεις"]
comboboxFilter["values"] = ["Τοποθεσία", "Βαθμολογία", "Τιμή"]
comboboxLoc["values"] = ['Βαλσαμάτα', 'Γριζάτα', 'Ζόλα', 'Διλινάτα', 'Αγία Ειρήνη', 'Καμιναράτα',\
    'Μιτικάτα','Μακρυώτικα', 'Τζανάτα','Φαρακλάτα', 'Πλάκα','Άδαμας','Περιστέρι'\
        ,'Χαλάνδρι','Κηφισιά','Γλυφάδα','Πειραιάς','Αγυιά','Κέντρο','Φάληρο','Φώκι']

OutputBox.config(xscrollcommand=scrollbar2.set)
OutputBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=OutputBox.yview)

T.grid(row =0, column = 0, sticky = 'nsew')
OutputBox.grid(row=0, column=1,sticky="nsew")
frame.grid(row =1, column = 0,columnspan=2, sticky = 'nsew')
scrollbar.grid(row=0, column=2, sticky="nsew")
scrollbar2.grid(row=0, column=1,sticky="wse")
B1.grid(row=1, column=3, sticky="nsew")
B2.grid(row=1, column=2, sticky="nsew")
checkbutton.grid(row=1, column=4, sticky="nsew")
label.grid(row =0, column = 0)
combobox.grid(row =1, column = 0)
labelFilter.grid(row =0, column = 1)
comboboxFilter.grid(row =1, column = 1)
labelLoc.grid(row =0, column = 5)
comboboxLoc.grid(row =1, column = 5)


root.title("Travel guide database")


B1.bind("<Enter>", lambda e: B1.config( bg="#f00"))
B1.bind("<Leave>", lambda e: B1.config( bg="#f09"))

root.bind('<Escape>', lambda e: exitP())

B2.bind("<Enter>", lambda e: B2.config(bg="#bbb"))
B2.bind("<Leave>", lambda e: B2.config( bg="white"))
change_icon("AppIcon.png", root)


combobox.bind("<<ComboboxSelected>>", combobox_changed)

w = 1500 # Width 
h = 700 # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.mainloop()

