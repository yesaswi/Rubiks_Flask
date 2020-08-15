from flask import Flask, render_template, url_for
from waitress import serve #Production Environment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    # serve(app, host='0.0.0.0', port=8000)