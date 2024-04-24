from flask import Flask, render_template

app = Flask(__name__)  # create the Flask app


@app.route('/')  # root directory, add endpoint
def index():
    return 'welcome to the webpage!'


@app.route('/page1')  # add endpoint
def page1():
    return 'This is the page1!'


@app.route('/page2')  # add endpoint
def page2():
    return render_template('test-template.html')


app.run(debug=True)  # debug= Can be chenged the code when the server is running
