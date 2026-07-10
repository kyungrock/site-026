#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""식물·초록 보기 블로그 HTML 생성 (fb 피드 스타일)"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
SITE_PATH = ROOT / "config" / "site.json"
INDEX_PATH = ROOT / "index.html"

MEDIA_CLASSES = ("gift", "warm", "calm", "nature", "sunset", "luxe")

HOME_STATIC = [
    {
        "href": "guide.html",
        "title": "초록 식물 보기 가이드 — 입문·루틴·정서",
        "summary": "식물 감상의 기본부터 5분 루틴, 마사지·웰니스와 연결하는 법까지 단계별로 정리했습니다.",
        "category": "가이드",
        "date": "2026-06-11",
        "emoji": "📖",
    },
    {
        "href": "tips.html",
        "title": "식물 힐링 실전 팁 — 아침·저녁·책상",
        "summary": "창가 3분, 퇴근 후 잎 보기, 셀프케어와 함께하는 상황별 실전 팁 모음.",
        "category": "팁",
        "date": "2026-06-14",
        "emoji": "💡",
    },
    {
        "href": "faq.html",
        "title": "초록 식물 보기 FAQ — 자주 묻는 질문",
        "summary": "식물 힐링 효과, 시간, 초보 추천, 마사지와의 연결 등 자주 묻는 질문과 답변.",
        "category": "FAQ",
        "date": "2026-06-10",
        "emoji": "❓",
    },
]


