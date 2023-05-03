# Este projeto trata-se da criação de um temporizador
#Contagem regressiva de tempo para uma dada atividade

import time

tarefa = input('Digite o nome da tarefa: ')
t = input('Digite o tempo em Segundos: ')
if t.isdigit():
    t = int(t)
else:
    print('Entrada inválida, digite o tempo em segundos')
    quit()

while t != 0:
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

print('TEMPO ESGOTADO!!!')



