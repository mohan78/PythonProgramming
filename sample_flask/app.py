from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get('fullName')
        return render_template("greet.html", name=name)        
    return render_template("hello_world.html")


if __name__ == '__main__':
    app.run(debug=True)

