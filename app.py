from flask import Flask

flames = Flask(__name__)


if __name__ == '__main__':
    flames.run(debug=True)
