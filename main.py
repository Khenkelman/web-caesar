from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action = "http://localhost:5000/encrypt" method = "POST">
                    <label>Rotate By:</label>
                    <input name="rot" type="text" value="0">
                     <textarea name="text">{0}</textarea>
                     <button type="submit" name="submit" value="submit">Submit Query</button>
            </form> 
        </body>
    </html>
"""


@app.route("/", methods = ["POST", "GET"] )
def index():
    return form.format("")


@app.route('/encrypt', methods = ["POST", "GET"])
def encrypt():
    rot= request.form.get('rot')
    rotInt = int(rot)
    text= request.form.get('text')
    textNew = rotate_string(text, rotInt)
    return form.format(textNew)
    
    
app.run()