#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""블로그 글 추가 후 HTML·sitemap 재생성"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from blog import (  # noqa: E402
    blog_sitemap_urls,
    import_legacy_posts,
    load_site,
    merge_draft,
    write_blog_pages,
)

OUT_DIR = ROOT
STATIC_PAGES = [
    ("", "1.0"),
    ("guide.html", "0.9"),
    ("tips.html", "0.8"),
    ("faq.html", "0.8"),
    ("blog.html", "0.85"),
    ("blog-write.html", "0.3"),
]


def resolve_draft_path(arg: str) -> Path:
    candidates = [
        Path(arg),
        ROOT / arg,
        Path.home() / "Downloads" / Path(arg).name,
    ]
    for p in candidates:
        if p.is_file():
            return p.resolve()
    tried = "\n  ".join(str(c) for c in candidates)
    raise FileNotFoundError(
        f"파일을 찾을 수 없습니다: {arg}\n"
        f"시도한 경로:\n  {tried}\n\n"
        f"글쓰기 페이지에서 '게시 파일 저장' 후\n"
        f"  python scripts/publish_blog.py --add blog-draft.json"
    )


def write_sitemap(domain: str) -> None:
    domain = domain.rstrip("/")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, priority in STATIC_PAGES:
        loc = f"{domain}/{path}" if path else f"{domain}/"
        lines.append(f"  <url><loc>{loc}</loc><priority>{priority}</priority></url>")
    for path in blog_sitemap_urls():
        lines.append(
            f'  <url><loc>{domain}/{path}</loc><priority>0.7</priority></url>'
        )
    lines.append("</urlset>\n")
    (OUT_DIR / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_robots(domain: str) -> None:
    domain = domain.rstrip("/")
    (OUT_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml\n",
        encoding="utf-8",
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    parser = argparse.ArgumentParser(description="블로그 글 게시 및 페이지 재생성")
    parser.add_argument(
        "--add",
        metavar="FILE",
        help="새 글 JSON 병합 (단일 글 또는 {posts:[...]})",
    )
    parser.add_argument("--list", action="store_true", help="등록된 글 목록")
    parser.add_argument(
        "--import-legacy",
        action="store_true",
        help="기존 blog/*.html → data/blog-posts.json 가져오기",
    )
    args = parser.parse_args()

    site = load_site()

    if args.import_legacy:
        n = import_legacy_posts(site)
        print(f"기존 HTML에서 {n}건 가져옴")

    if args.add:
        draft_path = resolve_draft_path(args.add)
        print(f"파일 사용: {draft_path}")
        result = merge_draft(draft_path, site)
        print(
            f"병합 완료: 추가 {result['added']}건, 수정 {result['updated']}건, "
            f"총 {result['total']}건"
        )

    if args.list:
        from blog import POSTS_PATH, load_all_posts_raw

        posts = load_all_posts_raw()
        if not posts:
            print("  (등록된 글이 없습니다)")
        for p in posts:
            status = "공개" if p.get("published", True) else "비공개"
            print(
                f"  [{status}] {p.get('date', '')}  {p.get('id')}  {p.get('title')}"
            )
        if not args.add and not args.import_legacy:
            return

    from blog import POSTS_PATH

    if not POSTS_PATH.exists():
        print("data/blog-posts.json 이 없습니다. --import-legacy 또는 --add 를 사용하세요.")
        sys.exit(1)

    n = write_blog_pages(OUT_DIR, site)
    write_sitemap(site["domain"])
    write_robots(site["domain"])
    print(f"블로그 페이지 {n}개 생성 (blog.html + 글 {n - 1}개)")
    print("index.html 홈 전체글·사이드바 갱신 완료")
    print("sitemap.xml, robots.txt 갱신 완료")
    print("\nStormkit 배포:")
    print("  GitHub/GitLab 푸시 후 app.stormkit.io 에서 저장소 연결")
    print("  Build command: (비움)  /  Output folder: .")
    print("  Cloud Free($0) 또는 Self-Hosted Free 시트 사용 가능")


if __name__ == "__main__":
    main()
