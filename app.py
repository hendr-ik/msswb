# define imports
from flask import Flask
from flask import render_template



app = Flask(__name__)




@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/imprint")
def imprint():
    return render_template('imprint.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')


#-------------------------------------------------------------
# standard boilerplate
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
