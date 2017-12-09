 # -*- coding: utf-8 -*-

creditos_de_trabajo = 10 #10 creditos
creditos_extra_trabajo = 20 #20 creditos

hora_semanal = 40 #40 horas

horas_normales = input("Horas semanales: ")
horas_extras = input("Horas semanales extras: ")

if horas_normales >= hora_semanal:
    print("Nómina semanal normal: " + str(creditos_de_trabajo*horas_normales))
    print("Nómina semanal extra: " + str(creditos_extra_trabajo*horas_extras))
    print("Total: " + str((creditos_extra_trabajo*horas_extras)+(creditos_de_trabajo*horas_normales)))
elif(horas_normales < hora_semanal):
    print("Ha tebajado menos de: " + str(hora_semanal) + ", lo siento.")
