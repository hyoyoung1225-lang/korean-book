# -*- coding: utf-8 -*-
"""build_ch12.py — 산업안전한국어 제12과 「예방 제안」 (4부 사례 · 14주차 · Q12 · 과제③ 수합 · 기말 공방)
   기반: build_ch7.py 검증 완료 오버라이드(표제어 돋움·connect enc 내장·전각 밑줄·1과식 gcard 헤더·정리 틀)
   내용 확정: 2026-07-17 (진행DB 8과 행·색인 15건·오류기록 11번)
   실물: 작업중지권 행사 절차 안내문(기업 사례 재구성) + 위험 상황 대화(제조 소재)
"""
import sys
sys.path.insert(0, '/home/claude/sik')
exec(open('/home/claude/sik/kit_sik_v3_UPLOAD_ME.py').read())

OVERRIDE_CSS = f"""
.vcard .w{{font-family:'Arimo','Noto Sans KR','Noto Sans CJK KR',sans-serif !important;
  font-size:18px; font-weight:800; color:{DEEP};}}
.vcard .ex b{{color:{NAVY};}}
.vcard{{padding:13px 16px;}}
table.cellwide td{{padding:14px 12px !important;}}
"""
HEAD = HEAD.replace('</style>\n</head>', OVERRIDE_CSS + '</style>\n</head>')

def blank(n=8):
    return '<span style="letter-spacing:0;">' + '＿' * n + '</span>'

def connect(left, right, lw=140, rw=150, rowgap=18):
    dot = '<span style="color:#8A929E;font-size:14px;line-height:1;flex:none;">&middot;</span>'
    def L(t):
        n, w = t.split(" ", 1)
        return (f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:{rowgap}px;width:{lw}px;">'
                f'<span class="enc">{n}</span><span style="flex:1;">{w}</span>{dot}</div>')
    def R(t):
        n, w = t.split(" ", 1)
        return (f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:{rowgap}px;width:{rw}px;">'
                f'{dot}<span class="enc">{n}</span><span>{w}</span></div>')
    return ('<div style="display:flex;justify-content:space-between;">'
            f'<div>{"".join(L(t) for t in left)}</div><div>{"".join(R(t) for t in right)}</div></div>')

FOOT_L = "산업안전한국어 · 4부 사례 제12과 예방 제안"
def foot(n): return footer(FOOT_L, f"{n:02d}")
def enc(t): return f'<span class="enc">{t}</span>'
PAGES = []
def page(label, body):
    PAGES.append(f'<div class="page" data-document-role="page" data-label="{label}">{body}</div>')





# ═══ 픽토 4종 — 12과 (제안서·전구·수칙 체크·악수/졸업) ═══
def picto_doc():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <rect x="30" y="22" width="40" height="56" rx="3" fill="#fff"/>
      <line x1="37" y1="34" x2="63" y2="34" stroke="{NAVY}" stroke-width="4"/>
      <line x1="37" y1="44" x2="63" y2="44" stroke="{NAVY}" stroke-width="4"/>
      <path d="M52 66 l6 6 l10 -12" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/></svg>'''
def picto_bulb():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 22 a19 19 0 0 1 10 35 v8 h-20 v-8 a19 19 0 0 1 10 -35 Z" fill="#fff"/>
      <line x1="43" y1="72" x2="57" y2="72" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
      <line x1="45" y1="79" x2="55" y2="79" stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg>'''
def picto_check3():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <g stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none">
        <rect x="26" y="26" width="12" height="12" rx="2"/><path d="M28 32 l4 4 l7 -9"/>
        <rect x="26" y="46" width="12" height="12" rx="2"/><path d="M28 52 l4 4 l7 -9"/>
        <rect x="26" y="66" width="12" height="12" rx="2"/></g>
      <line x1="46" y1="32" x2="74" y2="32" stroke="#fff" stroke-width="5"/>
      <line x1="46" y1="52" x2="74" y2="52" stroke="#fff" stroke-width="5"/>
      <line x1="46" y1="72" x2="74" y2="72" stroke="#fff" stroke-width="5"/></svg>'''
def picto_grad():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 30 L78 42 L50 54 L22 42 Z" fill="#fff"/>
      <path d="M36 48 v14 q14 10 28 0 v-14" fill="none" stroke="#fff" stroke-width="5"/>
      <line x1="74" y1="44" x2="74" y2="62" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>'''

G_TALK = f'<svg width="30" height="30" viewBox="0 0 100 100"><path d="M14 22 h72 v44 h-40 l-16 16 v-16 h-16 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/><line x1="30" y1="38" x2="70" y2="38" stroke="{NAVY}" stroke-width="7"/><line x1="30" y1="52" x2="58" y2="52" stroke="{NAVY}" stroke-width="7"/></svg>'
G_AA   = f'<span style="font-family:\'Noto Serif KR\',serif;font-size:24px;font-weight:900;color:{NAVY};">Aa</span>'
G_BOOK = f'<svg width="30" height="30" viewBox="0 0 100 100"><path d="M50 26 q-16 -10 -34 -4 v52 q18 -6 34 4 q16 -10 34 -4 v-52 q-18 -6 -34 4 Z M50 26 v52" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/></svg>'
G_TARGET = f'<svg width="19" height="19" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="{NAVY}" stroke-width="10"/><circle cx="50" cy="50" r="16" fill="{NAVY}"/></svg>'
G_BULB = f'<svg width="17" height="17" viewBox="0 0 100 100"><path d="M50 12 a26 26 0 0 1 14 48 v10 h-28 v-10 a26 26 0 0 1 14 -48 Z" fill="none" stroke="{NAVY}" stroke-width="9"/><line x1="40" y1="82" x2="60" y2="82" stroke="{NAVY}" stroke-width="8"/></svg>'
G_SHIELD = f'<svg width="15" height="15" viewBox="0 0 100 100"><path d="M50 8 L86 20 V52 q0 28 -36 40 q-36 -12 -36 -40 V20 Z" fill="{NAVY}"/><path d="M36 50 l10 10 l20 -22" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/></svg>'

