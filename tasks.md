/# Tasks: Add a "Videos" Tab (Embed YouTube Teaching Videos)

Tracks the work to add a new **Videos** tab that embeds YouTube teaching videos in a responsive grid.
Source is a hardcoded `Video` list (mirrors the `Course` pattern); no external API.

## Checklist

- [x] **models.py** — Add `Video` class + module-level `videos` list (with placeholder video IDs).
- [x] **views.py** — Add `videos()` view; import `videos` list aliased as `videos_data`.
- [x] **app.py** — Register route `/videos` via `add_url_rule`; import `videos` from views.
- [x] **templates/videos.html** — New page using `{% extends 'layout.html' %}` + responsive grid of iframes.
- [x] **templates/layout.html** — Add `Videos` nav `<li>` to `.main-nav`.
- [x] **static/css/styles.css** — Add `.video-grid` / `.video-card` / `.video-embed` (16:9) styles.
- [x] **tests/test_app.py** — Add `test_videos` and `test_videos_nav_link_present`; run suite.

## Verification

- [x] `python -m unittest discover -s tests` — all tests pass.
- [ ] `python src/app.py` → open `http://127.0.0.1:5000/videos` and confirm the grid + nav link render.

## Open item

- [ ] Replace placeholder `youtube_id`s / titles / descriptions in `src/models.py` with real videos
      from the channel. (Each `youtube_id` is the 11-char ID from `youtube.com/watch?v=<id>`.)
