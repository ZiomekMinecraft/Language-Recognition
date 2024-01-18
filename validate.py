badSintence = []
Sintence = []


with open("./data/badpolish.txt", 'r', encoding="UTF-8") as f:
    badSintence = f.readlines()
with open("./data/polish.txt", 'r', encoding="UTF-8") as f:
    Sintence = f.readlines()

for sintence in badSintence:
    while True:
        print(sintence)
        odp: str = input("Czy usunąć to? (T/n)")
        
        if odp == "T":
            Sintence.remove(sintence)
            break
        elif odp.lower() == "n":
            break

with open("./data/polish.txt", 'w', encoding="UTF-8") as f:
    f.writelines(Sintence)