def klass_icon(g):
    return f'<div style="width:62px;height:62px;border-radius:50%;background:{TINT};display:flex;align-items:center;justify-content:center;margin:0 auto 10px auto;">{g}</div>'
def kcol(g, pilltxt, pillbg, c1, c2):
    return f'''<div style="width:200px;text-align:center;">{klass_icon(g)}
      <div><span style="display:inline-block;background:{pillbg};color:#fff;font-size:12.5px;font-weight:800;height:27px;line-height:27px;padding:0 16px;border-radius:14px;">{pilltxt}</span></div>
      <div style="font-size:12px;color:{SUB};line-height:1.6;margin-top:9px;">{c1}<br>{c2}</div></div>'''
CHEV = '<div style="color:#C4CBD7;font-size:15px;margin-top:26px;">〉</div>'

dobira = f"""
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid {NAVY};padding-bottom:11px;">
    <span style="font-size:13px;font-weight:700;letter-spacing:.5em;color:{INK};">산업안전한국어</span>
    <span style="font-size:13px;font-weight:800;letter-spacing:.14em;color:{NAVY};">4부 · 사례</span>
  </div>
  <div style="display:flex;gap:26px;margin-top:34px;">
    <div style="flex:1;padding-top:20px;">
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:118px;font-weight:900;color:{NAVY};line-height:.95;">12</div>
      <div style="margin-top:14px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:12.5px;font-weight:800;letter-spacing:.34em;height:30px;line-height:30px;padding:0 12px 0 20px;">제 12 과</span></div>
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:46px;font-weight:900;color:{INK};margin-top:22px;">예방 제안</div>
    </div>
    <div style="flex:none;width:322px;height:462px;position:relative;background:#E7EDF6;overflow:hidden;">
      <div style="position:absolute;top:120px;left:24px;width:56px;height:400px;background:#D8E1EF;"></div>
      <div style="position:absolute;top:230px;right:16px;width:70px;height:300px;background:#D1DBEC;"></div>
      <div style="position:absolute;top:-70px;left:150px;width:52px;height:640px;background:{NAVY};transform:rotate(16deg);"></div>
      <div style="position:absolute;top:52px;left:34px;right:34px;background:#fff;border-radius:16px;box-shadow:0 10px 26px rgba(20,35,80,.16);padding:26px 20px;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;justify-items:center;">
          {picto_bulb()}{picto_doc()}{picto_check3()}{picto_grad()}</div></div>
    </div>
  </div>
  <div style="display:flex;gap:26px;margin-top:40px;">
    <div style="flex:1.06;">
      <div style="display:flex;align-items:center;gap:9px;margin-bottom:16px;">
        {G_TARGET}<span style="font-size:16px;font-weight:800;color:{INK};">학습 목표</span>
        <div style="flex:1;border-top:1px solid {HAIR};"></div></div>
      <div style="display:flex;flex-direction:column;gap:13px;font-size:14.5px;line-height:1.6;">
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">1</span><span style="padding-top:2px;">위험이 <b>생기지 않도록</b> 막는 개선을 제안합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">2</span><span style="padding-top:2px;">안전 개선 <b>제안서</b>를 격식에 맞게 씁니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">3</span><span style="padding-top:2px;">배운 문형을 모아 <b>기말 안내문</b>을 완성합니다.</span></div>
      </div>
    </div>
    <div style="flex:1;background:#EDF2FA;border-radius:12px;padding:20px 24px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px;">
        {G_BULB}<span style="font-size:15px;font-weight:800;color:{INK};">생각해 보기</span></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">1과부터 지금까지, 가장 기억에 남는 위험은 무엇입니까?</div>
      <div style="border-top:1px dashed #C9D2E2;margin:11px 0;"></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">내가 회사에 하나를 제안할 수 있다면, 무엇을 바꾸겠습니까?</div>
    </div>
  </div>
  <div style="display:flex;justify-content:center;align-items:flex-start;gap:4px;margin-top:42px;">
    {kcol(G_TALK,'1교시 · 어휘',NAVY,'핵심 어휘 12개 + 연습','제안의 말')}
    {CHEV}
    {kcol(G_AA,'2교시 · 문형',LIGHT,'-지 않도록 · 제안합니다','전 과 문형 종합')}
    {CHEV}
    {kcol(G_BOOK,'3교시 · 쓰기',DEEP,'제안서 완성본 읽기','기말 안내문 공방 + 정리')}
  </div>
  <div style="position:absolute;top:{FOOTER_Y}px;left:64px;right:64px;border-top:1px solid {HAIR};padding-top:12px;display:flex;justify-content:space-between;align-items:center;">
    <span style="display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800;color:{INK};">
      {G_SHIELD} 읽는 사람에서, 제안하는 사람으로.</span>
    <span style="font-size:13px;font-weight:800;color:{NAVY};">01</span>
  </div>"""
