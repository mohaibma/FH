from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/room_rate')
def room_rate():
    return render_template("room_rate.html")

if __name__ == "__main__":
    app.run(debug=True)
