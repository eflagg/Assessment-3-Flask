from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form")
def app_form():

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def app_resp():

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary_requirement = request.form.get("salary-requirement")
    job = request.form.get("job")

    return render_template("application-response.html", first=first_name,
                            last=last_name, salary=salary_requirement, job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

