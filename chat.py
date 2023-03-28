# IMPORTS
from flask import Flask, request, jsonify,render_template
app=Flask(__name__)

from model import message


# ROUTING
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    # message(request.json['message'])
    return {
      "user":request.form['ques'],
      "bot":message(request.form['ques'])
   }

if __name__=='__main__':
    app.run(debug=True)