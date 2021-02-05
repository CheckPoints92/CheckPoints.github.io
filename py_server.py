from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:code>', methods=['GET'])
def user(code):
    return "User code: " + str(code)


if __name__ == "__main__":
    app.run(debug=True)
    print(user())