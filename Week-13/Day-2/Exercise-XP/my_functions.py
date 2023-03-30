import string
import random 
import json
import mysql.connector

def get_random_string(length):
    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)

def populate_database(database,database_model,json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    for line in json_file:
        user = database_model(id = line['id'],
                              name = line['name'],
                              street =  line['address']['street'],
                              city = line['address']['city'],
                              zipcode = line['address']['zipcode'])
        database.session.add(user)
    database.session.commit()    


