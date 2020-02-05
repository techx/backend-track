from pymongo import MongoClient
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_json('config.json')

client = MongoClient(app.config['MONGO_URI'])
db = client['blueprint']
messages = db['messages']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', messages=messages.find({}))

@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    messages.insert_one({'message': message})
    return 'success'

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
