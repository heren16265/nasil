from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('icat/')
def icat():
    return render_template('icat.html')




app.run(debug=True)