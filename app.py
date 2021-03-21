# app.py
from flask import Flask,request,render_template           # import flask, request and render_template
app = Flask(__name__, template_folder="templates")           # create an app instance

@app.route("/", methods =["GET", "POST"])                   # at the end point /
def test():                    # call method test
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       first_name = request.form.get("fname") 
       # getting input with name = lname in HTML form  
       last_name = request.form.get("lname")
       return "Your name is "+first_name + last_name
    return render_template("dummy.html")
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
