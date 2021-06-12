from flask import Flask, render_template
from AzureDB import AzureDB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/guestbook')
def guestbook():
    with AzureDB() as a:
        data = a.azureGetData()
    return render_template("guestbook.html", data = data)


if __name__ == '__main__':
    app.run(debug=True)
