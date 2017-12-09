# -*- coding: utf-8 -*-

'''

    targetH = Altura de la ventana principal
    targetW = Ancho de la ventana principal
    popupH = Altura del popup
    popupW = Ancho del popup
    popupVA = Alineamiento vertical del popup
        T = Top -> (popupH)
        C = Center  -> (targetH-popupH)/2
        B = Bottom  -> (-1*popupH)
    popupHA = Alineamiento horizontal del popup
        L = Left    -> (-targetW+popupW)
        C = Center  -> (targetW-popupW)/2
        R = Right   -> (targeW+popupW)

'''

targetH = input("Altura de la ventana principal: ")
targetW = input("Ancho de la ventana principal: ")
popupH = input("Altura de la segunda ventana: ")
popupW = input("Ancho de la segunda ventana: ")
popupVA = raw_input("Alineamiento vertical de la segunda ventana(T,C,B): ")
popupHA = raw_input("Alineamiento horizontal de la segunda ventana(L,C,R): ")

T = (popupH)
B = (-1*popupH)

Ca = (float(targetH-popupH)/2)
Cb = (float(targetW-popupW)/2)

L = (-targetW+popupW)
R = (targetW+popupW)

if popupVA == "B" and popupHA == "L":
    popupX = L
    popupY = B
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "B" and popupHA == "C":
    popupX = Cb
    popupY = B
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "B" and popupHA == "R":
    popupX = R
    popupY = B
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "C" and popupHA == "L":
    popupX = L
    popupY = Ca
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "C" and popupHA == "C":
    popupX = Cb
    popupY = Ca
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "C" and popupHA == "R":
    popupX = R
    popupY = Ca
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "T" and popupHA == "L":
    popupX = L
    popupY = T
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "T" and popupHA == "C":
    popupX = Cb
    popupY = T
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
elif popupVA == "T" and popupHA == "R":
    popupX = R
    popupY = T
    print("\ntargetH="+str(targetH))
    print("targetW="+str(targetW))
    print("popupH="+str(popupH))
    print("popupW="+str(popupW))
    print("popupVA="+str(popupVA))
    print("popupHA="+str(popupHA))
    print("popupX="+str(popupX))
    print("popupY="+str(popupY))
else:
    print("ERR_CODE=100")