def esc(s: str) -> str:
    return (
        (s or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def load_site() -> dict:
    site = json.loads(SITE_PATH.read_text(encoding="utf-8"))
    site.setdefault("site_name", site.get("site_title", "식물"))
    site.setdefault("tagline", f"{site.get('topic', '')} 관련 정보 허브")
    site.setdefault("domain", site.get("deploy_url", "https://site-026.stormkit.dev"))
    return site


def load_blog_posts() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    posts = [p for p in data.get("posts", []) if p.get("published", True)]
    posts.sort(key=lambda p: p.get("date", ""), reverse=True)
    return posts


def load_all_posts_raw() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    return data.get("posts", [])


def save_posts(posts: list[dict]) -> None:
    POSTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def slugify(text: str) -> str:
    s = (text or "").strip().lower()
    s = re.sub(r"[^\w\s-가-힣]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60] or "post"


def format_date_kr(d: str) -> str:
    if not d or len(d) < 10:
        return d or ""
    y, m, day = d[:10].split("-")
    return f"{y}년 {int(m)}월 {int(day)}일"


def media_class(post: dict) -> str:
    key = post.get("id") or post.get("title") or ""
    return MEDIA_CLASSES[hash(key) % len(MEDIA_CLASSES)]


def fix_escaped_html(content: str) -> str:
    if "&lt;a " not in content and "&lt;/a&gt;" not in content:
        return content
    import html as html_module

    return html_module.unescape(content)


def inline_format(text: str) -> str:
    s = esc(text)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    return s


def markdown_to_html(text: str) -> str:
    lines = (text or "").replace("\r\n", "\n").split("\n")
    parts: list[str] = []
    in_ul = False

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            parts.append("</ul>")
            in_ul = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            close_ul()
            continue
        if re.search(r"^<a\s+href=", stripped, re.I) or re.search(
            r"^<p>\s*<a\s+href=", stripped, re.I
        ):
            close_ul()
            parts.append(stripped if stripped.startswith("<p>") else f"<p>{stripped}</p>")
        elif stripped.startswith("<") and (stripped.endswith(">") or "</" in stripped):
            close_ul()
            parts.append(stripped)
        elif stripped.startswith("### "):
            close_ul()
            parts.append(f"<h3>{inline_format(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[2:])}</h2>")
        elif stripped.startswith("* "):
            if not in_ul:
                parts.append("<ul>")
                in_ul = True
            parts.append(f"<li>{inline_format(stripped[2:])}</li>")
        else:
            close_ul()
            parts.append(f"<p>{inline_format(stripped)}</p>")
    close_ul()
    return "\n".join(parts)


def normalize_content(content: str) -> str:
    c = (content or "").strip()
    if not c:
        return ""
    if c.startswith("<"):
        return fix_escaped_html(c)
    return fix_escaped_html(markdown_to_html(c))


def fb_header(site: dict, *, active: str = "", depth: int = 0) -> str:
    p = "../" * depth
    home = f"{p}index.html"

    def link(href: str, label: str, key: str) -> str:
        cls = ' class="fb-nav-link active"' if active == key else ' class="fb-nav-link"'
        return f'<a href="{href}"{cls}>{label}</a>'

    search = ""
    if depth == 0:
        search = """      <div class="fb-search">
        <span class="fb-search-icon">🔍</span>
        <input type="search" placeholder="식물 힐링 검색" aria-label="검색">
      </div>"""

    return f"""  <header class="fb-header">
    <div class="fb-header-inner">
      <a href="{home}" class="fb-logo">
        <span class="fb-logo-icon">🌿</span>
        <span>{esc(site["site_name"])}</span>
      </a>
{search}
      <button class="fb-nav-toggle" aria-label="메뉴 열기" aria-expanded="false">☰</button>
      <nav class="fb-header-nav">
        {link(home, "홈", "home")}
        {link(f"{p}guide.html", "가이드", "guide")}
        {link(f"{p}blog.html", "블로그", "blog")}
        {link(f"{p}tips.html", "팁", "tips")}
        {link(f"{p}faq.html", "FAQ", "faq")}
        {link(f"{p}blog-write.html", "글쓰기", "write")}
      </nav>
    </div>
  </header>"""


def fb_footer(site: dict, depth: int = 0) -> str:
    p = "../" * depth
    host = esc(site.get("host_name", "Stormkit"))
    slug = esc(site.get("slug", "site-026"))
    return f"""  <footer class="fb-footer">
    <p class="fb-footer-brand">{esc(site["site_name"])}</p>
    <p class="fb-footer-tagline">{esc(site.get("tagline", ""))}</p>
    <p class="fb-footer-copy">&copy; 2026 {esc(site["site_name"])} · {host} · {slug}</p>
  </footer>

  <nav class="fb-bottom-nav" aria-label="모바일 내비게이션">
    <div class="fb-bottom-nav-inner">
      <a href="{p}index.html"><span class="nav-icon">🏠</span>홈</a>
      <a href="{p}blog.html"><span class="nav-icon">📝</span>블로그</a>
      <a href="{p}guide.html"><span class="nav-icon">📖</span>가이드</a>
      <a href="{p}tips.html"><span class="nav-icon">💡</span>팁</a>
    </div>
  </nav>

  <script src="{p}js/main.js"></script>"""


def post_url(post: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    if post.get("href"):
        return f"{prefix}{post['href']}"
    return f"{prefix}blog/{esc(post['id'])}.html"


def fb_feed_item(post: dict, site: dict, depth: int = 0) -> str:
    url = post_url(post, depth)
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_kr(post.get("date", "")))
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    emoji = post.get("emoji") or "🌿"
    media = media_class(post)
    badge = "가이드" if post.get("href") in ("guide.html",) else (
        "팁" if post.get("href") in ("tips.html",) else "블로그"
    )
    if post.get("href") == "faq.html":
        badge = "FAQ"
    elif not post.get("href"):
        badge = cat if len(cat) <= 8 else "블로그"

    return f"""      <article class="fb-post">
        <a href="{url}" class="fb-post-header">
          <div class="fb-post-avatar">{emoji}</div>
          <div class="fb-post-meta">
            <span class="fb-post-author">{esc(site["site_name"])}<span class="fb-post-badge">{esc(badge)}</span></span>
            <span class="fb-post-info">{display} · 🌐</span>
          </div>
        </a>
        <div class="fb-post-body">
          <h2 class="fb-post-title">{title}</h2>
          <p class="fb-post-excerpt">{summary}</p>
        </div>
        <div class="fb-post-media {media}" aria-hidden="true">{emoji}</div>
        <div class="fb-post-stats">
          <div class="fb-reactions">
            <div class="fb-reaction-icons"><span>👍</span><span>❤️</span></div>
            <span>·</span>
          </div>
          <span>블로그</span>
        </div>
        <div class="fb-post-actions">
          <span class="fb-action-btn">👍 좋아요</span>
          <span class="fb-action-btn">💬 댓글</span>
          <span class="fb-action-btn">↗️ 공유</span>
        </div>
      </article>"""


def fb_card_item(post: dict, depth: int = 0) -> str:
    url = post_url(post, depth)
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_kr(post.get("date", "")))
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    emoji = post.get("emoji") or "🌿"
    media = media_class(post)
    gradients = {
        "gift": "linear-gradient(135deg,#11998e,#38ef7d)",
        "warm": "linear-gradient(135deg,#a8edea,#fed6e3)",
        "calm": "linear-gradient(135deg,#4facfe,#00f2fe)",
        "nature": "linear-gradient(135deg,#43e97b,#38f9d7)",
        "sunset": "linear-gradient(135deg,#89f7fe,#66a6ff)",
        "luxe": "linear-gradient(135deg,#c2e9fb,#a1c4fd)",
    }
    grad = gradients.get(media, gradients["gift"])
    return f"""        <a href="{url}" class="fb-card">
          <div class="fb-card-thumb" style="background:{grad}">{emoji}</div>
          <div class="fb-card-body">
            <span class="fb-card-badge">{cat}</span>
            <time class="fb-card-date" datetime="{dt}">{display}</time>
            <h2 class="fb-card-title">{title}</h2>
            <p class="fb-card-excerpt">{summary}</p>
            <span class="fb-card-link">읽어보기 →</span>
          </div>
        </a>"""


def home_feed_items(posts: list[dict]) -> list[dict]:
    items = list(posts) + list(HOME_STATIC)
    items.sort(key=lambda p: p.get("date", ""), reverse=True)
    return items


def home_sidebar_categories_html(posts: list[dict]) -> str:
    lines = [
        '        <a href="guide.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon guide">📖</span>',
        '          <span>가이드</span>',
        '        </a>',
        '        <a href="tips.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon tips">💡</span>',
        '          <span>식물 팁</span>',
        '        </a>',
        '        <a href="blog.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon gift">📝</span>',
        '          <span>블로그 전체</span>',
        '        </a>',
    ]
    counts: dict[str, int] = {}
    for p in posts:
        cat = p.get("category") or "블로그"
        counts[cat] = counts.get(cat, 0) + 1
    icons = ("🌬️", "🧘", "💆", "😌", "🌙", "✨")
    for i, (cat, n) in enumerate(sorted(counts.items(), key=lambda x: -x[1])[:5]):
        icon = icons[i % len(icons)]
        lines.extend([
            f'        <a href="blog.html" class="fb-shortcut">',
            f'          <span class="fb-shortcut-icon faq">{icon}</span>',
            f'          <span>{esc(cat)} ({n})</span>',
            f'        </a>',
        ])
    return "\n".join(lines)


def home_sidebar_recent_html(items: list[dict], limit: int = 6) -> str:
    lines = []
    icons = ("gift", "guide", "tips", "faq")
    for i, p in enumerate(items[:limit]):
        href = post_url(p, 0)
        title = esc(p.get("title", ""))
        if len(title) > 22:
            title = title[:20] + "…"
        icon_cls = icons[i % len(icons)]
        emoji = p.get("emoji") or "🌬️"
        lines.extend([
            f'        <a href="{href}" class="fb-shortcut">',
            f'          <span class="fb-shortcut-icon {icon_cls}">{emoji}</span>',
            f'          <span>{title}</span>',
            f'        </a>',
        ])
    return "\n".join(lines)


def replace_html_block(html: str, block: str, content: str) -> str:
    pattern = rf"(<!-- {block}_START -->).*?(<!-- {block}_END -->)"
    if not re.search(pattern, html, re.S):
        raise ValueError(f"index.html에 <!-- {block}_START/END --> 마커가 없습니다.")
    return re.sub(pattern, rf"\1\n{content}\n      \2", html, count=1, flags=re.S)


def update_index_html(out_dir: Path, posts: list[dict], site: dict) -> None:
    index_path = out_dir / "index.html"
    if not index_path.is_file():
        return
    html = index_path.read_text(encoding="utf-8")
    feed = home_feed_items(posts)
    feed_html = "\n".join(fb_feed_item(p, site) for p in feed)
    if not feed_html.strip():
        feed_html = '      <p class="blog-empty-feed">아직 블로그 글이 없습니다. <a href="blog-write.html">첫 글 작성하기</a></p>'
    html = replace_html_block(html, "HOME_FEED", feed_html)
    html = replace_html_block(
        html, "HOME_SIDEBAR_CATEGORIES", home_sidebar_categories_html(posts)
    )
    html = replace_html_block(html, "HOME_SIDEBAR_RECENT", home_sidebar_recent_html(feed))
    count = len(feed)
    html = re.sub(
        r"(<div class=\"fb-stat\"><strong>)\d+",
        rf"\g<1>{count}",
        html,
        count=1,
    )
    index_path.write_text(html, encoding="utf-8")


def render_blog_list(site: dict, posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    cards = "\n".join(fb_card_item(p) for p in posts) or (
        '        <p class="blog-empty-feed">아직 글이 없습니다. <a href="blog-write.html">첫 글 작성하기</a></p>'
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>블로그 | {esc(site["site_name"])}</title>
  <meta name="description" content="{esc(site.get("topic", ""))} 블로그. {esc(site.get("backlink_angle", ""))}">
  <meta name="keywords" content="{esc(site.get("keywords", ""))}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{domain}/blog.html">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{fb_header(site, active="blog")}
  <div class="fb-layout">
    <aside class="fb-sidebar fb-sidebar-left"></aside>
    <main class="fb-feed">
      <section class="page-hero">
        <h1>블로그</h1>
        <p>{esc(site.get("topic", ""))} · {esc(site.get("content_focus", "웰니스"))} 관련 글 모음</p>
        <p class="blog-write-hero-link"><a href="blog-write.html" class="btn-blog-write">✏️ 글 작성하기</a></p>
      </section>
      <div class="fb-card-list">
{cards}
      </div>
    </main>
    <aside class="fb-sidebar fb-sidebar-right"></aside>
  </div>
{fb_footer(site)}
</body>
</html>
"""


def render_blog_post(site: dict, post: dict, all_posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    pid = esc(post["id"])
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_kr(post.get("date", "")))
    author = esc(post.get("author", site["site_name"]))
    content = normalize_content(post.get("content", ""))
    emoji = post.get("emoji") or "🌿"
    media = media_class(post)
    tags = post.get("tags") or []
    tag_html = "".join(f'<span class="fb-tag">#{esc(t)}</span>' for t in tags)

    others = [p for p in all_posts if p["id"] != post["id"]][:3]
    related = ""
    if others:
        items = "\n".join(
            f'          <li><a href="{esc(p["id"])}.html">{esc(p.get("title", ""))}</a></li>'
            for p in others
        )
        related = f"""      <h2>다른 글 보기</h2>
      <ul>
{items}
      </ul>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {esc(site["site_name"])}</title>
  <meta name="description" content="{summary}">
  <meta name="keywords" content="{esc(site.get("keywords", ""))}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{domain}/blog/{pid}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{summary}">
  <meta property="article:published_time" content="{dt}">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{title}",
    "datePublished": "{dt}",
    "author": {{ "@type": "Organization", "name": "{author}" }},
    "inLanguage": "ko-KR",
    "url": "{domain}/blog/{pid}.html"
  }}
  </script>
</head>
<body>
{fb_header(site, active="blog", depth=1)}
  <article class="article-wrap">
    <nav class="breadcrumb"><a href="../index.html">홈</a> / <a href="../blog.html">블로그</a> / {cat}</nav>
    <article class="fb-post">
      <div class="fb-post-header">
        <div class="fb-post-avatar">{emoji}</div>
        <div class="fb-post-meta">
          <span class="fb-post-author">{author}<span class="fb-post-badge">{cat}</span></span>
          <span class="fb-post-info">{display} · 🌐</span>
        </div>
      </div>
      <div class="fb-post-body">
        <h1 class="fb-post-title">{title}</h1>
        <p class="fb-post-excerpt">{summary}</p>
      </div>
      <div class="fb-post-media {media}" aria-hidden="true">{emoji}</div>
    </article>
    <div class="article-content blog-article-body">
{content}
{related}
    </div>
    <nav class="article-nav">
      <a href="../blog.html" class="btn btn-primary">블로그 목록</a>
      <a href="../blog-write.html" class="btn btn-outline">글쓰기</a>
    </nav>
  </article>
{fb_footer(site, depth=1)}
</body>
</html>
"""


def blog_sitemap_urls() -> list[str]:
    return [f"blog/{post['id']}.html" for post in load_blog_posts()]


def write_blog_pages(out_dir: Path, site: dict) -> int:
    posts = load_blog_posts()
    (out_dir / "blog.html").write_text(render_blog_list(site, posts), encoding="utf-8")
    update_index_html(out_dir, posts, site)
    blog_dir = out_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    count = 1
    for post in posts:
        (blog_dir / f"{post['id']}.html").write_text(
            render_blog_post(site, post, posts), encoding="utf-8"
        )
        count += 1
    return count


def merge_draft(draft_path: Path, site: dict) -> dict:
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    if "posts" in draft:
        new_posts = draft["posts"]
    elif "id" in draft:
        new_posts = [draft]
    else:
        raise ValueError("draft JSON must be a post object or {{posts: [...]}}")

    posts = load_all_posts_raw()
    by_id = {p["id"]: i for i, p in enumerate(posts)}
    added, updated = 0, 0
    for p in new_posts:
        if not p.get("id"):
            p["id"] = slugify(p.get("title", "post")) + "-" + date.today().strftime("%Y%m%d")
        if not p.get("date"):
            p["date"] = date.today().isoformat()
        p.setdefault("published", True)
        p.setdefault("author", site.get("site_name", "식물"))
        p.setdefault("emoji", "🌿")
        p.setdefault("category", (p.get("tags") or ["블로그"])[0] if p.get("tags") else "블로그")
        if p.get("content"):
            p["content"] = normalize_content(str(p["content"]))
        if p["id"] in by_id:
            posts[by_id[p["id"]]] = p
            updated += 1
        else:
            posts.append(p)
            added += 1
    posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    save_posts(posts)
    return {"added": added, "updated": updated, "total": len(posts)}


def import_legacy_posts(site: dict) -> int:
    blog_dir = ROOT / "blog"
    if not blog_dir.is_dir():
        return 0
    existing_ids = {p["id"] for p in load_all_posts_raw()}
    imported = 0
    for html_path in sorted(blog_dir.glob("*.html")):
        post_id = html_path.stem
        if post_id in existing_ids:
            continue
        text = html_path.read_text(encoding="utf-8")
        title_m = re.search(r"<h1 class=\"fb-post-title\">(.*?)</h1>", text, re.S)
        summary_m = re.search(r'<p class="fb-post-excerpt">(.*?)</p>', text, re.S)
        cat_m = re.search(r'<span class="fb-post-badge">(.*?)</span>', text)
        date_m = re.search(r'<span class="fb-post-info">(\d{4})년 (\d+)월 (\d+)일', text)
        body_m = re.search(
            r'<div class="article-content[^"]*">(.*)</div>\s*<nav class="article-nav"',
            text,
            re.S,
        )
        if not title_m or not body_m:
            continue
        content = body_m.group(1).strip()
        content = re.sub(r"<h2>다른 글 보기</h2>.*", "", content, flags=re.S).strip()
        post = {
            "id": post_id,
            "title": re.sub(r"<[^>]+>", "", title_m.group(1)).strip(),
            "summary": re.sub(r"<[^>]+>", "", summary_m.group(1)).strip() if summary_m else "",
            "category": cat_m.group(1).strip() if cat_m else "블로그",
            "content": content,
            "tags": [cat_m.group(1).strip()] if cat_m else [],
            "author": site.get("site_name", "식물"),
            "date": (
                f"{date_m.group(1)}-{int(date_m.group(2)):02d}-{int(date_m.group(3)):02d}"
                if date_m
                else date.today().isoformat()
            ),
            "published": True,
            "emoji": "🌿",
        }
        posts = load_all_posts_raw()
        posts.append(post)
        save_posts(posts)
        existing_ids.add(post_id)
        imported += 1
    if imported:
        posts = load_all_posts_raw()
        posts.sort(key=lambda x: x.get("date", ""), reverse=True)
        save_posts(posts)
    return imported
