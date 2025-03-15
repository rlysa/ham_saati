from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Возвращает макет основной страницы.

    :return: HTML-содержимое главной страницы. В текущей версии - заглушка.
    '''
    return 'main'

if __name__ == "__main__":
    app.run()
