# -*- coding: utf-8 -*-

'''

    J -> Jabba
    L -> Luke
    S -> Uno de los gamorreanos de Jabba
    (espacio) -> baldosa del suelo

'''

Posiciones = raw_input()

Luke = "L"
Jabba = "J"
gamorreanos = "s"
espacio = " "

Lukes = Luke * 2
Jabbas = Jabba * 2
JabbasLuke = Jabba + espacio + gamorreanos + espacio +Luke
LukesJabba = Luke + espacio + gamorreanos + espacio + Jabba
Jabba_Luke = Jabba + espacio + Luke
Luke_Jabba = Luke + espacio + Jabba
Luke_Luke = Luke + espacio + Luke
Jabba_Jabba = Jabba + espacio + Jabba

if Posiciones == "LJ" or Posiciones == "JL":
    print("Jabba is dead")
elif Posiciones == "J":
    print("Jabba can sleep")
elif Posiciones is "L":
    print("Jabba is on a trip")
elif Posiciones == Lukes or Posiciones == Jabbas or Posiciones == Luke_Luke or Posiciones == Jabba_Jabba:
    print("Wrong palace")
elif Posiciones == JabbasLuke or Posiciones == LukesJabba:
    print("Jabba is safe for now")
elif Posiciones == Jabba_Luke or Posiciones == Luke_Jabba:
    print("Jabba is at risk")
else:
    print("Wrong palace")
