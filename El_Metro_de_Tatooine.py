# -*- coding: utf-8 -*-

import random

monedas_uno = random.randrange(1,11)
monedas_dos = random.randrange(1,6)
monedas_cero_cincuenta = random.randrange(1,16)

print("--Bienvenido-Ciudadano-al-metro-de-TATOOINE!--")
print("----------------------------------------------")
print("----------------¿Que-Via-desea?---------------")
print("--1.-Via 1------------------------------------")
print("--2.-Via 2------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")
print("------:=)----------(o_>_o)-----------(=:------")

billete_escogido = raw_input("Escoga una Via(Ponga el numero): ")

if billete_escogido == "1":

    print("Creditos Maquina de 0.50: "+str(monedas_cero_cincuenta))
    print("Creditos Maquina de 1: "+str(monedas_uno))
    print("Creditos Maquina de 2: "+str(monedas_dos))

    dinero_billete = random.randrange(5,10)
    print("\nLa Via escogida cuesta: " +str(dinero_billete)+" creditos")
    monedas_insertadas = input("Inserte sus creditos: ")


    if monedas_insertadas >= dinero_billete:

        cambio = monedas_insertadas - dinero_billete

        if monedas_dos > monedas_insertadas:

            monedas_dos_utilizadas = (monedas_dos)*2 - monedas_insertadas

            print("-----Creditos-de-la-maquina--------------------")
            print("---------Creditos-de-1:-"+str(monedas_uno)+"----------------------")
            print("---------Creditos-de-2:-"+str(monedas_dos_utilizadas)+"----------------------")
            print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta)+"--------------------")
            print("----------------------------------------------")
            print("----------------------------------------------")
            print("-----------------Gracias-por-su-compra--------")
            print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")


        elif monedas_uno > monedas_insertadas and monedas_uno > monedas_insertadas:

            monedas_uno_utilizadas = monedas_uno - monedas_insertadas

            print("-----Creditos-de-la-maquina--------------------")
            print("---------Creditos-de-1:-"+str(monedas_uno_utilizadas)+"----------------------")
            print("---------Creditos-de-2:-"+str(monedas_dos_)+"----------------------")
            print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta)+"--------------------")
            print("----------------------------------------------")
            print("----------------------------------------------")
            print("-----------------Gracias-por-su-compra--------")
            print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")

        elif monedas_cero_cincuenta > monedas_insertadas and monedas_cero_cincuenta > monedas_dos and monedas_cero_cincuenta > monedas_uno:

            monedas_cero_cincuenta_utilizadas = 0.5*(monedas_cero_cincuenta) - monedas_insertadas

            print("-----Creditos-de-la-maquina--------------------")
            print("---------Creditos-de-1:-"+str(monedas_uno)+"----------------------")
            print("---------Creditos-de-2:-"+str(monedas_dos)+"----------------------")
            print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta_utilizadas)+"------------------")
            print("----------------------------------------------")
            print("----------------------------------------------")
            print("-----------------Gracias-por-su-compra--------")
            print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")
        else:
            print("----------No-hay-cambio-en-la-maquina---------")

    else:
        print("-----No-ha-insertado-los-creditos-necesarios-----")
elif billete_escogido == "2":

        print("Creditos Maquina de 0.50: "+str(monedas_cero_cincuenta))
        print("Creditos Maquina de 1: "+str(monedas_uno))
        print("Creditos Maquina de 2: "+str(monedas_dos))

        dinero_billete = random.randrange(5,15)
        print("\nLa Via escogida cuesta: " +str(dinero_billete)+" creditos")
        monedas_insertadas = input("Inserte sus creditos: ")


        if monedas_insertadas >= dinero_billete:

            cambio = monedas_insertadas - dinero_billete

            if monedas_dos > monedas_insertadas:

                monedas_dos_utilizadas = (monedas_dos)*2 - monedas_insertadas

                print("-----Creditos-de-la-maquina--------------------")
                print("---------Creditos-de-1:-"+str(monedas_uno)+"----------------------")
                print("---------Creditos-de-2:-"+str(monedas_dos_utilizadas)+"----------------------")
                print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta)+"--------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("-----------------Gracias-por-su-compra--------")
                print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")


            elif monedas_uno > monedas_insertadas and monedas_uno > monedas_insertadas:

                monedas_uno_utilizadas = monedas_uno - monedas_insertadas

                print("-----Creditos-de-la-maquina--------------------")
                print("---------Creditos-de-1:-"+str(monedas_uno_utilizadas)+"----------------------")
                print("---------Creditos-de-2:-"+str(monedas_dos)+"----------------------")
                print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta)+"--------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("-----------------Gracias-por-su-compra--------")
                print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")

            elif monedas_cero_cincuenta > monedas_insertadas and monedas_cero_cincuenta > monedas_dos and monedas_cero_cincuenta > monedas_uno:

                monedas_cero_cincuenta_utilizadas = 0.5*(monedas_cero_cincuenta) - monedas_insertadas

                print("-----Creditos-de-la-maquina--------------------")
                print("---------Creditos-de-1:-"+str(monedas_uno)+"----------------------")
                print("---------Creditos-de-2:-"+str(monedas_dos)+"----------------------")
                print("---------Creditos-de-0.5:-"+str(monedas_cero_cincuenta_utilizadas)+"-------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("-----------------Gracias-por-su-compra--------")
                print("--------Aqui-tine-su-cambio:"+str(cambio)+"-credito/s-------")
            else:
                print("----------No-hay-cambio-en-la-maquina---------")

        else:
            print("---No-ha-insertado-los-creditos-necesarios----")
else:
    print("--------------Esa-Via-no-existe---------------")
