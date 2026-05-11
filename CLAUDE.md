# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup (Unix/Mac)
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Setup (Windows)
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# Run app
python src/app.py  # available at http://127.0.0.1:5000

# Run tests
python -m unittest discover -s tests                              # all tests
python -m unittest tests.test_app.AppTestCase.test_index          # single test
```

## Architecture

Routes are registered in `src/app.py` using `add_url_rule()` (not decorators), which keeps view functions in `src/views.py` decoupled from Flask. Views only import `render_template` from Flask.

**Routes:**
- `GET /` → `index()` — renders all courses
- `GET /course/<course_id>` → `course(course_id)` — course_id is a **1-based index** into the `courses` list (matching Jinja2's `loop.index`), not a model field
- `GET|POST /contact` → `contact()` — handles form with server-side validation (regex email, min 10-char address)

**Data:** `src/models.py` holds a `Course` class with `title, description, instructor, duration, topics` and an in-memory list of 4 hardcoded courses. No database exists.

**Templates** all extend `src/templates/layout.html` via `{% block content %}`. The base template provides nav and footer.

**Tests** live in `tests/test_app.py` as a single `AppTestCase` class (13 tests). Tests use Flask's test client set up in `setUp()`.

## Development Workflow

### Unit Tests Required

Add unit tests for every change and verify they pass before finishing.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**

1. Start the Flask app (if not already runnung - `python src/app.py`)
2. Use the Playwright MCP tool to connect to the application at `http://127.0.0.1:5000`
3. Navigate to and interact with the new feature to verify it works correctly
4. Take a screenshot of the working feature
5. Save the screenhot in the `test-output/` folder with a descriptive filename (e.g., `feature-name-verification-YYYY-MM-DD.png`)

This step ensure that all features are visually verified and provides documentation of the working state of the application.
