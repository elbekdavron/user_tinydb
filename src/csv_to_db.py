import csv
from tinydb import TinyDB, Query

def read_csv(file_path):
    data = []
    file = open(file_path, 'r') 
    reader = csv.DictReader(file) 
    for row in reader:
        data.append(row)
    file.close()    
    return data


def insert_into_db(data, db_path):
    
    pass

def query_db(db_path, query_field, query_value):
    
    pass

if __name__ == "__main__":
    
    csv_file_path = 'user_data.csv' 
    db_file_path = 'user.json'  

    data = read_csv(csv_file_path)
    
    
    
    
    
    
    
    
    
    
    
   