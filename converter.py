print "Hallo ich bin ein Converter, von Kilometer auf Milen"


while True:
    try:
        km = int(raw_input("Bitte gib die Kilometer an, die umgerechnet werden sollen: "))
        miles = km * 0.621371

        print str(km) + " km sind " + str(miles) + " Milen"

    except ValueError:
        print "Gib bitte eine Zahl ein"

    answer = "ja"
    ask = raw_input("Moechtest du noch weitere Kilometer umrechnen? ja oder nein! ")

    if  ask != answer:
        print "Danke fuers verwenden und aufwiedersehen"
        break