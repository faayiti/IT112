from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My Flask App"

@app.route('/about')
def about():
    return "Hello, I'm Safia"

if __name__ == '__main__':
    app.run(debug=True)
