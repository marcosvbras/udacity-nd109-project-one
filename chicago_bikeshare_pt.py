# coding: utf-8

# Imports
import csv
import matplotlib.pyplot as plt

# Column Indexes
START_TIME_INDEX = 0
END_TIME_INDEX = 1
TRIP_DURATION_INDEX = 2
START_STATION_INDEX = 3
END_STATION_INDEX = 4
USER_TYPE_INDEX = 5
GENDER_INDEX = 6
BIRTH_YEAR_INDEX = 7

# Vamos ler os dados como uma lista
print("Lendo o documento...")

with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for sample in data_list[1:21]:
    print(sample)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
input("Aperte Enter para continuar...")

# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for sample in data_list[0:20]:
    print(sample[GENDER_INDEX])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3


def column_to_list(data, index):
    """
        Função que retorna a coluna de uma lista de listas como uma lista

        Argumentos:
            data: lista de listas
            index: posição (coluna) à ser acessada e retornada

        Retorna:
            Uma lista com os valores da coluna definida através do argumento index
    """
    return [item[index] for item in data]


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, GENDER_INDEX)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
gender_list = column_to_list(data_list, GENDER_INDEX)
male = len(list(filter(lambda gender: gender == "Male", gender_list)))
female = len(list(filter(lambda gender: gender == "Female", gender_list)))

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5


def count_gender(data):
    """
        Função que verifica a frequência de Homens (Male) e Mulheres (Female) em uma lista de gêneros

        Argumentos:
            data: lista de gêneros

        Retorna:
            Uma lista com duas posições, sendo a primeira a frequência de homens e a segunda a de mulheres
    """
    male = len(list(filter(lambda gender: gender == "Male", column_to_list(data, GENDER_INDEX))))
    female = len(list(filter(lambda gender: gender == "Female", column_to_list(data, GENDER_INDEX))))
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6


def most_popular_gender(data):
    """
        Função que verifica qual o gênero mais popular em uma lista de gêneros

        Argumentos:
            data: lista de gêneros

        Retorna:
            Uma string contendo o gênero mais popular ou a string "Equal" caso a quantidade seja igual
    """
    count = count_gender(data)
    if count[0] > count[1]:
        return "Male"
    elif count[0] < count[1]:
        return "Female"

    return "Equal"


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)
input("Aperte Enter para continuar...")

# TAREFA 7
print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, USER_TYPE_INDEX)
user_types = ["Subscriber", "Customer"]
subscriber_count = len(list(filter(lambda user_type: user_type == "Subscriber", user_type_list)))
customer_count = len(list(filter(lambda user_type: user_type == "Customer", user_type_list)))
quantity = [subscriber_count, customer_count]
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, user_types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)
input("Aperte Enter para continuar...")

# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque nem todos os usuários do sistema de compartilhamento de bicicletas preencheram o campo de gênero, " \
         "sendo possivelmente um campo opcional."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, TRIP_DURATION_INDEX)
trip_duration_list = list(map(lambda i: int(i), trip_duration_list))
count_trip_duration = len(trip_duration_list)
trip_duration_list.sort()

# Min
min_trip = trip_duration_list[0]
# Max
max_trip = trip_duration_list[-1]
# Mean
mean_trip = sum(trip_duration_list) / count_trip_duration
# Median
if count_trip_duration % 2 == 0:
    median_trip = trip_duration_list[count_trip_duration / 2] + \
                  trip_duration_list[count_trip_duration / 2 + 1] / 2
else:
    median_trip = trip_duration_list[round(count_trip_duration / 2)]


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
start_stations = {station for station in column_to_list(data_list, START_STATION_INDEX)}

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = "yes"
answer = input("Você vai encarar o desafio? (yes ou no)")

def count_items(column_list):
    """
        Função que conta tipos de usuários sem definir os tipos

        Argumentos:
            column_list: lista de tipos de usuário

        Retorna:
            Uma tupla contendo uma lista de tipos e uma lista de suas respectivas contagens
    """
    item_types = []
    count_items = []

    for user_type in column_list:
        if user_type in item_types:
            index = item_types.index(user_type)
            count_items[index] += 1
        else:
            item_types.append(user_type)
            count_items.append(1)

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
