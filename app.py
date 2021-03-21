# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                    # call method hello
    return "<h1>Hello Sathish!</h1><body>This is body</body>"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
