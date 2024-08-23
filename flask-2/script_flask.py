from flask import Flask

app = Flask(__name__)


# @app.route('/hello_world')
# def test_function():
#     return "Привет, мир!"


# if __name__ == '__main__':
def run():
    app.run(debug=True)
