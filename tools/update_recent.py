"""홈 화면의 "오늘의 외국어 지문"과 "최근 블로그 글"을 각 사이트에서 읽어 index.html 에 채운다.

사용: python3 tools/update_recent.py   (바뀐 것이 없으면 파일을 그대로 둔다)
- 블로그: https://blog.wspace.ai.kr/rss.xml 의 최신 글 5개
- 외국어 읽기: https://read.wspace.ai.kr/<언어>/ 목록의 맨 위 지문
"""
import datetime as dt
import email.utils
import html
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READ = "https://read.wspace.ai.kr"
BLOG = "https://blog.wspace.ai.kr"
LANGS = [("en", "영어"), ("ja", "일본어")]


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "wspace-home"}), timeout=30) as r:
        return r.read().decode("utf-8")


def read_items():
    rows = []
    for code, name in LANGS:
        page = get(f"{READ}/{code}/")
        m = re.search(r'<a class="item" href="\./([0-9-]+)/".*?<span class="d">([^<]+)<span.*?<span class="t">([^<]+)</span>', page, re.S)
        if m:
            day, label, topic = m.groups()
            rows.append(f'    <a href="{READ}/{code}/{day}/"><span class="t">{name}: {topic}</span><span class="m">{label}</span></a>')
    return rows


def blog_items(n=5):
    rows = []
    for it in re.findall(r"<item>(.*?)</item>", get(f"{BLOG}/rss.xml"), re.S)[:n]:
        title = re.sub(r"<!\[CDATA\[|\]\]>", "", re.search(r"<title>(.*?)</title>", it, re.S).group(1)).strip()
        link = re.search(r"<link>(.*?)</link>", it, re.S).group(1).strip()
        pub = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        when = ""
        if pub:
            d = email.utils.parsedate_to_datetime(pub.group(1)).astimezone(dt.timezone(dt.timedelta(hours=9)))
            when = f"{d.year}년 {d.month}월 {d.day}일"
        rows.append(f'    <a href="{html.escape(link)}"><span class="t">{html.escape(html.unescape(title))}</span><span class="m">{when}</span></a>')
    return rows


def fill(page, key, rows):
    if not rows:
        return page  # 가져오지 못하면 기존 내용을 그대로 둔다
    block = f"<!-- {key}:START -->\n  <div class=\"list\">\n" + "\n".join(rows) + "\n  </div>\n  <!-- {key}:END -->".replace("{key}", key)
    return re.sub(rf"<!-- {key}:START -->.*?<!-- {key}:END -->", block, page, flags=re.S)


if __name__ == "__main__":
    path = ROOT / "index.html"
    old = path.read_text(encoding="utf-8")
    new = old
    for key, fn in (("READ", read_items), ("BLOG", blog_items)):
        try:
            new = fill(new, key, fn())
        except Exception as e:  # 한쪽 사이트가 일시적으로 안 열려도 다른 쪽은 갱신한다
            print(f"{key} skipped: {e}")
    if new != old:
        path.write_text(new, encoding="utf-8")
        # 홈 내용이 바뀌었으므로 사이트맵의 홈 lastmod 도 오늘(KST)로 맞춘다.
        today = dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d")
        sitemap = ROOT / "sitemap.xml"
        sitemap.write_text(re.sub(r"(<loc>https://www\.wspace\.ai\.kr/</loc><lastmod>)[^<]*", rf"\g<1>{today}",
                                  sitemap.read_text(encoding="utf-8")), encoding="utf-8")
        print("updated")
    else:
        print("no change")
