from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/template')
@app.route('/template/index')
def index():
    return render_template('index.html')

@app.route('/formpatient')
def formpatient():
    return render_template('formpatient.html')

@app.route('/formprofessional')
def formprofessional():
    return render_template('formprofessional.html')

@app.route('/formfile')
def formfile():
    return render_template('formfile.html')

@app.route('/formpractices')
def formpractices():
    return render_template('formpractices.html')


@app.route('/newregister')
def newregister():
    return render_template('newregister.html')

@app.route('/manager')
def manager():
    return render_template('manager.html')

@app.route('/professional')
def professional():
    return render_template('professional.html')

    register_error_handlers(app)

    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)