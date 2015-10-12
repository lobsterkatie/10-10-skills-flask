from flask import Flask, render_template, request

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


@app.route("/application", methods=["POST"])
def confirmation_page():
    """Confirm the applicant's submission"""

    fname = request.form.get("firstname")
    lname = request.form.get("lastname")
    title = request.form.get("job-title")
    salary = int(request.form.get("min-salary"))

    return render_template("application-response.html",
                           firstname=fname, lastname=lname,
                           job_title=title, min_salary=salary)


#####---------- code to run the server below ----------#####

if __name__ == "__main__":
    app.run(debug=True)
