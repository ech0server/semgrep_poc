import os
import flask
import hashlib

app = flask.Flask(__name__)

@app.route("/post_param_branch", methods=["POST"])
def post_param_branch():
    param = flask.request.form['param']
    if True:
        # ruleid: os-system-injection
        os.system(param)

@app.route("/ok")
def ok():
    # ok: os-system-injection
    os.system("This is fine")

@app.route("filter")
def filter():
    # ok: open-redirect
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('main.index')
    return redirect(next_page)
