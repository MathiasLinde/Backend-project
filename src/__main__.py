from flask  import Flask, request, jsonify 
from jsonreader import read_json_from_file  
import datetime


file_path = 'product.json'
x = datetime.datetime.now()
app = Flask(__name__)

@app.route('/data/')
def get_products():
    json_data = read_json_from_file(file_path)
    
    return json_data

@app.route('/checkout_data/', methods = ['POST'])
def checkout_data():
    data = request.get_json()

    print("Recieved data:", data)
    
    // implement prepared statements to add checkout_data to database

    return 200
    



if __name__ == '__main__':
    app.run(debug=True)
