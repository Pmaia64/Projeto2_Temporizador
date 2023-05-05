# Este projeto trata da criação de um temporizador
#Contagem regressiva de tempo para uma dada atividade

import time

tarefa = input('Digite o nome da tarefa: ')
tempo = input('Digite o tempo em Segundos: ')
    
if tempo.isdigit():
    tempo = int(tempo)
else:
    print('Entrada inválida, digite o tempo em segundos')
    quit

while tempo != 0:
    minutes, seconds = divmod(tempo, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    tempo -= 1

print('TEMPO ESGOTADO!!!')



