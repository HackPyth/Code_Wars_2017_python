# -*- coding: utf-8 -*-

Primer_numero = input("Primer numero: ")
Operando = raw_input("Operando(+, -, *, / y **): ")
Segundo_numero = input("Segundo numero: ")

if Operando == "+":
    print("Resultado: " + str(Primer_numero + Segundo_numero))
elif Operando == "-":
    print("Resultado: " + str(Primer_numero - Segundo_numero))
elif Operando == "*":
    print("Resultado: " + str(Primer_numero * Segundo_numero))
elif Operando == "/":
    if Segundo_numero == 0:
        print("Error. División por 0!!")
    else:
        print("Resultado: " + str(Primer_numero / Segundo_numero))
elif Operando == "**":
    print("Resultado: " + str(Primer_numero ** Segundo_numero))
else:
    print("Ningun numero.")
