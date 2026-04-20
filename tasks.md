# Videos Tab Implementation Plan

## Goal
Add a **Videos** nav tab that embeds YouTube teaching videos from the user's channel.

## Architecture Decisions
- Video data stored as a list of dicts in `src/models.py` (title, description, youtube_embed_id)
- New route `GET /videos` → `videos()` view, registered in `app.py` via `add_url_rule()`
- New template `src/templates/videos.html` extending `layout.html`
- Responsive CSS grid for video cards with `<iframe>` embeds in `styles.css`
- Nav link added to `layout.html`

---

## Tasks

- [ ] **1. Add video data to `src/models.py`**
  - Add a `Video` dataclass/namedtuple with fields: `title`, `description`, `youtube_id`
  - Add an in-memory `videos` list with placeholder/real YouTube video IDs
  - _File:_ `src/models.py`

- [ ] **2. Add `videos()` view to `src/views.py`**
  - Import `videos` list from `models`
  - Return `render_template('videos.html', videos=videos)`
  - _File:_ `src/views.py`

- [ ] **3. Register `/videos` route in `src/app.py`**
  - Import `videos` view function
  - `app.add_url_rule('/videos', endpoint='videos', view_func=videos)`
  - _File:_ `src/app.py`

- [ ] **4. Create `src/templates/videos.html`**
  - Extend `layout.html`
  - Render a responsive grid of video cards
  - Each card: title, description, and `<iframe>` YouTube embed
  - _File:_ `src/templates/videos.html`

- [ ] **5. Add "Videos" nav link to `src/templates/layout.html`**
  - Add `<li><a href="{{ url_for('videos') }}">Videos</a></li>` to main-nav
  - _File:_ `src/templates/layout.html`

- [ ] **6. Add CSS styles for video grid and iframe embeds**
  - `.video-grid` responsive CSS grid
  - `.video-card` with title, description, and iframe wrapper
  - Responsive 16:9 aspect ratio iframe container
  - _File:_ `src/static/css/styles.css`

- [ ] **7. Write unit tests**
  - Test `GET /videos` returns 200
  - Test page contains expected video titles
  - Test YouTube embed iframes are present in response
  - _File:_ `tests/test_app.py`

- [ ] **8. Verify with Playwright**
  - Start Flask app and navigate to `/videos`
  - Confirm video cards render correctly
  - Take screenshot → `test-output/videos-tab-verification-2026-04-20.png`
