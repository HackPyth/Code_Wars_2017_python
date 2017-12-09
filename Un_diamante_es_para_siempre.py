# -*- coding: utf-8 -*-

ancho_input = raw_input("Ancho del diamante(1-5): ")

if ancho_input == "1":
    print("  x  ")
elif ancho_input == "2":
    print("  xx ")
elif ancho_input == "3":
    print("  x  ")
    print(" xxx ")
    print("  x  ")
elif ancho_input == "4":
    print("  xx   ")
    print(" xxxx  ")
    print("  xx   ")
elif ancho_input == "5":
    print("   x   ")
    print("  xxx  ")
    print(" xxxxx ")
    print("  xxx  ")
    print("   x   ")
else:
    print("ERR_CODE=100")
