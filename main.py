from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'main' #Основная страница. В данный момент - затычка.
