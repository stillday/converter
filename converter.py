# -*- coding: utf-8 -*-
print "Hallo ich bin ein Converter, von Kilometer auf Meilen"


while True:
    try:
        km = int(raw_input("Bitte gib die Kilometer an, die umgerechnet werden sollen: "))
        miles = km * 0.621371

        print str(km) + " km sind " + str(miles) + " Meilen"

    except ValueError:
        print "Gib bitte eine Zahl ein"

    answer = "ja"
    ask = raw_input("Moechtest du noch weitere Kilometer umrechnen? ja oder nein! ")

    if  ask != answer:
        print "Danke fürs verwenden und auf wiedersehen"
        break