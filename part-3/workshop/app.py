# import mongo
from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
# set app secret key

# configure database

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html'
        # get messages
        # other data like login information
    )

@app.route('/register', methods=['POST'])
def register():
    # handle registration of user given username and password
    return 'success'

@app.route('/login', methods=['POST'])
def login():
    # check if provided username and password match entry in database

@app.route('/logout', methods=['POST'])
def logout():
    # remove the user's login status

@app.route('/message', methods=['POST'])
def message():
    # check user login status
    message = request.form['message']
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # insert message, username, and time into database
    return 'success'

if __name__ == '__main__':
    app.run(port=3000, debug=True, host='0.0.0.0')
