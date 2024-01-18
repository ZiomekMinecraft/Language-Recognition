# Program został zrobiony przez Pawła P.
# Psełdonim "MZ" discord "ziomekminecraft"
# Server discord "discord.gg/ziomcaft"

import operator

# original
# polishTable = {'a': 0.0891, 'b': 0.0147, 'i': 0.0821, 'o': 0.0775, 'e': 0.0766, 'z': 0.0564, 'n': 0.0552, 'r': 0.0469, 'w': 0.0465, 's': 0.0432, 't': 0.0398, 'c': 0.0395, 'y': 0.0375, 'k': 0.0351, 'd': 0.0325, 'p': 0.0313, 'm': 0.0279, 'u': 0.025, 'j': 0.0227, 'l': 0.021, 'ł': 0.0182, 'g': 0.0142, 'ę': 0.0111, 'h': 0.0108, 'ą': 0.0098, 'ó': 0.0085, 'ż': 0.0083, 'ś': 0.0066, 'ć': 0.004, 'f': 0.003, 'ń': 0.002, 'q': 0.0014, 'ź': 0.0005, 'v': 0.0004, 'x': 0.0002}
# dane znalezione na stronach z danymi głównie wikipedia
polishTable = {'a': 0.0837, 'b': 0.0193, 'i': 0.0883, 'o': 0.0753, 'e': 0.0868, 'z': 0.0533, 'n': 0.0569, 'r': 0.0415, 'w': 0.0411, 's': 0.0413, 't': 0.0385, 'c': 0.0389, 'y': 0.0403, 'k': 0.0301, 'd': 0.0335, 'p': 0.0287, 'm': 0.0281, 'u': 0.0206, 'j': 0.0228, 'l': 0.0224, 'ł': 0.0238, 'g': 0.0146, 'ę': 0.0113, 'h': 0.0125, 'ą': 0.0079, 'ó': 0.0079, 'ż': 0.0093, 'ś': 0.0072, 'ć': 0.006, 'f': 0.0026, 'ń': 0.0016, 'q': 0.0014, 'ź': 0.0008, 'v': 0.0004, 'x': 0.0002}

# original oryginalne wartości z zadania
# englishTable = {'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.02, 'h': 0.061, 'i': 0.07, 'j':0.002, 'k': 0.008, 'l': 0.04, 'm': 0.024, 'n': 0.067, 'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.06, 's': 0.063, 't': 0.091, 'u': 0.028, 'v': 0.028, 'w': 0.023, 'x': 0.001, 'y': 0.02, 'z': 0.001}
# dane znalezione na stronach z danymi głównie wikipedia
englishTable = {'a': 0.0849, 'b': 0.0207, 'c': 0.0453, 'd': 0.0338, 'e': 0.1116, 'f': 0.0181, 'g': 0.0247, 'h': 0.03, 'i': 0.0754, 'j':0.0019, 'k': 0.011, 'l': 0.0548, 'm': 0.0301, 'n': 0.0665, 'o': 0.0716, 'p': 0.0316, 'q': 0.0019, 'r': 0.0758, 's': 0.0573, 't': 0.0695, 'u': 0.0363, 'v': 0.01, 'w': 0.0128, 'x': 0.0029, 'y': 0.0177, 'z': 0.0027}

# Funkcja której zadaniem jest pozyskać ciąg liter w kolejności od największej do najmniejszej częstotliwości
def getFrequrency(table: dict[str, float]) -> str:
    # Linijka odpowidzialna za to aby posortować słownik względem wartości
    table = dict(sorted(table.items(), key=operator.itemgetter(1), reverse=True))
    # Następnie tworzymy zmienną w której będzie się znajdował ciąg 
    # znaków w kolejności od najczęśniej powtarzającej się do najrzadziej powtarzającej się
    t = ""
    # teraz iterujemy każdy klucz w słowniku i dodajemy go do napisu w zmiennej 't'
    for letter in table.keys():
        t += letter
    # Na koniec funkcji zwracamy ciąg znaków w kolejności od najczęstrzej do najrzadszej
    return t

# Pozyskujemy na start Częstotliwość obu języków
polishFrequrency = getFrequrency(polishTable)
englishFrequrency = getFrequrency(englishTable)

