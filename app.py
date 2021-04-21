import os
import flask
import hashlib

app = flask.Flask(__name__)

@app.route("/post_param_branch", methods=["POST"])
def post_param_branch():
    param = flask.request.form['param']
    if True:
        os.system(param)

@app.route("/ok")
def ok():
    os.system("This is fine")

@app.route("open_redirect/")
def open_redirect():
    url = request.args.get("url")
    print("something")
    return redirect(url)
# Other test
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    param = flask.request.args.get("param")
    eval("import %s" % (param,))

    #add changes
