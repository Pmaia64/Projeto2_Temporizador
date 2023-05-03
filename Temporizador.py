# Usando o módulo time e a função sleep()para criar
# un cronômetro de contagem regressiva em Python.

import time
tempo = input('Digite o tempo (em segundos): ')
if tempo.isdigit():
    tempo = int(tempo)
else:
    print('Entrada Inválida')
    quit()


while tempo != 0:
minutes, seconds = divmod(tempo, 60)
timer = 



