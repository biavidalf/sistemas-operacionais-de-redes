"""
    Arquivo p/ armazenar as funções e variáveis
    da atividade de cgi de SOR1.
"""


def comprimento(metros):
    feet = metros // .3048
    inches = metros / .3048 % 1 * 12
    return f'''{feet:.0f}'{inches:.0f}"'''


def distancia(km):
    miles = km/1.6
    return f'{miles}'


def peso(kg):
    pounds = kg/0.45
    return f'{pounds}lbs\n'


def sapato(fm, numerobr):
    feminino = {"32": "5", "33": "4 1/2", "34": "6", "35": "6 1/2",
                "36": "7 1/2", "37": "8 1/2", "38": "9", "39": "9 1/2",
                "40": "10", "41": "11"}

    masculin = {"36": "6", "37": "6 1/2", "38": "7", "39": "7 1/2",
                "40": "8 1/2", "41": "9 1/2", "42": "10", "43": "11",
                "44": "12", "45": "13"}

    if fm == 2:
        for nmrbr in feminino:
            if int(numerobr) == int(nmrbr):
                return f'{feminino[nmrbr]}'
        return 'Numero inválido'
    elif fm == 1:
        for nmrbr in masculin:
            if int(nmrbr) == int(numerobr):
                return f'{masculin[nmrbr]}'
        return 'Numero inválido'
    else:
        return 'Numero inválido\n'


def monetario(real):
    dolar = float(real)/5
    if dolar <= 1:
        return f'{dolar} dolar.'
    else:
        return f'{dolar} dolares.'

"""
# Criando função para facilitar formatação da tabela de opções
def linha(indice, opcao):
    dois = RED + f'|{indice:^3d}|{opcao.title():^33s}|'
    tres = '+---+---------------------------------+' + RESET
    return f'{dois}\n{tres}'


# Armazenando as cores em variáveis
RED = "\033[1;31m"
RESET = "\033[0;0m"

# Imprimir pro usuário
print_intro = "Olá, bem vindo(a) :)!\nNesse programa você pode checar " \
                "como seriam suas\nmedições se estivéssemos nos Estados Unidos.\n" \
                "As instruções a seguir vão lhe guiar para\nutilizar o programa " \
                "sem demais problemas.\n\n" \
                + RED + "-> Instruções: " + RESET + \
                "\n1. Digite o número da opção que deseja (apenas um número por vez);" \
                "\n2. Pressione ENTER;" \
                "\n3. Se a sua resposta for um número decimal, utilize '.' invés de ',';" \
                "\n4. Assim que receber a resposta do servidor, pressione ENTER novamente para continuar o programa."

print_opcs = f'\n\n-> OPÇÕES DISPONÍVEIS: ' \
            + RED + f'\n+---+---------------------------------+' + RESET + \
            f'\n{linha(1, "Calcule sua altura")}' \
            f'\n{linha(2, "Converta uma distância")}' \
            f'\n{linha(3, "Pese seu alimento")}' \
            f'\n{linha(4, "Confira seu tamanho de calçado")}' \
            f'\n{linha(5, "Converta p/dolar (aproximado)")}' \
            f'\n{linha(9, "Sair do programa")}\nDigite a opção desejada: '
"""
# TESTES:
"""
    print("Tranformar metros em pés:")
    meter = float(input("Diga a medida em metros (utilize '.' invés de ',': "))
    print(comprimento(meter))
    
    print()
    
    print("Tranformar km em milhas:")
    qm = float(input("Diga a medida em quilometros (utilize '.' invés de ',': "))
    print(distancia(qm))
    
    print()
    
    print("Tranformar kg em pounds:")
    qg = float(input("Diga a medida em quilogramas (utilize '.' invés de ',': "))
    print(peso(qg))
    
    print()
    
    print("Numero de calçados BR -> EUA")
    sexo = input("Seu tamanho é masculino[1] ou feminino?[2] ")
    numero = float(input("Diga a medida na numeração brasileira: "))
    print(sapato(sexo, numero))
"""
