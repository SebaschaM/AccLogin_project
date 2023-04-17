from flask import Flask, request, jsonify
import controllers

app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    return jsonify(controllers.login(email, password))


@app.route("/register", methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return jsonify(controllers.register(name, email, password))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
