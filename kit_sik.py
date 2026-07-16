# -*- coding: utf-8 -*-
"""1·2과 형식 재사용 키트 — tokens.py 클래스를 그대로 쓰는 컴포넌트 모음.
   5~14과가 이 키트를 공유한다. (ch3 HTML 베끼기 금지)"""
exec(open('tokens.py').read())  # 색·CSS·footer 로드

# ── 페이지 공통 head (폰트 CDN + tokens CSS + 키트 보조 CSS) ──
EXTRA_CSS = f"""
/* 어휘 카드 (2열) */
.vgrid {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
.vcard {{ border:1px solid {HAIR}; border-radius:8px; padding:11px 15px; }}
.vcard .top {{ display:flex; align-items:baseline; gap:8px; margin-bottom:6px; }}
.vcard .w {{ font-family:'Noto Serif KR',serif; font-size:19px; font-weight:700; color:{DEEP}; }}
.vcard .hanja {{ font-size:13px; color:{SUB}; }}
.vcard .badge {{ margin-left:auto; }}
.vcard .mean {{ font-size:13.5px; color:{INK}; line-height:1.45; }}
.vcard .ex {{ font-size:12.5px; color:{SUB}; line-height:1.45; border-top:1px dashed {HAIR};
             padding-top:6px; margin-top:6px; }}
/* 원형 A·B·C / 번호 배지 (큰) */
.cbadge {{ display:inline-flex; width:30px; height:30px; border-radius:50%; background:{NAVY};
           color:#fff; font-weight:800; font-size:15px; align-items:center; justify-content:center; }}
.sechead {{ display:flex; align-items:center; gap:12px; margin-bottom:14px; }}
.sechead .t {{ font-weight:800; font-size:15.5px; }}
/* 워드뱅크 (음영 박스 중앙) */
.wbank {{ background:{TINT}; border-radius:6px; text-align:center; padding:12px;
          font-size:15px; font-weight:700; color:{NAVY}; letter-spacing:.06em; margin-bottom:16px; }}
/* 표지/장치 카드 그리드 */
.scard {{ border:1px solid {HAIR}; border-radius:8px; padding:14px 10px; text-align:center; }}
.scard .nm {{ font-weight:700; font-size:15px; color:{DEEP}; margin-top:8px; }}
.scard .han {{ font-size:11.5px; color:{SUB}; margin-top:2px; }}
.scard .ds {{ font-size:12px; color:{INK}; margin-top:4px; line-height:1.4; }}
/* 밑줄 빈칸 */
.bl {{ display:inline-block; border-bottom:1.3px solid #333; }}
/* 원문자(①㉠ 등) 크기 통일 — 한 폰트에서 렌더 */
.enc {{ font-family:'Noto Sans CJK KR',sans-serif; font-size:1em; }}
"""

HEAD = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Arimo:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
<style>
body {{ font-family:'Arimo','Liberation Sans','Noto Sans KR','Noto Sans CJK KR',sans-serif; }}
h2.sec, .formbig, .serif {{ font-family:'Noto Serif KR','Noto Serif CJK KR',serif !important; }}
.enc {{ font-family:'Noto Sans KR','Noto Sans CJK KR',sans-serif; }}
{EXTRA_CSS}</style>
</head>"""

FOOT_L = "산업안전한국어 · 2부 작업절차 제4과 절차 지시문 읽기"
def foot(n): return footer(FOOT_L, f"{n:02d}")

def blank(w=120): return f'<span class="bl" style="min-width:{w}px;">&nbsp;</span>'
def pill(t): return f'<div class="el"><span>{t}</span></div>'
def cbadge(ch): return f'<span class="cbadge">{ch}</span>'
def sechead(ch, title): return f'<div class="sechead">{cbadge(ch)}<span class="t">{title}</span></div>'

def head_sec(eyebrow, title):
    return f'<div class="eyebrow">{eyebrow}</div><h2 class="sec">{title}</h2>'

def vcard(word, lv, mean, ex, hanja=""):
    lvc = 'b' if lv=='기본' else 'a'
    h = f'<span class="hanja">{hanja}</span>' if hanja else ''
    return f'''<div class="vcard"><div class="top"><span class="w">{word}</span>{h}<span class="badge lv {lvc}">{lv}</span></div>
      <div class="mean">{mean}</div><div class="ex">{ex}</div></div>'''

def sitebox_img(img_svg, quote, source):
    """1·2과식: 그림+인용 가운데 정렬, 인용문은 본문체(세리프 X), 목표 문법만 <b>."""
    return f'''<div class="sitebox" style="margin-bottom:14px;">
      <div class="head">현장에서 만나기</div>
      <div class="body" style="display:flex;align-items:center;justify-content:center;gap:26px;padding:16px 24px;">
        <div style="flex:none;">{img_svg}</div>
        <div style="text-align:center;">
          <div style="font-size:18px;line-height:1.6;color:{INK};">"{quote}"</div>
          <div style="font-size:12px;color:{SUB};margin-top:7px;">{source}</div></div></div></div>'''

def connect(left, right, lw=140, rw=150, gap=96, rowgap=18):
    """1·2과식: 좌 항목(번호+말) 오른끝에 점 정렬, 우 항목 왼끝 점, 가운데 넓게.
       번호는 원문자 통일(.enc, Noto Sans CJK KR), 점은 작은 가운뎃점."""
    dot = '<span style="color:#8A929E;font-size:14px;line-height:1;flex:none;">&middot;</span>'
    def L(t):
        n,w = t.split(" ",1)
        return f'''<div style="display:flex;align-items:center;gap:9px;margin-bottom:{rowgap}px;width:{lw}px;">
          <span>{n}</span><span style="flex:1;">{w}</span>{dot}</div>'''
    def R(t):
        n,w = t.split(" ",1)
        return f'''<div style="display:flex;align-items:center;gap:10px;margin-bottom:{rowgap}px;width:{rw}px;">
          {dot}<span>{n}</span><span>{w}</span></div>'''
    return f'<div style="display:flex;gap:{gap}px;">' + \
           f'<div>{"".join(L(t) for t in left)}</div><div>{"".join(R(t) for t in right)}</div></div>'
