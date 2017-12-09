# -*- coding: utf-8 -*-

frase = raw_input("Frase encriptada: ")

'''

    a -> e
    e -> i
    i -> o
    o -> u
    u -> a

'''

diccionario = {'a':'e', 'e':'i' , 'i':'o', 'o':'u', 'u':'a'}

frase_transformada = ''
for i in frase:
	if i in diccionario.keys():
		frase_transformada += diccionario[i]
	else:
		frase_transformada += i
print("Frase desencriptada: " + frase_transformada)
