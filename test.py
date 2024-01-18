from main import getLanguage
from time import time
wholeTime = time()


english = []
polish = []
with open("./data/polish.txt", encoding="UTF-8") as f:
    polish = f.readlines()

with open("./data/english.txt", encoding="UTF-8") as f:
    english = f.readlines()
print(f"Read take {int((time()-wholeTime)*10000)/10000}s")
testy = {True: 0, False: 0}
dlugosc = len(polish)+len(english)
with open("./data/badpolish.txt", encoding="UTF-8", mode="w") as f:
    for zdanie in polish:
        lang, t = getLanguage(zdanie)
        testy[lang=="polski"] += 1
        if(lang!="polski"):
            f.write(zdanie)
        tekst = f"\r[{testy[True]+testy[False]}/{dlugosc}] "

        tekst += str(lang=="polski") + " "

        tekst += f"polish {t[0]} english: {t[1]}"

        #tekst += str(t)
        print(tekst+"                       ", end="")
with open("./data/badenglish.txt", encoding="UTF-8", mode="w") as f:
    for zdanie in english:
        lang, t = getLanguage(zdanie)
        testy[lang=="angielski"] += 1
        if(lang!="angielski"):
            f.write(zdanie)
        tekst = f"\r[{testy[True]+testy[False]}/{dlugosc}] "

        tekst += str(lang=="angielski") + " "

        tekst += f"polish {t[0]} english: {t[1]}"

        #tekst += str(t)
        print(tekst+"                       ", end="")

print(f"\n\n{testy[True]}/{testy[True]+testy[False]} = {int((testy[True]/(testy[True]+testy[False]))*10000)/100}%\nMaked in {int((time()-wholeTime)*100)/100}s")



