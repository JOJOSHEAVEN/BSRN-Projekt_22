def pruefen(schiff, besetzt):
    schiff.sort()   # .sort() sortiert alle Elemente in der Liste
    for i in range(len(schiff)):
        zahl = schiff[i]

        if zahl in besetzt:
            schiff = [-1]   # [-1] bedeutet index von hinten
            break

        elif zahl < 0 or zahl > 99:
            schiff = [-1]
            break

    return schiff


def get_schiff(laenge, besetzt):
    ok = True
    while ok:
        schiff = []

        # der Spieler verlegt hier seine Schiffe
        print("Schiff mit länge", laenge)
        for i in range(laenge):
            schiff_num = input("Bitte geben Sie die Koordinaten ein. Erst die Zeile, dann die Spalte: ")
            schiff.append(int(schiff_num))

        # Überpüfung der Schiffe
        schiff = pruefen(schiff, besetzt)

        # Die Felder werden besetzt
        if schiff[0] != -1:
            besetzt = besetzt + schiff
            break

        else:
            print("Hier befindet sich schon ein anderes Schiff")

    return schiff, besetzt


def schiffe_erstellen(besetzt, boete):
    schiffe_list = []

    for boot in boete:
        ship, besetzt = get_schiff(boot, besetzt)
        schiffe_list.append(ship)

    return schiffe_list, besetzt


def zeig_spielfeld_schiffe(besetzt):
    print("          Schiffe Versenken    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    platz = 0
    for x in range(10):
        zeile = ""
        for y in range(10):
            zeichen = " _ "
            if platz in besetzt:
                zeichen = " o "
            zeile = zeile + zeichen
            platz = platz + 1

        print(x, " ", zeile)


def zeig_spielfeld(treffer, verfehlt, versenkt):
    print("          Schiffe Versenken    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    platz = 0
    for x in range(10):
        zeile = ""
        for y in range(10):
            zeichen = " _ "
            if platz in treffer:
                zeichen = " o "
            elif platz in verfehlt:
                zeichen = " x "
            elif platz in versenkt:
                zeichen = " O "
            zeile = zeile + zeichen
            platz = platz + 1

        print(x, " ", zeile)


def check_shot(schuss, schiffe, treffer, verfehlt, versenkt):
    missed = 0
    for i in range(len(schiffe)):
        if schuss in schiffe[i]:
            schiffe[i].remove(schuss)
            if len(schiffe[i]) > 0:
                treffer.append(schuss)
                missed = 1
            else:
                versenkt.append(schuss)
                missed = 2
    if missed == 0:
        verfehlt.append(schuss)

    return schiffe, treffer, verfehlt, versenkt, missed


def get_schuss(versuch):
    ok = "n"
    while ok == "n":
        try:
            schuss = input("Geben Sie die Koordinaten ein")
            schuss = int(schuss)
            if schuss < 0 or schuss > 99:
                print("Die Koordinaten befinden sich nicht auf dem Spielfeld. Versuchen Sie nochmal")
            elif schuss in versuch:
                print("Falsche Koordinaten. Sie wurden schon eingegeben. Versuchen Sie nochmal")
            else:
                ok = "y"
                break
        except:
            print("Geben Sie bitte nur die Koordinaten ein, die existieren")

    return schuss

# überprüft, ob es noch übrige Schiffe gibt
def pruefen_ob_leer(alle_schiffe):
    return all([not elem for elem in alle_schiffe])


# vor dem Spielbeginn
treffer1 = []
verfehlt1 = []
versenkt1 = []
versuch1 = []
missed1 = 0
besetzt1 = []

treffer2 = []
verfehlt2 = []
versenkt2 = []
versuch2 = []
missed2 = 0
besetzt2 = []

# Anzahl und größe der Schiffe
schiffe = [4, 3, 2, 1]

# Spielfeld für Spieler 1
schiffe1, besetzt1 = schiffe_erstellen(besetzt1, schiffe)
zeig_spielfeld_schiffe(besetzt1)

# Spielfeld für Spieler 2
schiffe2, besetzt2 = schiffe_erstellen(besetzt2, schiffe)
zeig_spielfeld_schiffe(besetzt2)

# Wenn man z.B.: bis Runde 71 spielt, beendet das Programm alles
for i in range(70):

    # spieler1 schießt
    versuch1 = treffer1 + verfehlt1 + versenkt1
    schuss1 = get_schuss(versuch1)
    schiffe1, treffer1, verfehlt1, versenkt1, missed1 = check_shot(schuss1, schiffe1, treffer1, verfehlt1, versenkt1)
    zeig_spielfeld(treffer1, verfehlt1, versenkt1)

    # überprüft, ob es noch übrige Schiffe von Spieler 1 gibt
    if pruefen_ob_leer(schiffe1):
        print("VICTORY - Spieler 2 gewinnt")
        break

    # spieler2 schießt
    versuch2 = treffer2 + verfehlt2 + versenkt2
    schuss2 = get_schuss(versuch2)
    schiffe2, treffer2, verfehlt2, versenkt2, missed2 = check_shot(schuss2, schiffe2, treffer2, verfehlt2, versenkt2)
    zeig_spielfeld(treffer2, verfehlt2, versenkt2)

    # überprüft, ob es noch übrige Schiffe von Spieler 2 gibt
    if pruefen_ob_leer(schiffe2):
        print("VICTORY - Spieler 1 gewinnt")
        break

