#Biblioteca para modificar, utilizar e estabelecer conexões de internet
import socket

'''
Todas as variáveis importantes para o sistema, 
sendo o array de todas as portas abertas,
o limite padrão do sistema,
o limite do scan total do sistema
e o limite utilizado para calcular no sistema.

'''
all_open = []
default_limit = 10000
total_limit = 65535
limit = 0

#Utilizado para obter o endereço ip desejado
target = input('Type your ip adress: ')

'''
Utilizei um while para rodar apenas esta parte até as condições
necessárias serem concluidas, sendo elas escolher especificamente
escolher entre a opção A (que é o scan comum) e a opção B (que é 
o scan total), caso contrário ele volta para o começo do looping.
'''
while True:
    actual_limit = input('\nType what type of scan you prefer between:\nA) Normal Scan\nB) Full Scan\n')

    match actual_limit:
        case 'A':
            limit = default_limit
            break
        case 'B':
            limit = total_limit
            break
        case _:
            print('\nTry again!!!')
            actual_limit = input('\nType what type of scan you prefer between:\nA) Normal Scan\nB) Full Scan\n')

'''
Aqui onde a mágica acontece, utilizo um loop for para
passar por todas as portas até o limite escolhido, assim
verificando se estão abertas e no final do scan mostrando
todas as portas que estão abertas.
'''
for port in range(1, limit):
    print(f'{int((port / limit) * 100)}%', end='\r')

    client = socket.socket()
    client.settimeout(0.05)

    if client.connect_ex((target, port)) == 0:
        all_open.append(port)
print(f'Thats all open ports: {all_open}')