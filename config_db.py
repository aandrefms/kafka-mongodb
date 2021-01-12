from pymongo import MongoClient

usuario = 'andre'  # input('Digite o usuario: ')
senha = '182597'  # input('Digite a senha')
client = MongoClient(f'mongodb+srv://{usuario}:{senha}@'
                     f'projectcluster1.evl3l.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.acme
todos = db.todos
message = {"NomeCidade": "S\u00e3o Paulo", "Temperatura": 29.36, "Umidade": 61, "CreationTime": "2021-0112 11:56:54"}
def inserir_database(message):
    todos.insert_one({
        'NomeCidade': message["NomeCidade"],
        'Temperatura': message['Temperatura'],
        'Umidade': message['Umidade'],
        'Date': message['CreationTime']
    })

'''
for item in todos.find():
    print(item)'''