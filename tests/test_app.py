import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_videos(self):
        response = self.app.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teaching Videos', response.data)
        # the embed iframe should be present for each video
        self.assertIn(b'youtube.com/embed/', response.data)

    def test_videos_nav_link_present(self):
        # the Videos tab should appear in the shared nav on every page
        response = self.app.get('/')
        self.assertIn(b'/videos', response.data)

    def test_index_shows_course_titles(self):
        # The home page should list each course by its title, not "Course N"
        response = self.app.get('/')
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertNotIn(b'>Course 1<', response.data)

    def test_no_leaked_css_or_markers(self):
        # Regression: raw CSS / "...existing code..." markers were pasted
        # into layout.html and rendered as visible text on the home page.
        response = self.app.get('/')
        self.assertNotIn(b'...existing code...', response.data)
        self.assertNotIn(b'box-sizing: border-box', response.data)

if __name__ == '__main__':
    unittest.main()