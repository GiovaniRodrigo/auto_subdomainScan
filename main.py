import requests
import sys
import subprocess

# Variáveis Globais
arguments = sys.argv
subdominios= []

# Consultar subdomínios
consultas = subprocess.Popen(["docker run 380c17451f17 -d " + arguments[1]], stdout=subprocess.PIPE, shell=True)
(out, err) = consultas.communicate()
subdominios = out.split()

#  remover tag "b'" dos subdominios
for i, subdominio in enumerate(subdominios):
    subdominios[i] = subdominio.decode('utf-8').replace("b'", "")

# Consultar resposta de URL 
if len(subdominios) == 0:
    print("URLs não encontrados")
else:
    urls_code = []
    for i, arg in enumerate(subdominios):
        print("Alvo: " + subdominios[i])
        try: 
            consulta = requests.get('https://' + str(arg))
            print("Consultando: https://www" + arg, "\n")
            urls_code.append(arg + ": " + str(consulta.status_code))
            print("\n")
        except requests.exceptions.RequestException as e:
            print('Erro ao consultar URL: ', e)

    for url_code in urls_code:
        print(url_code)
