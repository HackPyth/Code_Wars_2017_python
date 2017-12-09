'''



'''

numero_de_disparos_recibidos_de_la_torre = input("Numero de disparos recibidos por la torre: ")
numero_medio_de_disparos_al_intentar_llegar_al_objetivo = input("Numero de disparos al intentar llegar al objetivo: ")
disparos_al_hueco = input("Disparos al punto debil: ")


probabilidad_disparos_de_la_torre = 100/(numero_de_disparos_recibidos_de_la_torre) #de cada input disparos uno acierta, entonces, para porcentaje un 100% son x
probabilidad_medio_de_disparos_al_intentar_llegar_al_objetivo = 100/(numero_medio_de_disparos_al_intentar_llegar_al_objetivo)

print("\nprobabilidad_disparos_de_la_torre: " + str(probabilidad_disparos_de_la_torre) + "%")
print("probabilidad_medio_de_disparos_al_intentar_llegar_al_objetivo: " + str(probabilidad_medio_de_disparos_al_intentar_llegar_al_objetivo) + "%")

probabilidad_de_exito = (probabilidad_disparos_de_la_torre + probabilidad_medio_de_disparos_al_intentar_llegar_al_objetivo)/2

print("probabilidad_de_exito: " + str(probabilidad_de_exito) + "%")
