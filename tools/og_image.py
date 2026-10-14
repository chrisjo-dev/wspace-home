"""공유 미리보기 이미지(og.png, 1200x630)를 만든다. 사이트 소개 문구가 바뀌면 다시 실행한다.

사용: python3 tools/og_image.py   (글꼴은 english-reading 저장소의 Pretendard 를 쓴다)
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "english-reading" / "tools" / "fonts"
W, H, S = 1200, 630, 2  # 2배로 그린 뒤 줄여 글자 가장자리를 부드럽게 한다


def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"Pretendard-{weight}.otf"), size * S)


img = Image.new("RGB", (W * S, H * S), "#f2f4f6")
d = ImageDraw.Draw(img)
x = 96 * S
d.text((x, 150 * S), "wspace", font=font("ExtraBold", 120), fill="#191f28")
d.text((x, 300 * S), "매일 외국어 읽기, 기술 블로그,", font=font("SemiBold", 52), fill="#333d4b")
d.text((x, 370 * S), "브라우저 도구, 두뇌 게임", font=font("SemiBold", 52), fill="#333d4b")
colors = ["#3182f6", "#12ac7c", "#6b5cf6", "#e89a14"]
for i, c in enumerate(colors):
    cx = x + i * 72 * S
    d.rounded_rectangle((cx, 470 * S, cx + 52 * S, 522 * S), radius=16 * S, fill=c)
d.text((x + 300 * S, 478 * S), "www.wspace.ai.kr", font=font("SemiBold", 36), fill="#6b7684")
img.resize((W, H), Image.LANCZOS).save(ROOT / "og.png", optimize=True)
print("og.png", W, H)
