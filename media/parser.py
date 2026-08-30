import re

BILIBILI_RE = re.compile(r"(?:bilibili\.com/video/|bvid=)(BV[0-9A-Za-z]+)")
YOUTUBE_PATTERNS = [
    re.compile(r"youtube\.com/watch\?.*v=([0-9A-Za-z_-]{11})"),
    re.compile(r"youtu\.be/([0-9A-Za-z_-]{11})"),
    re.compile(r"youtube\.com/embed/([0-9A-Za-z_-]{11})"),
    re.compile(r"youtube\.com/shorts/([0-9A-Za-z_-]{11})"),
]


def parse_media_url(url):
    """从链接中识别平台与视频 ID；识别失败返回 None。"""
    url = (url or "").strip()
    match = BILIBILI_RE.search(url)
    if match:
        return "bilibili", match.group(1)
    for pattern in YOUTUBE_PATTERNS:
        match = pattern.search(url)
        if match:
            return "youtube", match.group(1)
    return None
