from flask import render_template, abort
from models import courses

# COURSES = {
#     1: "Python Basics",
#     2: "Flask Web Development",
#     3: "APIs and Web Services",
# }

def index():
    return render_template('index.html', courses=courses)


def get_course(course_id):
    try:
        course_index = int(course_id) -1
    except (TypeError, ValueError):
        return None
    return courses[course_index] if 0 <= course_index < len(courses) else None

def course(course_id):
    course = get_course(course_id)
    if course is None:
        return "Course not found", abort(404)    # clean 404 instead of a 500
    return render_template("course.html", course_id=course_id, course=course)