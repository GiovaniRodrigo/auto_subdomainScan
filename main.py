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
        # print("Alvo: https://www." + subdominios[i])
        try: 
            consulta = requests.get('https://' + str(arg))
            if consulta.status_code == 200:
                print("\033[93m" + "Status code: ", consulta.status_code, arg)
            else:
                print("\033[34m" + "Status code: ", consulta.status_code, arg)
                
            urls_code.append(arg + ": " + str(consulta.status_code))
            print("\n")
        except requests.exceptions.RequestException as e:
            print("\033[31m" + "Erro ao consultar URL: " + arg)
            print(e)
            print("\n")


    for url_code in urls_code:
        print(url_code)
