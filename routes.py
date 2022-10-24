
from flask import render_template, request, redirect, url_for
from ben_and_jerry import maxx
import sqlite3


@maxx.route("/")
def noor():
    if "faveflave" in request.args:
        return redirect(url_for("browserecipes",
            flavor=request.args['faveflave']))
    else:
        msg = request.args['msg'] if 'msg' in request.args else ""
        conn = sqlite3.connect("bj.sqlite")
        cur = conn.cursor()
        cur.execute("select distinct flavorName from recipe order by flavorName")
        our_query_results = cur.fetchall()
        conn.close()
        return render_template("chooseflavor.html",
            flavornames=our_query_results, msg=msg)

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
    if 'recipe' not in request.args:
        return "<HTML><BODY>Please give us a recipe bruh.</BODY></HTML>"

    if 'quantity' in request.args:
        # Aha! They just pressed submit on the order form.
        conn = sqlite3.connect("bj.sqlite")
        cur = conn.cursor()
        cur.execute("update recipe set cartonsordered=cartonsordered+? " +
            " where name=?",
            (int(request.args['quantity']), request.args['recipe'],))
        conn.commit()
        return redirect(url_for("noor",
            msg=f"Thanks for your {request.args['quantity']}-carton order!"))
    
    else:
        # They are new to this page: just show them the recipe details.
        conn = sqlite3.connect("bj.sqlite")
        cur = conn.cursor()
        cur.execute("select flavorName from recipe where name=?",
            (request.args['recipe'],))
        specificFlavor = cur.fetchone()[0]
        cur.execute("select mixin_name from ingredients where recipe_name=?",
            (request.args['recipe'],))
        mixins = cur.fetchall()
        conn.close()
        return render_template("recipedetails.html",
            recipename=request.args['recipe'], flavor=specificFlavor,
            mixins=mixins)



