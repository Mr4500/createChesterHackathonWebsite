from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/TrickOrTreat')
def TrickOrTreat():
    return render_template('map.html')


#host and port can be changed if needed to
app.run(host='0.0.0.0', port=3025)