page("도비라", dobira)

# ═══ 2쪽 어휘 12 ═══
V = [
 ("예방","기본","일이 생기기 전에 미리 막는 것입니다.","<b>예방</b>이 최고의 대책입니다."),
 ("개선","기본","나쁜 점을 고쳐서 좋게 만드는 것입니다.","작업 방법을 <b>개선</b>하였습니다."),
 ("제안","기본","좋은 생각을 내놓는 것입니다.","덮개 설치를 <b>제안</b>합니다."),
 ("건의","기본","회사에 공식적으로 제안하는 것입니다.","안전 교육 확대를 <b>건의</b>하였습니다."),
 ("효과","기본","좋은 결과입니다.","기대 <b>효과</b>를 함께 씁니다."),
 ("수칙","기본","지켜야 할 규칙입니다.","안전 <b>수칙</b>을 실천합니다."),
 ("실천","기본","아는 것을 실제로 하는 것입니다.","아는 것보다 <b>실천</b>이 중요합니다."),
 ("안전","기본","위험이 없는 상태입니다. 이 수업의 이름입니다.","나의 제안이 모두의 <b>안전</b>이 됩니다."),
 ("방안","심화","'방법'의 문서 말입니다.","개선 <b>방안</b>을 세 가지 적었습니다."),
 ("수립","심화","계획이나 대책을 세우는 것입니다.","재발 방지 대책을 <b>수립</b>합니다."),
 ("발굴","심화","숨어 있는 것을 찾아내는 것입니다.","위험 요인을 <b>발굴</b>하였습니다."),
 ("정착","심화","제도가 자리를 잡는 것입니다.","안전 문화가 <b>정착</b>되었습니다."),
]
v_cards = ''.join(vcard(w, lv, m, e) for w, lv, m, e in V)
p2 = f"""{head_sec('1교시 · 어휘', '핵심 어휘 12')}
  <div style="display:flex; align-items:center; gap:8px; font-size:13px; color:{SUB}; margin-bottom:16px;">
    <span class="lv b">기본</span><span>모든 학생 필수</span>
    <span class="lv a" style="margin-left:10px;">심화</span><span>제안서·보고서의 문어 표현 — 읽고 이해할 수 있으면 충분합니다.</span></div>
  <div class="vgrid" style="gap:16px;">{v_cards}</div>
  {foot(2)}"""
page("핵심어휘", p2)

# ═══ 3쪽 어휘 연습 ═══
p3 = f"""{head_sec('1교시 · 어휘', '어휘 연습')}
  {sechead('A','알맞은 단어를 골라 빈칸을 채우십시오.')}
  <div class="wbank" style="margin-bottom:22px;">방안 · 발굴 · 수립 · 정착</div>
  <div class="left" style="font-size:15px; line-height:2.75; margin-bottom:{SP_XL}px;">
    ① 숨어 있는 위험 요인을 {blank(4)}하였습니다.<br>
    ② 개선 {blank(4)}을 세 가지 제안합니다.<br>
    ③ 재발 방지 대책을 {blank(4)}합니다.<br>
    ④ 제안 제도가 회사에 {blank(4)}되었습니다.</div>
  {sechead('B','짝이 되는 말을 선으로 연결하십시오.')}
  <div style="margin-bottom:{SP_XL}px;">
  {connect(
    ["① 개선을", "② 수칙을", "③ 대책을", "④ 요인을", "⑤ 효과를"],
    ["㉠ 발굴하다", "㉡ 제안하다", "㉢ 실천하다", "㉣ 기대하다", "㉤ 수립하다"],
    lw=160, rw=230, rowgap=34)}
  </div>
  {sechead('C','B에서 연결한 표현 중 두 개를 골라 문장을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.4;">
    ① {blank(40)}<br>
    ② {blank(40)}</div>
  {foot(3)}"""
page("어휘연습", p3)

