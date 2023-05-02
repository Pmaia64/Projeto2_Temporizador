# Usando o módulo time e a função sleep()para criar
# un cronômetro de contagem regressiva em Python.

import time

def countdown(num_of_secs):
    while num_of_secs:
        m,s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1
    print('tempo finalizado. ')
inp = input('digite o tempo da atividade: ')
countdown(inp)

