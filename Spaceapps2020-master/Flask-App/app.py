from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/Navbar')
def index():
    return render_template("Navbar.html")

if __name__ == '__main__':
    app.run(debug=True)
