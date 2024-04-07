import json


def read_json_from_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None 
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON data from '{file_path}'.")
        return None


file_path = 'product.json'  # Specify the path to your .json file
json_data = read_json_from_file(file_path)
if json_data:
    print(json_data)
