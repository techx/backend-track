# Part 1

We will be building a simple Hello World website!

## Steps
1. Create the file `app.py`
1. In `app.py`:
    * Install pip if not already installed (should come with Python)
        * For Mac: `brew install python`
        * For Windows: https://stackoverflow.com/questions/41501636/how-to-install-pip3-on-windows
    * Run `pip3 install flask`
    * Import `Flask` from `flask`
    * Create a `Flask` object called `app`
    * Add a route to `app` to handle `GET` requests to the root path `/`
    * In the request handler, return "Hello World!" (or your favorite string)
    * Run the app
1. To start the server, run `python3 app.py`

If you get stuck at any point, this is a helpful resource: https://flask.palletsprojects.com/en/1.1.x/quickstart/.
