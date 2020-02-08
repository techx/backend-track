from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
app.secret_key = "secret"

messages = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', messages=messages)

@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append({'message': message, 'ts': now})
    return 'success'

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
