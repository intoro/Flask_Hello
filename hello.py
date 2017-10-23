from flask import Flask
project = Flask(__name__)


@project.route('/')
def welcome():
    return "Welcome to flask!"

if __name__ == '__main__':
    project.run()

