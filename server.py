from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi_name(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<int:num>/<string:choice_word>')
def hello(num, choice_word):
    return "{choice_word * num}"


if __name__ == "__main__":
    app.run(debug=True)