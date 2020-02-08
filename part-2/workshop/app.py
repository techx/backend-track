from flask import Flask, render_template

app = Flask(__name__)

# store messages in a list

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    # get the message from the request and append it to the list
    pass

if __name__ == '__main__':
    app.run(port=3000, debug=True, host='0.0.0.0')
