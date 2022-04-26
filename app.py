from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Real-time Data',
        year=datetime.now().year
    )


@app.route('/configuration')
def configuration():
    """Renders the about page."""
    return render_template(
        'configuration.html',
        title='System Configuration',
        year=datetime.now().year,
        message='System Configuration'
    )


if __name__ == '__main__':
    app.run()
