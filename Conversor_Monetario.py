 # -*- coding: utf-8 -*-

cambio = raw_input("Cambio de EUR, GBP y USD a Créditos: ")

if cambio == "EUR":
    Dinero = input("Dinero a cambiar: ")
    print("Sus créditos son: " + str(Dinero*1.08))
elif cambio == "GBP":
    Dinero = input("Dinero a cambiar: ")
    print("Sus créditos son: " + str(Dinero*1.56))
elif cambio == "USD":
    Dinero = input("Dinero a cambiar: ")
    print("Sus créditos son: " + str(Dinero*0.99))
