from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
    <head>
        <title>Python Webpage</title>
        <style>
            body {
                background-color: #306998; /* Python Blue */
                color: white;
                text-align: center;
                font-family: Arial, sans-serif;
            }
            img {
                width: 200px;
                margin-top: 20px;
            }
            p {
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
        <p>This webpage is made using pure Python</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)