# Funkcja której zadaniem jest wygenerowanie jaką ilość punktów zebrał język.
# Tym mniej tym lepiej.
# Funkcja pobiera dwie zmienne gdzie 
# - x to ciąg znaków częstotliwości wpisanego zdania
# - y to ciąg znaków częstotliwości języka ( w tym tekscie znajdują się tylko litery występujące w zdaniu )
def getFirstPoint(x: str, y: str) -> int:
    # ustawiamy zmienną punktów które uzyskał język na 0
    points = 0
    # pętla for która powtarza się tyle razy jaki długi jest x
    for xn in range(len(x)):
        # do zmiennej xletter jest przypiywana litera znajdująca się pod danym numerem 
        xletter = x[xn]
        # do zmiennej gettedNumber przypisuje liczbę -1
        gettedNumber = -1
        # rozpoczynam pętlę for powtarzającą się tyle razy jaki długi jest y
        for yn in range(len(y)):
            # sprawdzam czy litera w napisie y pod indeksem yn jest równa literze xletter
            if(y[yn]==xletter):
                # ustawiam zmienną gettedNumber do absolutnej różnicy yn i xn
                gettedNumber = abs(yn - xn)
                # przerywam funkcję
                break
        # jeżeli danej litery nie było w napisie y zwracam -1 ( -1 informuje że to nie jest na pewno dany język )
        if gettedNumber == -1:
            return -1
        # jeżeli litera była w zbiorze dodaje wynik do zmiennej points
        else:
            points += gettedNumber
    # po skończeniu pętli zwracam liczbę punktów zdobytych przez dany język
    return points

