# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run from the `course-explainer-app/` directory.

```bash
# Setup
python -m venv venv && source venv/bin/activate
uv pip install -r requirements.txt          # or: pip install -r requirements.txt

# Run the dev server (http://127.0.0.1:5000, debug mode on)
python src/app.py

# Run all tests
python -m unittest discover -s tests

# Run a single test
python -m unittest tests.test_app.AppTestCase.test_index
```

Production entry point is `gunicorn` (in requirements) — serve `app:app` from the `src/` directory.

## Architecture

A minimal Flask web app for browsing courses. Three source modules under `src/`:

- **`app.py`** — Entry point. Creates the Flask app and registers routes via `add_url_rule` (not decorators): `/` → `index`, `/course/<course_id>` → `course`.
- **`views.py`** — View functions that render templates.
- **`models.py`** — A plain `Course` class and a hardcoded module-level `courses` list (the data source).

### Import path convention (important)

`app.py` uses flat imports (`from views import ...`), not package-relative imports. The app therefore only runs correctly when `src/` is on the Python path. Tests handle this by inserting `src/` into `sys.path` at the top of `tests/test_app.py` — replicate that pattern in any new test file.

### Templates

`layout.html` is the base (header/nav/footer + `{% block content %}`). Note the two page templates currently use **different and inconsistent** mechanisms:
- `course.html` correctly `{% extends 'layout.html' %}`.
- `index.html` uses `{% include 'layout.html' %}` wrapped in its own full HTML document instead of extending it.

When editing templates, prefer the `extends`/`block` pattern.

### Known gap: models not wired to views

`models.py` defines `Course` objects, but `views.py` does **not** pass them to the templates — `course()` passes only `course_id`, and `index()` passes nothing. Meanwhile `course.html` references `{{ course.title }}`, `{{ course.description }}`, `{{ course.instructor }}`, `{{ course.duration }}`, and `{{ course.topics }}` (and `index.html` hardcodes course links 1–3). The model fields also lack a `topics` attribute the template expects. Connecting `models.courses` to the views is the main unfinished work here.

Because of this, the tests assert against strings from `layout.html` (e.g. `"Course Details"` comes from the nav link, not the course content) rather than actual course data.

## Add Unit tests
- Whenever you add any changes add unit tests and run and make sure the tests passes.
