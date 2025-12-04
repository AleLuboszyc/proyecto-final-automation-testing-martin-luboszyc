import csv
import os

def get_login_data():
    """Lee datos de login_data.csv y los devuelve como una lista de tuplas."""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, '..', 'data', 'login_data.csv')
    
    data = []
    
    with open(data_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:
            data.append(tuple(row))
            
    return data