# ═══ 4쪽 개념 — 제안의 세 칸 ═══
def zone(n, t, sub, d):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:46px 24px; display:flex; gap:16px; align-items:flex-start;">
      <span class="enc" style="margin-top:2px;">{n}</span>
      <div style="flex:1;">
        <div style="font-weight:800; font-size:16px; color:{DEEP};">{t} <span style="font-size:12.5px; color:{SUB}; font-weight:500;">{sub}</span></div>
        <div style="font-size:14px; line-height:1.65; margin-top:5px;">{d}</div></div></div>'''

p4 = f"""{head_sec('1교시 · 어휘', '제안서의 세 칸')}
  <div class="prose" style="margin-bottom:26px;">안전 개선 제안서는 세 칸으로 이루어집니다. 10과에서 읽은 사례의 세 구획과 순서가 같습니다 — 읽던 틀이 쓰는 틀이 됩니다.</div>
  <div style="display:flex; flex-direction:column; gap:34px; margin-bottom:{SP_XL}px;">
    {zone('①','위험 요인','— 무엇이 위험한가','내가 발굴한 위험을 씁니다. "N이/가 -(으)ㄹ 우려가 있다"(1과 공식)로 씁니다.')}
    {zone('②','개선 방안','— 어떻게 막을 것인가','위험이 생기지 않도록 무엇을 할지 씁니다. "-(으)ㄹ 것을 제안합니다"로 끝냅니다.')}
    {zone('③','기대 효과','— 무엇이 좋아지는가','제안이 실행되면 어떤 결과가 오는지 씁니다. "그 결과"(10과)로 이으면 됩니다.')}
  </div>
  <div class="tintbox">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">마지막 과입니다 — 읽는 사람에서 제안하는 사람으로</div>
    <div style="font-size:14.5px; line-height:1.85;">1부에서 표지를 읽었고, 2부에서 절차를 따랐고, 3부에서 권리를 썼고, 4부에서 사례를 분석했습니다. 이제 마지막 한 걸음 — 내가 회사에 <b>안전을 제안</b>합니다.</div>
  </div>
  {foot(4)}"""
page("개념", p4)

# ═══ 5쪽 확장① — 비슷한 말 구별 ═══
p5 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ① — 비슷한 말 구별')}
  <div class="prose" style="margin-bottom:24px;">이 교재에서 배운 '막는 말'들이 모두 모였습니다. 뜻이 비슷해 보여도 자리가 다릅니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:110px;height:16px;">말</th><th style="width:150px;">언제</th><th>예</th></tr>
    <tr><td><b>예방</b></td><td>일이 생기기 전에</td><td>사고를 <b>예방</b>하는 교육</td></tr>
    <tr><td><b>방지</b> <span style="font-size:12px;color:{SUB};">(10과)</span></td><td>같은 일이 다시 없게</td><td>재발 <b>방지</b> 대책</td></tr>
    <tr><td><b>대책</b> <span style="font-size:12px;color:{SUB};">(10과)</span></td><td>막는 방법 그 자체</td><td><b>대책</b>을 수립하다</td></tr>
    <tr><td><b>개선</b></td><td>지금 것을 고칠 때</td><td>작업 방법 <b>개선</b></td></tr>
  </table>
  {sechead('A','알맞은 말을 고르십시오.')}
  <div class="left" style="font-size:15px; line-height:4.0; margin-bottom:{SP_XL}px;">
    ① 같은 사고가 다시 나지 않게 하는 것 → ( 예방 · 재발 방지 )<br>
    ② 낡은 설비를 새것으로 바꾸는 것 → ( 개선 · 정착 )</div>
  {sechead('B','문장을 완성해 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:4.05;">
    ① 안전 교육은 사고를 미리 막는 {blank(4)} 활동입니다.<br>
    ② 재발을 막기 위한 {blank(4)}을 수립하였습니다.</div>
  {foot(5)}"""
page("어휘확장1", p5)

# ═══ 6쪽 확장② — 함께 쓰는 말 ═══
def collo(a, b, m, e):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:24px 18px;">
      <div style="font-size:17px; font-weight:800; color:{DEEP};">{a} <span style="color:{LIGHT};">+</span> {b}</div>
      <div style="font-size:13.5px; margin-top:5px; line-height:1.6;">{m}</div>
      <div style="font-size:12.5px; color:{SUB}; border-top:1px dashed {HAIR}; margin-top:12px; padding-top:11px; line-height:1.7;">{e}</div></div>'''

