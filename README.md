On local machine install virtualenv:
https://virtualenv.pypa.io/en/stable/installation/

works on all platforms I use Ubuntu:
 sudo apt-get install virtualenv


  Once it installs navigate to the directory you will be working in and use the command:
virtualenv venv

  You will see the the creation of a python installation local to the working directory. The venv is a variable and can be anything you choose:
virtualenv anything_

  after it installs activate your enviroment:
source venv/bin/activate

  You know its working if you see (venv) add to the beginning of your command line

git init

  create your basic file structure:

touch hello.py .gitignore README.md requirements.txt

  Add this to your .gitignore file:

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# folders
venv/



  Now install Flask:
pip install flask

  After installing anything related to the flask app save it to a text file
pip freeze > requirements.txt

  add this to the hello.py

from flask import Flask
project = Flask(__name__)


@project.route('/')
def welcome():
    return "Welcome to flask!"

if __name__ == '__main__':
    project.run()


    Now run the app:
python hello.py

  it will say :  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) You can now open your browser to that address and you will see "Welcome To Flask!"