# Główna funkcja logiczna programu
# funkcja odpowiedzialna za odgadnięcie języka
# w którym jest napisany podany tekst 
# który jest zapisany w argumęcie tekst
def getLanguage(tekst: str):
    # do zmiennej _t zapisuję kopie tekstu
    _t = tekst
    # do zmiennej tekst zapisuje pusty ciąg znaków
    tekst = ""
    # przy urzyciu pętli for literuje wszystkie litery znajdujące się w zmiennej _t
    for letter in _t:
        # jeżeli dana litera znajduje się w tabelach częstotliwości liter dla języka
        # polskiego lub angielskiego litera zostaje dodana do ciągu znaktów w zmiennej tekst
        if letter in polishTable.keys() or letter in englishTable.keys():
            tekst += letter
    # po skończonej pętli zmienną _t ustawiam na None
    _t = None
    # do zmiennej lenght przypisuje długość tekstu w zmiennej tekst
    lenght = len(tekst)
    # do zmiennej letters przypisuje pisty słownik
    letters = {}
    # literuję wszystkie litery w zmiennej tekst po zmienieniu ich w małe litery
    for letter in tekst.lower():
        # jeżeli w zmiennej letters już znajduje się litera z zmiennej letter dodaje do wartości z słownika 1
        # jeżeli w zmiennej letters nie znajduje się taka liter wtedy do niej przypisuje 1
        if(letter in letters.keys()):
            letters[letter] += 1
        else:
            letters[letter] = 1

    # literuję wszystkie litery w kluczu słownika i przypisuje do niej
    # dzielenie liczby znajdującej się w letters[letter] przez liczbę znajdującą się w zmiennej lenght
    for letter in letters.keys():
        letters[letter] = letters[letter] / lenght
    
    # ustawiam punkty języka polskiego i angielskiego na zero
    polishPoint = 0
    englishPoint = 0
    
    # do zmiennej frequrency przypisuję ciąg znaków z funkcji getFrequrency
    frequrency = getFrequrency(letters)

    # do zmiennej pf i ef ustawiam częstotliwość liter w danym języku języku
    pf = ''.join([ letter if letter in frequrency else '' for letter in polishFrequrency])
    ef = ''.join([ letter if letter in frequrency else '' for letter in englishFrequrency])

    # tekst służący do debugowania
    if(__debug__):
        print("[DEBUG] " + frequrency)
        print("[DEBUG] " + pf)
        print("[DEBUG] " + ef)

    # Krok pierwszy odgadnięcia języka

    # do zmiennej polish i english przypisuję zwróconą wartość z funkcji getFirstPoint
    polish = getFirstPoint(frequrency, pf)
    english = getFirstPoint(frequrency, ef)
    # tekst służący do debugowania
    if(__debug__):
        print("[DEBUG] " + f"polish: {polish}\n[DEBUG] english: {english}")

    # if służący do ustalenia który język otrzymuje punkt
    # jeżeli zmienna polish i english równe są -1 język polski otrzymuje punkt 
    if(polish == -1 and english == -1):
        englishPoint += 1
    # jeżeli zmienna polish jest większa niż zmienna english i
    # zmienna english nie jest równa -1
    # lub zmienna polish jest równa -1
    # wtedy język angielski otrzymuje punkt
    elif((english < polish and english != -1) or polish == -1):
        englishPoint += 1
    # w przeciwnym wypadku język polski otrzymuje punkt
    else:
        polishPoint += 1

    # Krok drugi do ustalenia języka
    # zmienne polish i english ustawimy na 0
    polish = 0
    english = 0
    # tworzymy pętle for literującą wszystkie wyrażenia w kluczach w zmiennej letters
    for letter in letters.keys():
        # do zmiennych polish i/lub english dodajemy absolutną różnicę częstotliwość z słownika letters z klucza 
        # w zmiennej letter i częstotliwość z słownika (polish/english)Table z klucza w zmiennej letter jeżeli
        # taka litera znajduje się w liście kluczy słownika, w przeciwnym razie zostaje dodana liczba 999
        # do zmiennej polish i/lub english
        polish += abs((letters[letter] - polishTable[letter]) if letter in polishTable.keys() else 999)
        english += abs((letters[letter] - englishTable[letter]) if letter in englishTable.keys() else 999)
    
    # jeżeli zmienna english jest mniejsza od zmiennej polish, angielski dostaje punkt
    # w przeciwnym razie polski dostaje punkt
    if english < polish:
        englishPoint += 1
    else:
        polishPoint += 1
    
    # Krok trzeci do ustalenia języka
    
    # zmienne polish i english ustawiamy na 0
    polish = 0
    english = 0

    # tworzę pętle for w której literuje wszystkie klucz w słowniku letters
    for letter in letters.keys():
        # do zmiennych polish i english dodaje kwadrat różnicy częstotliwości danej litery z zmienny letter w słowniku letters i słowniku (polish/english)Table
        # jeżeli litera z zmiennej letter nie znajduje sie w słowniku (polish/english)Table dodaje się do zmiennej 999
        polish += (letters[letter] - polishTable[letter])**2 if letter in polishTable else 999
        english += (letters[letter] - englishTable[letter])**2 if letter in englishTable else 999
    
    # zmienne polish i english ustawiamy na ich wartość podniesioną do potęgi 1/2 ( pierwiastek tej liczby )
    polish **= 1/2.0
    english **= 1/2.0
    
    # jeżeli zmienna english jest mniejsza bądz równa polish język angielski dostaje punkt 
    # w przeciwnym razie język polski otrzymuje punkt
    if english <= polish:
        englishPoint += 1
    else:
        polishPoint += 1

    # na koniec funkcji zostaje zwrócona nazwa języka który został stwierdzony jako prawidłowy oraz liczbę punktów otrzymanych przez języki
    return ("angielski" if englishPoint > polishPoint else "polski", (polishPoint, englishPoint), letters)

# główna funkcja która jest wykonywana na samym początku programu
def main():
    # print informujący kto zrobił program ;)
    print("Program zrobiony przez Paweł P. (MZ)")
    # print informacji o włączonym trybie debugowania
    if __debug__:
        print("[DEBUG] Tryb DEBUG jest włączony! Aby wyłączyć tryb debugowania proszę uruchomić program z parametrem -O lub -OO")
    # pozyskuje tekst do sprawdzenia języka
    tekst = input("Napisz swoje zdanie: ")
    t = None
    if __debug__:
        from time import time

        t = time()
    
    # wykonuje funkcję getLanguage i pozyskuję język w jakim został napisany tekst
    language, table, letters = getLanguage(tekst)

    # printuje jaki to jest język
    print(f"Język to {language}")
    print(f"częstotliwości liter:")
    for letter in dict(sorted(letters.items(), key=operator.itemgetter(1), reverse=True)):
        print(f" - {letter}: {int(letters[letter]*10000)/100 if letter in letters.keys() else 0}%")
    if __debug__:
        print(f"[DEBUG] polish: {table[0]}\n[DEBUG] english: {table[1]}\n[DEBUG] wykonano w {time()-t}s")



# jeżeli program jest odpalany jak główny plik wykonuje funkcję main
if(__name__=="__main__"):
    main()