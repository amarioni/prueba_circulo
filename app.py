from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



# landing page that will display all the books in our database
# This function will operate on the Read operation.
@app.route('/')
@app.route('/template')
@app.route('/template/index')
def index():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug=True)