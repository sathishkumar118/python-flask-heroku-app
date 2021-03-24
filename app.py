# app.py
from flask import Flask,request,render_template           # import flask, request and render_template
import os
import psycopg2

app = Flask(__name__, template_folder="templates")           # create an app instance


    
@app.route("/", methods =["GET", "POST"])                   # at the end point /
def test():                    # call method test
    #DATABASE_URL = os.environ['DATABASE_URL']
    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    if request.method == "POST": 
       # getting input url
       input_url = request.form.get("url")
       return "<BODY>"+input_url.upper()+"</BODY>"
    return render_template("url.html")
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
