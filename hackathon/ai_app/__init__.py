from flask import Flask

# this file causes this folder to act as a package, making imports easier
app = Flask(__name__)
app.config["selections"] = []
app.config["profs"] = []
app.config["completed_credits"] = 0
app.config["gpa"] = 0

# DO NOT MOVE THIS IMPORT, OTHERWISE YOU GET A CIRCULAR IMPORT ERROR

from ai_app import routes