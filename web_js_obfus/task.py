from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = b'hello_world'

SESSION_TYPE = 'filesystem'
SESSION_USE_SIGNER = True


@app.route('/', methods=["GET", "POST"])
def entry_point():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        if request.form.get("your-password") == "qwoerhinnbxc":
            return render_template("qwoerhinnbxc.html")
        else:
            return render_template("index.html")


@app.route('/qwoerhinnbxc.html', methods=["GET", "POST"])
def get_flag():
    if request.method == "GET":
        return render_template("qwoerhinnbxc.html")


@app.route('/flag', methods=["GET", "POST"])
def try_get_flag():
    if request.method == "GET":
        return "Not bad but try again..."


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
    sess.init_app(app)
