from flask import Flask, request, jsonify, render_template
import controllers

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if (request.method == 'GET'):
        return render_template('login.html')

    data = request.get_json()
    email = data['email']
    password = data['password']
    return jsonify(controllers.login(email, password))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'GET'):
        return render_template('register.html')

    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    print(name, email, password)
    return jsonify(controllers.register(name, email, password))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
