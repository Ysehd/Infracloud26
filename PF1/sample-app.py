from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if not os.path.exists('tempdir'):
    os.makedirs('tempdir')

if __name__ == "__main__":
    print("PF1 Python Webapp gestart op http://127.0.0.1:5000")
    app.run(debug=True)
