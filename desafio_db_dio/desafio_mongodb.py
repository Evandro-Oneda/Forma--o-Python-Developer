import datetime
import pprint
from pymongo import MongoClient


connection_string = "mongodb+srv://oneda:oneda@cluster0.bldx3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]

collection = db_connection.get_collection("minhaCollection")

collection.insert_one({    
    "id":"1", 
    "nome": "evandro",
    "cpf": "123.456.789-80",
    "endereco":"rua teste",
    "tags":["evandro", "123.456.789-80","rua teste" ],
    "data": datetime.datetime.now()

})
collection.insert_one({     
    "id":"2",
    "nome": "maria",
    "cpf": "789.456.123-80",
    "endereco":"rua bla bla",
    "tags":["maria", "789.456.123-80","rua bla bla" ],
    "data": datetime.datetime.now()
})

collection.insert_one({     
   "id":"3",
    "nome": "paulo",
    "cpf": "456.789.123-10",
    "endereco":"rua do ze",
    "tags":["paulo", "456.789.123-10","rua do ze" ],
    "data": datetime.datetime.now()
})



# procurar informacoes
search_filter = {"nome":"evandro"}
response = collection.find(search_filter)
for registry in response: print(registry)
print("##################################################################################\n")
search_filter = {"nome":"maria"}
response = collection.find(search_filter)
for registry in response: print(registry)
print("##################################################################################\n")
search_filter = {"nome":"paulo"}
response = collection.find(search_filter)
for registry in response: print(registry)