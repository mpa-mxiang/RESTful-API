from flask import Flask      #Import the Flask class


app = Flask(__name__)      #Create an instance of the class


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
