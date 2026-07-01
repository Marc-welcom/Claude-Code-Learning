class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics if topics is not None else []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"


class Video:
    def __init__(self, title, description, youtube_id):
        self.title = title
        self.description = description
        self.youtube_id = youtube_id

    def __repr__(self):
        return f"<Video {self.title}>"

courses = [
    Course("Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks",
           ["Variables and Data Types", "Control Structures", "Functions", "Object-Oriented Programming"]),
    Course("Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks",
           ["Flask Basics", "Routing and Templates", "Forms and Validation", "Database Integration", "Deployment"]),
    Course("Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks",
           ["Statistics Basics", "Python for Data Science", "Data Visualization", "Machine Learning Introduction"]),
    Course("Go Programming Essentials", "Master Go programming language from basics to advanced concepts.", "Robert Chen", "5 weeks",
           ["Go Basics and Syntax", "Goroutines and Concurrency", "Channels and Synchronization", "Web Services with Go", "Testing and Deployment"]),
    Course("Backend Development with Nodejs", "Build scalable backend applications using Node.js and Express.", "Michael Brown", "6 weeks",
           ["Node.js Fundamentals", "Express Framework", "REST APIs", "Database Integration with MongoDB", "Authentication and Security", "Deployment"]),
]

# Teaching videos embedded on the /videos page.
# youtube_id is the 11-char ID from a watch URL: youtube.com/watch?v=<youtube_id>
# Replace these placeholders with real videos from your channel.
videos = [
    Video("Getting Started", "Kick off the series with an overview of what you'll learn.", "dQw4w9WgXcQ"),
    Video("Core Concepts", "A deeper dive into the fundamentals covered in the course.", "dQw4w9WgXcQ"),
    Video("Hands-on Walkthrough", "Build along step by step in this practical lesson.", "dQw4w9WgXcQ"),
]