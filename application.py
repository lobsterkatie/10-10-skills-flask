from flask import Flask, render_template

app = Flask(__name__)

#####---------- app routes ----------#####

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/spurned")
def rejected_page():
    """React to the cruel rejection"""

    return render_template("rejection.html")


@app.route("/application-form")
def application_page():
    """Show the application form"""

    return render_template("application-form.html")


#####---------- code to run the server below ----------#####

if __name__ == "__main__":
    app.run(debug=True)
