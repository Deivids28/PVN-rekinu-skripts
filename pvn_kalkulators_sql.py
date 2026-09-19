import sqlite3
connection_obj = sqlite3.connect('Rekini.db')
cursor_obj = connection_obj.cursor()
table_creation_query = """
    CREATE TABLE IF NOT EXISTS Rekini (
        kategorija VARCHAR(255) NOT NULL,
        ievade REAL NOT NULL);
"""

cursor_obj.execute(table_creation_query)
print("Table is Ready")
rekini=[]
summas=[]
Dati = '''SELECT * FROM Rekini'''

cursor_obj.execute(Dati)
output = cursor_obj.fetchall()
for row in output:
  rekini.append([row[0],row[1]])
  summas.append(row[1])

while True:
    ievade=(input("ievadi summu: (quit to exit)"))
    if ievade=="quit":
        break
    ievade= float(ievade)
    kategorija= input("Ievadi katgoriju: ")
    pvn = ievade / 121 * 21
    Kopeja_summa = ievade
    rekini.append([Kopeja_summa, kategorija])
    summas.append(Kopeja_summa)
    cursor_obj.execute("INSERT INTO Rekini(kategorija, ievade) VALUES (?,?)",(kategorija, Kopeja_summa))
    print("Summa ar pvn:", ievade,"EUR")
    print("Pvn no summas ir: ", pvn, "EUR") 
    print("Summa bez pvn: ", ievade - pvn,"EUR")

connection_obj.commit()
print("Rekini kopa:",len(rekini))
print("kopeja summa rekinos", sum(summas))     


connection_obj.close()