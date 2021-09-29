from flask import Flask
# app object
app = Flask(__name__)

# route (by default GET method)
@app.route("/hello-world")
def hello_world():
    return "hello world"

if(__name__ == "__main__"):
    app.run(debug = True)




