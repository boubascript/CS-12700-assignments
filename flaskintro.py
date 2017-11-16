#localhost is the same as 127
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "ayyyyyyuuuuhhh"


app.run(debug = True, host = "0.0.0.0", port = 8000)