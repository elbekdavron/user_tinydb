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
    db = TinyDB(db_path)
    for info in data:
        db.insert(info)

def query_db(db_path, query_field, query_value):
    
    db = TinyDB(db_path)
    User = Query()
    if query_field and query_value:  
        return db.search(User[query_field] == query_value)
    

if __name__ == "__main__":
    
    csv_file_path = 'user_data.csv' 
    db_file_path = 'user.json'  

    data = read_csv(csv_file_path)
    
    insert_into_db(data, db_file_path)

    teachers = query_db('user.json', 'job', 'Teacher')
    print(teachers)
    
    
    

    
    
    
    
    
    
   