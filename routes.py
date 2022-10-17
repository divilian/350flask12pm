
from flask import render_template, request, redirect, url_for
from ben_and_jerry import maxx
import sqlite3


@maxx.route("/")
def noor():
    if "faveflave" in request.args:
        return redirect(url_for("browserecipes",
            flavor=request.args['faveflave']))
    else:
        conn = sqlite3.connect("bj.sqlite")
        cur = conn.cursor()
        cur.execute("select distinct flavorName from recipe")
        our_query_results = cur.fetchall()
        conn.close()
        return render_template("chooseflavor.html",
            flavornames=our_query_results)

@maxx.route("/ben")
def ben():
    return "<HTML><BODY><H1>Yet another file</H1></BODY></HTML>"

@maxx.route("/browserecipes")
def browserecipes():
    conn = sqlite3.connect("bj.sqlite")
    cur = conn.cursor()
    cur.execute("select name,cartonsOrdered from recipe where flavorName=?",
        (request.args['flavor'],))
    recipestuff = cur.fetchall()
    conn.close()
    return render_template("browserecipes.html", flavor=request.args['flavor'],
        recipestuff=recipestuff)

@maxx.route("/recipedetails")
def recipedetails():
    return f"You just asked for the details for {request.args['recipe']}!"



