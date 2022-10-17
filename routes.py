
from ben_and_jerry import maxx


@maxx.route("/")
def noor():
    return "<HTML><BODY><H1>Hi there!</H1></HTML>"

@maxx.route("/ben")
def ben():
    return "<HTML><BODY><H1>Yet another file</H1></BODY></HTML>"

