from flask import Flask

# create app object
app = Flask(__name__)

from app import calculator
