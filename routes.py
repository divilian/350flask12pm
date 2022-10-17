
from flask import render_template, request
from ben_and_jerry import maxx
import sqlite3


@maxx.route("/")
def noor():
    if "faveflave" in request.args:
        return f"<HTML><BODY><p>Wow, {request.args['faveflave']} is my favorite too!</BODY></HTML>"
    else:
        conn = sqlite3.connect("bj.sqlite")
        cur = conn.cursor()
        cur.execute("select distinct flavorName from recipe")
        our_query_results = cur.fetchall()
        return render_template("chooseflavor.html",
            flavornames=our_query_results)

@maxx.route("/ben")
def ben():
    return "<HTML><BODY><H1>Yet another file</H1></BODY></HTML>"

