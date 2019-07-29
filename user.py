import requests, json

url = "http://127.0.0.1:3000/info/"

while True:
    
    entrada = input("\nInforme o id que deseja consultar: ")

    if(entrada == '-1'):
        break

    req = requests.get(url + entrada)

    js = json.loads(req.content.decode())

    nome = js[-1]['nome']

    del js[-1]

    tamanho = len(js)

    print("\nUsuário de nome " + nome + '\n')

    print("Valores do Sensor de Temperatura: \n")

    for i in js:
        if(i['type'] == 'temperatura'):
            print("Temperatura: " + str(i['value']) + 'C, Momento: ' + i['time'])

    print("\nValores do Sensor de Umidade: \n")

    for i in js:
        if(i['type'] == 'temperatura'):
            print("Porcentagem de Umidade: " + str(i['value']) + '%, Momento: ' + i['time'])



