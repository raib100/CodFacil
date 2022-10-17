from flask import Flask, request, render_template

import forms

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    comment_form = forms.CommentForm()    
    title = 'Curso de Flask'
    return render_template('index.html', title=title, form=comment_form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
