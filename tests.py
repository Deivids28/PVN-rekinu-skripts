import csv
rekini=[]
summas=[]
with open("rekini.csv", "r",) as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        if not line:
            continue
        rekini.append([float(line[0]),line[1]])
        summas.append(float(line[0]))
        print ('line[{}] = {}'.format(i, line))

file = open("rekini.csv","a",newline='')
writer =csv.writer(file)


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
    writer.writerow([ievade, kategorija])
    print("Summa ar pvn:", ievade,"EUR")
    print("Pvn no summas ir: ", pvn, "EUR") 
    print("Summa bez pvn: ", ievade - pvn,"EUR")

print("Rekini kopa:",len(rekini))
print("kopeja summa rekinos", sum(summas))    
file.close()