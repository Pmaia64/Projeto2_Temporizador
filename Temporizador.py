# Este projeto trata da criação de um temporizador
#Contagem regressiva de tempo para uma dada atividade

import time

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        t = str(input(msg))
        if t.isnumeric():
            valor = int(t)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

t = leiaInt('Digite o tempo em segundos: ')

while t != 0:
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

print('\033[0;31mTEMPO ESGOTADO!!!\033[m')