p6 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ② — 함께 쓰는 말')}
  <div class="prose" style="margin-bottom:24px;">제안서의 말도 짝이 정해져 있습니다. 네 짝이면 제안서의 세 칸을 다 채울 수 있습니다.</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:26px; margin-bottom:{SP_XL}px;">
    {collo('요인을','발굴하다','숨은 위험을 찾아내는 것입니다. (요인: 3과)','위험 <b>요인을 발굴</b>하였습니다.')}
    {collo('개선을','제안하다','고칠 것을 내놓는 것입니다.','덮개 설치 <b>개선을 제안</b>합니다.')}
    {collo('대책을','수립하다','막을 방법을 세우는 것입니다. (대책: 10과)','재발 방지 <b>대책을 수립</b>합니다.')}
    {collo('수칙을','실천하다','규칙을 실제로 지키는 것입니다.','안전 <b>수칙을 실천</b>합니다.')}
  </div>
  {sechead('A','알맞은 짝을 골라 문장을 완성하십시오.')}
  <div class="wbank" style="margin-bottom:26px;">발굴 · 제안 · 수립 · 실천</div>
  <div class="left" style="font-size:15px; line-height:4.05;">
    ① 점검에서 위험 요인 두 건을 {blank(4)}하였습니다.<br>
    ② 통행로 구분선 설치를 {blank(4)}합니다.<br>
    ③ 원인에 맞는 대책을 {blank(4)}하였습니다.<br>
    ④ 배운 수칙을 현장에서 {blank(4)}합니다.</div>
  {foot(6)}"""
page("어휘확장2", p6)

print(f"[1/3] {len(PAGES)}쪽")

# ═══ 7~9쪽 문형 ═══
def pillrow(*ps):
    return '<div style="display:flex; gap:8px; margin:10px 0 4px 0;">' + ''.join(pill(t) for t in ps) + '</div>'
def gcard(num, title, site_img, quote, source, mean_html, comp_pill, comp_html, err_html, drill_html, wide=True, lv='심화', comb='동사'):
    sb, mm, cm, dl = (24, 16, 22, 2.75) if wide else (28, 20, 26, 3.05)
    return f"""<div style="display:flex; align-items:center; gap:13px; margin-bottom:18px;">
    <span class="num">{num}</span>
    <span class="formbig" style="white-space:nowrap;">{title}</span>
    <span class="lv {'b' if lv=='기본' else 'a'}">{lv}</span>
    <span style="margin-left:auto; font-size:13.5px; color:{SUB};">결합: <b style="color:{INK};">{comb}</b></span></div>
  <div style="margin-bottom:{sb}px;">{sitebox_img(site_img, quote, source)}</div>
  {pillrow('의미와 쓰임')}
  <div class="prose" style="margin-bottom:{mm}px;">{mean_html}</div>
  {pillrow(comp_pill)}
  <div style="font-size:14.5px; line-height:{1.8 if wide else 1.7}; margin-bottom:{mm}px;">{comp_html}</div>
  {pillrow('자주 하는 오류')}
  <div class="caution" style="font-size:14.5px; line-height:{2.0 if wide else 1.85}; margin-bottom:{cm}px;">{err_html}</div>
  {pillrow('연습')}
  <div class="drill left" style="font-size:15px; line-height:{dl};">{drill_html}</div>"""

IMG_COVER = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <circle cx="40" cy="58" r="15" fill="none" stroke="{NAVY}" stroke-width="6"/>
  <rect x="20" y="36" width="44" height="10" rx="5" fill="{NAVY}"/>
  <path d="M70 28 q14 8 8 24" fill="none" stroke="{SUB}" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 7"/>
  <path d="M72 60 q8 -5 14 2 l-3 14 h-12 Z" fill="#C8CFDC"/></svg>'''
IMG_PROP = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <rect x="12" y="12" width="76" height="76" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="5"/>
  <rect x="20" y="20" width="60" height="16" fill="{NAVY}"/>
  <text x="50" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">안전 개선 제안서</text>
  <line x1="22" y1="48" x2="78" y2="48" stroke="{HAIR}" stroke-width="4"/>
  <line x1="22" y1="60" x2="78" y2="60" stroke="{HAIR}" stroke-width="4"/>
  <text x="50" y="80" text-anchor="middle" font-size="11.5" font-weight="bold" fill="{NAVY}">…제안합니다</text></svg>'''
IMG_SUM = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <circle cx="30" cy="30" r="12" fill="none" stroke="{NAVY}" stroke-width="4"/><text x="30" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="{NAVY}">1</text>
  <circle cx="70" cy="30" r="12" fill="none" stroke="{NAVY}" stroke-width="4"/><text x="70" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="{NAVY}">7</text>
  <circle cx="30" cy="70" r="12" fill="none" stroke="{NAVY}" stroke-width="4"/><text x="30" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="{NAVY}">10</text>
  <circle cx="70" cy="70" r="12" fill="{NAVY}"/><text x="70" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#fff">12</text>
  <g stroke="{HAIR}" stroke-width="4"><line x1="40" y1="34" x2="60" y2="66"/><line x1="42" y1="30" x2="58" y2="30"/><line x1="40" y1="66" x2="58" y2="70"/><line x1="30" y1="42" x2="30" y2="58"/></g></svg>'''

p7 = gcard('1', '-지 않도록', IMG_COVER,
  '손이 말려들<b>지 않도록</b> 안전덮개를 설치한다.', '개선 방안 문장',
  """나쁜 일이 생기는 것을 막는 <b>목적</b>을 나타냅니다. 예방의 문형입니다 — 앞에는 막고 싶은 위험(피동), 뒤에는 내가 할 일이 옵니다.""",
  '비교 · 비슷한 꼴',
  f"""· 말려들<b>지 않도록</b> 덮개를 설치한다 — 위험을 <b>막는 목적</b><br>
      · 확인하<b>도록</b> 한다 — 하게 만드는 목적 (규정의 말)<br>
      · 4과에서 배운 -지 않은 채 — '안 한 상태로'라는 뜻입니다. 꼴이 비슷하니 주의합니다.""",
  f"""<span class="x">✗ 손이 말려들지 않도록 위험합니다.</span><br>
      ○ 손이 말려들지 않도록 <b>덮개를 설치합니다</b>.<br>
      <span style="font-size:13px; color:{SUB};">'-지 않도록' 뒤에는 막기 위해 하는 행동이 와야 합니다.</span>""",
  f"""{enc('①')} 미끄러지다 → 미끄러지{blank(5)} 방지 매트를 깝니다.<br>
      {enc('②')} 떨어지다 → 화물이 {blank(7)} 결속합니다.<br>
      {enc('③')} 재발하다 → 같은 사고가 {blank(7)} 대책을 수립합니다.""", lv='기본')
page("문형1", p7 + foot(7))

p8 = gcard('2', '-(으)ㄹ 것을 제안합니다', IMG_PROP,
  '동력전달부에 안전덮개를 설치<b>할 것을 제안합니다</b>.', '안전 개선 제안서',
  """제안서의 끝 문장입니다. 하고 싶은 일을 <b>-(으)ㄹ 것</b>으로 묶어 '제안합니다'에 얹습니다. 회사에 내는 문서의 격식입니다.""",
  '비교 · 명사로 만드는 세 계단',
  f"""8과 — 작동 <b>여부</b>를 확인한다 (명사 하나로)<br>
      9과 — 손가락이 끼<b>임</b> (문장 끝을 명사로)<br>
      12과 — 설치<b>할 것을</b> 제안합니다 (할 일을 명사로) — 계단의 마지막입니다.<br>
      말할 때는? "덮개를 설치하<b>는 게 어떻겠습니까</b>?" — 회의의 말입니다.""",
  f"""<span class="x">✗ 안전덮개를 설치를 제안합니다.</span><br>
      ○ 안전덮개를 설치<b>할 것을</b> 제안합니다. / 안전덮개 <b>설치를</b> 제안합니다.<br>
      <span style="font-size:13px; color:{SUB};">동사를 살리려면 -(으)ㄹ 것을, 명사로 하려면 조사 하나만 씁니다.</span>""",
  f"""{enc('①')} 통행로에 구분선을 긋다 → 구분선을 {blank(6)} 제안합니다.<br>
      {enc('②')} 조명을 밝게 바꾸다 → 조명을 밝게 {blank(6)} 제안합니다.<br>
      {enc('③')} (말로) 안전화를 지급하다 → 안전화를 지급하{blank(8)}?""")
page("문형2", p8 + foot(8))

p9 = gcard('3', '전 과 문형 종합 — 안내문 공식', IMG_SUM,
  '끼일 우려가 있으니, 전원을 차단한 후 작업하십시오.', '이 교재의 대표 문장',
  """새 문형이 없습니다. 열두 과의 문형이 한 문장에 모입니다. <b>[무엇]이 [피동]-(으)ㄹ 우려가 있으니, [행동]하십시오.</b> 1과의 공식이 이 교재의 처음이자 끝입니다.""",
  '비교 · 기말시험의 네 유형',
  f"""A 표지 → 문장 — "출입 금지" → 출입이 금지되어 있습니다.<br>
      B 구어 → 격식 — "미끄러우니까 조심하세요" → 미끄러질 우려가 있으니 주의하십시오.<br>
      C 상황 → 안내문 — 사진을 보고 [우려]+[행동] 두 문장.<br>
      D 실물 독해 — 안내문·서식에서 금지·조건 찾기.""",
  f"""<span class="x">✗ 끼일 우려가 있으니까 조심하세요.</span> (구어)<br>
      ○ 끼일 우려가 있으니 <b>주의하십시오</b>. (격식 — 시험의 말)<br>
      <span style="font-size:13px; color:{SUB};">3과에서 배운 구별입니다. 시험 유형 B가 바로 이것입니다.</span>""",
  f"""{enc('①')} (A형) "안전모 착용" 표지 → 안전모를 반드시 {blank(8)}.<br>
      {enc('②')} (B형) "여기 물건 쌓지 마세요" → 적재를 {blank(8)}.<br>
      {enc('③')} (C형) 회전부 + 장갑 → 장갑이 {blank(4)} 우려가 있으니 {blank(10)}.""", wide=False, lv='기본')
page("문형3", p9 + foot(9))

# ═══ 10쪽 문형 종합 ═══
p10 = f"""{head_sec('2교시 · 문형', '문형 종합')}
  {sechead('A','두 문형을 이어 제안서 문장을 만드십시오.')}
  <div class="tintbox" style="margin-bottom:16px; font-size:14.5px; line-height:2.0;"><b>보기</b> &nbsp; 손이 말려들다 + 덮개를 설치하다<br>→ 손이 말려들<b>지 않도록</b> 덮개를 설치<b>할 것을 제안합니다</b>.</div>
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.0;">
    {enc('①')} 화물이 떨어지다 + 결속 규정을 만들다<br>
    → {blank(34)}<br>
    {enc('②')} 사람이 미끄러지다 + 방지 매트를 깔다<br>
    → {blank(34)}</div>
  {sechead('B','기말 유형으로 바꾸십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.95;">
    {enc('①')} (B형) "지게차 올 때는 비켜 주세요" → 지게차 접근 시 {blank(12)}.<br>
    {enc('②')} (A형) "화기 엄금" 표지 → 화기 사용이 {blank(8)}.</div>
  {sechead('C','미니 쓰기 — 나의 제안 한 문장.')}
  <div class="drill left" style="font-size:15px; line-height:3.3;">
    내 실습장(일터)에서 바꾸고 싶은 것 하나를 골라 보기의 꼴로 쓰십시오.<br>
    {blank(34)}<br>
    {blank(34)}</div>
  {foot(10)}"""
page("문형종합", p10)

print(f"[2/3] {len(PAGES)}쪽")

# ═══ 11쪽 실물 — 제안서 기입 완성본 ═══
FILL = f'color:{NAVY};font-weight:800;'
def frow(label, val, lw=118):
    return (f'<div style="display:flex;border-bottom:1px solid {HAIR};">'
            f'<div style="flex:none;width:{lw}px;background:#F4F6FA;padding:22px 10px;font-size:12.5px;color:{INK};">{label}</div>'
            f'<div style="flex:1;padding:22px 12px;font-size:13.5px;line-height:2.0;"><span style="{FILL}">{val}</span></div></div>')

p11 = f"""{head_sec('3교시 · 쓰기', '실물 자료 읽기 — 기입이 끝난 제안서')}
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[가] 안전 개선 제안서 — 기입 완성본 <span style="font-weight:500;color:{SUB};font-size:12px;">· 파란 글씨 = 기입한 내용</span></div>
  <div style="border:1.5px solid {NAVY};border-radius:6px;overflow:hidden;margin-bottom:8px;">
    <div style="background:{NAVY};color:#fff;text-align:center;font-weight:800;font-size:13.5px;padding:9px;">안전 개선 제안서</div>
    {frow('제안자 · 부서','응우옌 반 안 · 제2공장 포장팀')}
    {frow('제안 일자','2026년 6월 10일')}
    {frow('위험 요인','포장 라인 컨베이어의 동력전달부가 노출되어 있음. 작업 중 장갑이나 소매가 <b>말려들 우려가 있음</b>.')}
    {frow('개선 방안','동력전달부에 안전덮개를 설치<b>할 것을 제안합니다</b>. 또한 컨베이어 주변에 경고 표지를 부착하여 접근하<b>지 않도록</b> 안내합니다.')}
    {frow('기대 효과','감김 사고를 예방할 수 있음. <b>그 결과</b> 안전한 작업 환경이 정착됨.')}
    <div style="padding:20px 12px;font-size:13.5px;text-align:center;">위와 같이 개선을 제안합니다. &nbsp; 제안자: <span style="{FILL}">응우옌 반 안</span> (서명)</div>
  </div>
  <div class="lnote" style="font-size:11.5px;color:{SUB};margin-bottom:26px;">KOSHA 「안전제안에 관한 지침」의 제안 제도를 교육용 서식으로 재구성함 · 인물은 가상(9과의 응우옌 반 안 — 다쳤던 사람이 제안하는 사람이 되었습니다)</div>
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[나] 제안은 실제로 회사를 바꿉니다</div>
  <div class="tintbox" style="font-size:13.5px;line-height:2.5;padding:34px 30px;">
    한 사업장에서는 근로자 제안 제도로 한 해 <b>215건</b>의 제안이 접수되어 <b>70% 이상</b>이 개선되었고, 무재해로 이어졌습니다. 제안서의 세 칸을 채울 수 있는 사람 — 그 사람이 현장을 바꿉니다.</div>
  {foot(11)}"""
page("실물자료읽기", p11)

# ═══ 12쪽 읽고 답하기 ═══
p12 = f"""{head_sec('3교시 · 쓰기', '읽고 답하기')}
  <div class="tintbox" style="margin-bottom:{SP_M}px; font-size:14px;">11쪽의 제안서를 다시 보면서 답하십시오.</div>
  {sechead('A','기본 — 맞으면 ○, 틀리면 ✗를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.75;">
    {enc('①')} 제안자는 위험 요인을 1과의 우려 공식으로 썼다. ( {blank(2)} )<br>
    {enc('②')} 개선 방안은 한 가지만 써야 한다. ( {blank(2)} )<br>
    {enc('③')} 기대 효과에는 제안이 가져올 좋은 결과를 쓴다. ( {blank(2)} )</div>
  {sechead('B','심화 — 제안서에서 찾아 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.7;">
    {enc('①')} '개선 방안' 칸에서 이 과의 문형 두 개를 찾아 쓰십시오.<br>
    → {blank(12)} · {blank(12)}<br>
    {enc('②')} 이 제안서와 10과 사례 [나]는 같은 위험을 다룹니다. 무슨 사고입니까?<br>
    → {blank(8)}</div>
  {sechead('C','확장 — 생각을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    사고가 난 후의 사례 보고서와, 사고가 나기 전의 제안서 — 어느 쪽이 더 좋은 문서입니까? 이유를 쓰십시오.<br>
    → {blank(26)}<br>
    {blank(30)}</div>
  {foot(12)}"""
page("읽고답하기", p12)

# ═══ 13쪽 연습 — 제안서 부분 기입 ═══
CARD_B = f'''<div style="border:1.5px solid {LIGHT};border-radius:9px;padding:16px 20px;margin-bottom:18px;">
  <div style="font-weight:800;color:{DEEP};font-size:13.5px;margin-bottom:7px;">연습 상황 카드 — 이 위험으로 제안서를 쓰십시오</div>
  <div style="font-size:13.5px;line-height:1.9;">제1공장 자재 창고 앞 통로에 상자가 자주 쌓여 있습니다(3과에서 본 그 통로입니다). 사람이 걸려 넘어질 위험이 있고, 비상구로 가는 길이 막힙니다.</div></div>'''

p13 = f"""{head_sec('3교시 · 쓰기', '연습 — 제안서에 기입하기')}
  {CARD_B}
  {sechead('A','제안서의 세 칸을 채우십시오.')}
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:120px;height:6px;">칸</th><th>내용</th></tr>
    <tr><td>위험 요인</td><td>통로에 상자가 {blank(6)} 있어, 사람이 {blank(6)} 우려가 있음</td></tr>
    <tr><td>개선 방안</td><td>통로에 적재를 {blank(4)}하고, 자재 보관 구역을 {blank(5)} 것을 제안합니다</td></tr>
    <tr><td>기대 효과</td><td>넘어짐 사고를 {blank(4)}할 수 있음</td></tr>
  </table>
  {sechead('B','제목을 만드십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.5;">
    {enc('①')} 이 제안서의 제목(10과의 꼴): 통로 적재{blank(5)} 넘어짐 예방 제안</div>
  {sechead('C','말로 제안해 보십시오.')}
  <div class="drill left" style="font-size:15px; line-height:3.7;">
    (회의에서) 통로의 상자를 치우{blank(10)}?<br>
    (문서에서) 자재 보관 구역을 지정{blank(10)}.</div>
  {foot(13)}"""
page("연습", p13)

# ═══ 14쪽 상황 쓰기 — 과제③ 기말 안내문 공방 ═══
p14 = f"""{head_sec('3교시 · 쓰기', '기말 공방 — 나의 안전 안내문')}
  <div class="prose" style="margin-bottom:16px;">학기의 마지막 쓰기입니다. 1과부터 쓴 미니 쓰기를 꺼내, 내 작업장의 안전 안내문 한 편을 완성합니다. 이것이 과제③이고, 기말시험(유형 C)의 준비입니다.</div>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">안내문 공식 — 이 교재가 가르친 전부</div>
    <div style="font-size:14.5px; line-height:2.15;">① [무엇]이 [피동]-(으)ㄹ <b>우려가 있으니</b>, [행동]<b>하십시오</b>. (지시)<br>② [위험]이 생기<b>지 않도록</b> [대책]<b>할 것을 제안합니다</b>. (제안)<br>③ 안전 수칙을 <b>실천</b>합시다. (마무리)</div>
  </div>
  {sechead('A','나의 안내문 — 세 문장으로 완성하십시오.')}
  <div class="drill left" style="margin-bottom:{SP_M}px; font-size:15px; line-height:3.9;">
    제목: {blank(20)} 안전 안내문<br>
    ① {blank(34)}<br>
    ② {blank(34)}<br>
    ③ {blank(34)}</div>
  {sechead('B','점검 — 제출 전에 확인하십시오.')}
  <div class="left" style="font-size:14.5px; line-height:2.15; margin-bottom:{SP_M}px;">☐ 우려 공식을 썼다 &nbsp; ☐ 피동을 썼다 &nbsp; ☐ 격식체로 끝냈다 &nbsp; ☐ 구어(-니까·-세요)가 없다</div>
  <div class="caution" style="font-size:14px; line-height:1.95; padding:16px 18px;">
    <b>과제③ 제출(이번 주 수합)</b> · 완성한 안내문을 <b>LMS 과제방</b>에 제출합니다. 2~13주의 미니 쓰기 중 두 편을 골라 함께 제출합니다. 이 안내문이 기말시험 유형 C의 답안 연습입니다.</div>
  {foot(14)}"""
page("상황쓰기", p14)

# ═══ 15쪽 정리 ═══
def npill(t):
    return f'<div style="margin-bottom:12px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:13px;font-weight:800;height:29px;line-height:29px;padding:0 16px;">{t}</span></div>'
vgrid12 = ''.join(f'<div style="border:1px solid {HAIR};border-radius:6px;padding:8px 12px;font-size:13.5px;">☐ {w}</div>'
    for w in ['예방','개선','제안','건의','효과','수칙','실천','안전','방안','수립','발굴','정착'])

p15 = f"""{head_sec('3교시 · 쓰기', '정리 — 그리고 열두 과')}
  <div style="display:flex;flex-direction:column;gap:10px;font-size:15px;line-height:1.55;margin-bottom:14px;">
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">1</span><span style="padding-top:2px;">제안서는 세 칸이다 — <b>위험 요인 → 개선 방안 → 기대 효과</b>. 읽던 틀이 쓰는 틀이다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">2</span><span style="padding-top:2px;">예방의 문장은 <b>-지 않도록 + -(으)ㄹ 것을 제안합니다</b>로 만든다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">3</span><span style="padding-top:2px;">이 교재의 대표 문장 — <b>[무엇]이 [피동]-(으)ㄹ 우려가 있으니, [행동]하십시오.</b></span></div>
  </div>
  <div style="border-top:1px solid {HAIR};margin-bottom:16px;"></div>
  {npill('자가 점검 ① 체크리스트')}
  <div class="left" style="display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;font-size:14.5px;line-height:1.55;margin-bottom:{SP_M}px;">
    <div>☐ 제안서의 세 칸을 채울 수 있다</div>
    <div>☐ -지 않도록와 제안합니다를 이어 쓸 수 있다</div>
    <div>☐ 안내문 공식으로 두 문장을 쓸 수 있다</div>
    <div>☐ 기말 네 유형(A~D)이 무엇인지 안다</div>
    <div>☐ 구어와 격식체를 구별해 쓸 수 있다</div>
  </div>
  {npill('자가 점검 ② 문제로 확인')}
  <div class="left" style="font-size:15px;line-height:2.1;margin-bottom:{SP_M}px;">
    ① 제안서의 세 칸을 순서대로 쓰십시오. → {blank(14)}<br>
    ② "화물이 떨어지다"를 예방 목적으로 바꾸십시오. → 화물이 {blank(7)}<br>
    ③ 다음 중 <u>틀린</u> 문장을 고르십시오. ( {blank(2)} )<br>
    <span style="display:block; padding-left:26px; font-size:14.5px; line-height:1.8;">㉮ 덮개를 설치할 것을 제안합니다.<br>㉯ 덮개를 설치를 제안합니다.<br>㉰ 덮개 설치를 제안합니다.</span>
    ④ '미끄러질 우려가 있으니까 조심하세요'를 격식체로 고치십시오.<br>
    → {blank(22)}<br>
    ⑤ 미리 막는 것을 한 단어로 쓰십시오. → {blank(4)}</div>
  {npill('10초 어휘 셀프 체크')}
  <div style="font-size:13px;color:{SUB};margin-bottom:10px;">각 단어의 뜻이 3초 안에 떠오르지 않으면 ☐에 ✔ 하십시오. ✔한 단어는 2쪽으로 돌아가 예문과 함께 다시 읽으십시오.</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">{vgrid12}</div>
  {foot(15)}"""
page("정리", p15)

html = HEAD + '<body>' + ''.join(PAGES) + '</body></html>'
open('/home/claude/sik/ch12_full_15pages.html', 'w', encoding='utf-8').write(html)
print(f"[3/3] {len(PAGES)}쪽")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file:///home/claude/sik/ch12_full_15pages.html')
    pg.wait_for_timeout(1200)
    pg.pdf(path='/home/claude/sik/ch12.pdf', width='794px', height='1123px', print_background=True, page_ranges='1-15')
    b.close()
print("PDF ok")
