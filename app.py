#flask --app app run --debug
from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def index():
    return render_template('index.html')

app = Flask(__name__, static_url_path='/static')


app.run()

