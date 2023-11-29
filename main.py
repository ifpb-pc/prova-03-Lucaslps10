def q1(idades):
    lista_cidades = []
    for chave in idades:
        if idades[chave] > 100:
            lista_cidades.append(chave)
    return lista_cidades

def q2(lista1, lista2):
    lista_soma = lista1 + lista2
    soma = 0
    lista_positivos = []

    for num in lista_soma:
    
        if num > 0:
            soma += num
            lista_positivos.append(num)
    lista_ordenada = sorted(lista_positivos)
    return soma, lista_ordenada


def q3(valores):
    lista = []

    while True:
        valor = int(input("Digite um número:"))
        if valor == 0:
            break
        lista.append(valor)
    return lista

def ler_valores(lista):
    lista_pares = []
    lista_impares = []
    for num in lista:
        if num%2 == 0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
    return lista_pares, lista_impares


def ler_03_alturas(valores):
    alturas = []
    contador = 0
    while True:
        contador += 1
        altura = float(input("Digite sua altura:"))
        alturas.append(f'{altura:.2f}')
        if contador == 3:
            break
    return alturas

def organizar_alturas(alturas):
    ordem_joaquina = []
    alturas[0], alturas[1], alturas[2] = alturas[1], alturas[2], alturas[0]
    for i in alturas:
        ordem_joaquina.append(i)
    return ordem_joaquina

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()


