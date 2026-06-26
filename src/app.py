"""Minimal Flask application for the Claude Code Learning project.

Serves a list of courses and a detail page for each course. The course
detail route passes the selected ``course`` object to the template, which
is what prevents the ``jinja2.exceptions.UndefinedError: 'course' is
undefined`` error reported in issue #2.
"""

from flask import Flask, abort, render_template

app = Flask(__name__)

# In-memory sample data. In a real application this would come from a database.
COURSES = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "description": "Learn the fundamentals of Python programming, including "
        "variables, control flow, functions, and data structures.",
        "instructor": "Ada Lovelace",
        "duration_hours": 12,
    },
    {
        "id": 2,
        "title": "Web Development with Flask",
        "description": "Build dynamic web applications using the Flask framework, "
        "Jinja2 templates, and routing.",
        "instructor": "Grace Hopper",
        "duration_hours": 18,
    },
    {
        "id": 3,
        "title": "Working with Claude Code",
        "description": "Discover how to use Claude Code to accelerate software "
        "development, review pull requests, and fix issues.",
        "instructor": "Alan Turing",
        "duration_hours": 8,
    },
]


def get_course(course_id):
    """Return the course matching ``course_id`` or ``None`` if not found."""
    return next((course for course in COURSES if course["id"] == course_id), None)


@app.route("/")
def index():
    """Render the list of available courses."""
    return render_template("index.html", courses=COURSES)


@app.route("/course/<int:course_id>")
def course_detail(course_id):
    """Render the detail page for a single course.

    The ``course`` variable is explicitly passed to the template. Omitting
    it is what caused the reported ``UndefinedError: 'course' is undefined``.
    """
    course = get_course(course_id)
    if course is None:
        abort(404)
    return render_template("course.html", course=course)


if __name__ == "__main__":
    app.run(debug=True)
