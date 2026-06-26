from flask import render_template

def index():
    return render_template('index.html')

#def course(course_id):
#    return render_template('course.html', course_id=course_id)
#@app.route("/course/<int:course_id>")
def course_detail(course_id):
    course = get_course(course_id)
    if course is None:
        abort(404)                                   # clean 404 instead of a 500
    return render_template("course.html", course=course)   # <-- the fix