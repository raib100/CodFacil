from flask import Flask, render_template


app = Flask(__name__) # Los html se encuentran en la carpeta templates, para cambiar:..name__,teplate_folder= 'nueva carpeta'


@app.route('/')
def index():
    return 'Hola Mundo'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
