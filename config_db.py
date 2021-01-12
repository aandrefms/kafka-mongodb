from pymongo import MongoClient

usuario = input('Digite o usuario: ')
senha = input('Digite a senha')
client = MongoClient(f'mongodb+srv://{usuario}:{senha}@'
                     f'projectcluster1.evl3l.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.acme
todos = db.todos
def inserir_database(message):
    todos.insert_one({
        'NomeCidade': message["NomeCidade"],
        'Temperatura': message['Temperatura'],
        'Umidade': message['Umidade'],
        'Date': message['CreationTime']
    })