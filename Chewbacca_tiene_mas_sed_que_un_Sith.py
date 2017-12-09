# -*- coding: utf-8 -*-
    #beep -> GGWWWRGHH
    #boop -> RAWRGWAWGGR
    #chuit -> RWGWGWARAHHHHWWRGGWRWRW
    #tui -> WWWWWWWGGGGHHHRRRRW
    #pupi -> GGGWARRRHHWWWW
    #pipu -> AAARARRRGWWWH

frase_chewaka = raw_input("Frase en Chewaka: ")

'''                         PRIMERA OPCION:
traducciones = {'GGWWWRGHH':'beep', 'RAWRGWAWGGR':'boop', 'RWGWGWARAHHHHWWRGGWRWRW':'chuit', 'WWWWWWWGGGGHHHRRRRW':'tui', 'GGGWARRRHHWWWW':'pupi', 'AAARARRRGWWWH':'pipu',
                        'GGWWWRGHH GGWWWRGHH':'beep beep' ,'GGWWWRGHH RAWRGWAWGGR':'beep boop', 'GGWWWRGHH RWGWGWARAHHHHWWRGGWRWRW':'beep chuit', 'GGWWWRGHH WWWWWWWGGGGHHHRRRRW':'beep tui', 'GGWWWRGHH GGGWARRRHHWWWW':'beep pupi',
                        'GGWWWRGHH AAARARRRGWWWH':'beep pipu', 'RAWRGWAWGGR GGWWWRGHH':'boop beep', 'RAWRGWAWGGR RAWRGWAWGGR':'boop boop', 'RAWRGWAWGGR RWGWGWARAHHHHWWRGGWRWRW':'boop chuit',
                        'RAWRGWAWGGR WWWWWWWGGGGHHHRRRRW':'boop tui', 'RAWRGWAWGGR GGGWARRRHHWWWW':'boop pupi', 'RAWRGWAWGGR AAARARRRGWWWH':'boop pipu', 'RWGWGWARAHHHHWWRGGWRWRW RWGWGWARAHHHHWWRGGWRWRW':'chuit chuit',
                        'RWGWGWARAHHHHWWRGGWRWRW GGWWWRGHH':'chuit beep', 'RWGWGWARAHHHHWWRGGWRWRW RAWRGWAWGGR':'chuit boop', 'RWGWGWARAHHHHWWRGGWRWRW  WWWWWWWGGGGHHHRRRRW':'chuit tui', 'RWGWGWARAHHHHWWRGGWRWRW GGGWARRRHHWWWW':'chuit pupi',
                        'RWGWGWARAHHHHWWRGGWRWRW AAARARRRGWWWH': 'chuit pipu', 'WWWWWWWGGGGHHHRRRRW  WWWWWWWGGGGHHHRRRRW': 'tui tui', 'WWWWWWWGGGGHHHRRRRW GGWWWRGHH':'tui beep', 'WWWWWWWGGGGHHHRRRRW RAWRGWAWGGR':'tui boop',
                        'WWWWWWWGGGGHHHRRRRW RWGWGWARAHHHHWWRGGWRWRW':'tui chuit', 'WWWWWWWGGGGHHHRRRRW GGGWARRRHHWWWW':'tui pupi', 'WWWWWWWGGGGHHHRRRRW AAARARRRGWWWH':'tui pipu', 'GGGWARRRHHWWWW GGGWARRRHHWWWW':'pupi pupi',
                        'GGGWARRRHHWWWW GGWWWRGHH':'pupi beep', 'GGGWARRRHHWWWW RAWRGWAWGGR':'pupi boop', 'GGGWARRRHHWWWW RWGWGWARAHHHHWWRGGWRWRW':'pupi chuit', 'GGGWARRRHHWWWW WWWWWWWGGGGHHHRRRRW':'pupi tui', 'GGGWARRRHHWWWW AAARARRRGWWWH':'pupi pipu',
                        'AAARARRRGWWWH AAARARRRGWWWH':'pipu pipu', 'AAARARRRGWWWH GGWWWRGHH':'pipu beep', 'AAARARRRGWWWH RAWRGWAWGGR':'pipu boop', 'AAARARRRGWWWH RWGWGWARAHHHHWWRGGWRWRW':'pipu chuit', 'AAARARRRGWWWH WWWWWWWGGGGHHHRRRRW':'pipu tui',
                        'AAARARRRGWWWH GGGWARRRHHWWWW':'pipu pupi'}
frase_robot = ''

if frase_chewaka in traducciones.keys():
    frase_robot += traducciones[frase_chewaka]
    print("Frase en Robot: " + frase_robot)
'''

#SEGUNDA OPCION

frase_robot = frase_chewaka.replace('GGWWWRGHH','beep').replace('RAWRGWAWGGR','boop').replace('RWGWGWARAHHHHWWRGGWRWRW','chuit').replace('WWWWWWWGGGGHHHRRRRW','tui').replace( 'GGGWARRRHHWWWW','pupi').replace('AAARARRRGWWWH','pipu')
print("Frase en Binario Vocalizado: " + frase_robot)
