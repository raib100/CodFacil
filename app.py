from flask import Flask, flash, render_template


app= Flask (__name__)


@app.route('/')
@app.route('/<name>')
def hello(name='Ricardo'):
    return render_template('index.html', name=name)
    

app.run(host='localhost', port=5000, debug=True)
