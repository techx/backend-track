Databases

In this section, we will be integrating databases into our application!

At this point, you should have a working message application that can receive
messages and add it to a list of messages to display. This list would clear
every time the server crashes or is shut down.

Databases make the data permanent, so that if the server encounters a fatal
error, it can recover the messages it lost earlier.

In order to complete this section, we must make it so that the data is stored
separately from the server in MongoDB.

To use MongoDB, we can import it as so:
from pymongo import MongoClient

We can then configure the client given a SRV (like a URL in a web browser):
client = MongoClient(SRV)

We can then enter the specific db and collections within:
db = client['blueprint']
messages = db['messages']

We can then interact with messages through methods such as find() and
insert_one(). It's worth Googling around to practice looking for documentation.

Given these tools, you should be able to integrate a working database! As a
stretch goal, you can also use the database combined with a flask session to
implement a login system.

A flask session is essentially a dictionary that stays the same even as the
user navigates around our web service. To use a session, we have to set a
secret key for the application:

app.secret_key = <ANY RANDOM STRING>

Then, we can use the session like any other Python dictionary to keep track of
key value pairs!

If you have any questions, don't hesitate to ask us for help!