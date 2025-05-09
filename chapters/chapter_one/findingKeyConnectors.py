#Identificar os conectores chave dentre os cientistas de dados utilizando um dump de dad
users = [
    { "id" : 0, "name" : "Hero"},
    { "id" : 1, "name" : "Dunn"},
    { "id" : 2, "name" : "Sue"},
    { "id" : 3, "name" : "Chi"},
    { "id" : 4, "name" : "Thor"},
    { "id" : 5, "name" : "Clive"},
    { "id" : 6, "name" : "Hicks"},
    { "id" : 7, "name" : "Devin"},
    { "id" : 8, "name" : "Kate"},
    { "id" : 9, "name" : "Klein"}
]

friendship_pairs = [ 
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8,9)
]

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j) # Adiciona o amigo j à lista de amigos do usuário i
    friendships[j].append(i) # Adiciona o amigo i à lista de amigos do usuário j

def number_of_friends(user):
    """Quantos amigos o _user_ tem?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

print(f"Total de conexões: {total_connections}")
print(f"Total de usuários: {num_users}")
print(f"Média de conexões: {avg_connections}")

# Achando as pessoas com mais conexões usando uma métrica de rede chamada de "centralidade de grau"
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key = lambda id_and_friends: 
id_and_friends[1],
    reverse = True)

print("Pessoas com mais conexões:", num_friends_by_id)

# Encontrando os amigos de amigos
def foaf_ids_bad(user):
    """foaf é um acronimo para Friend of a Friend"""
    return [foaf_id
            for friend_id in 
    friendships[user["id"]]
            for foaf_id in 
    friendships[friend_id]]

print(friendships[0])
print(friendships[1])
print(friendships[2])

# Encontrando os amigos de amigos de forma mais eficiente com o uso de um contador (amigos mais próximos)
from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id])

print(friends_of_friends(users[3]))

# Identificando usuários com interesses em comum
interest = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Cassandra"), (1, "NoSQL"), (1, "MongoDB"),
    (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), (2, "Python"),
    (2, "scikit learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"),
    (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"),
    (3, "regression"), (3, "probability"), (4, "machine learning"), (4, "regression"),
    (4, "decision trees"), (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"),
    (5, "C++"), (5, "Haskell"), (5, "programming languages"), (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Criando um dicionário de interesses, onde a chave é o id do usuário e o valor é uma lista de interesses. Dessa forma, podemos encontrar os interesses de cada usuário de forma mais eficiente.
def data_scientists_who_like(target_interest):
    """Ache os ids de todos os usuários que gostam do interesse alvo"""
    return [user_id
        for user_id, user_interest in interest
        if user_interest == target_interest       
    ]
    
print(data_scientists_who_like("Big Data"))

from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, user_interest in interest:
        user_ids_by_interest[user_interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interest:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interest_user_id
        for interest in interests_by_user_id[user["id"]]
        for interest_user_id in user_ids_by_interest[interest]
        if interest_user_id != user["id"]
    )
print(most_common_interests_with(users[0]))
print(most_common_interests_with(users[1]))
print(most_common_interests_with(users[2]))
print(most_common_interests_with(users[3]))

#Plotando salário por anos de experiência com os dados fornecidos
import matplotlib.pyplot as plt

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salaries = [salary for salary, _ in salaries_and_tenures]
tenures = [tenure for _, tenure in salaries_and_tenures]

plt.figure(figsize=(10, 6))
plt.scatter(tenures, salaries)
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário (R$)')
plt.title('Salário por Anos de Experiência')
plt.grid(True)
plt.tight_layout()
plt.show()