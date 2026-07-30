# -*- coding: utf-8 -*-
"""build_ch10.py — 산업안전한국어 제10과 「사고 사례」 (4부 사례 · 12주차 · Q10 · 부 전환)
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

FOOT_L = "산업안전한국어 · 4부 사례 제10과 사고 사례"
def foot(n): return footer(FOOT_L, f"{n:02d}")
def enc(t): return f'<span class="enc">{t}</span>'
PAGES = []
def page(label, body):
    PAGES.append(f'<div class="page" data-document-role="page" data-label="{label}">{body}</div>')



# ═══ 픽토 4종 — 10과 (사례 문서·원인 분석·위험·재발 방지) ═══
def picto_case():   # 사례 보고서 (문서+⚠)
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <rect x="30" y="22" width="40" height="56" rx="3" fill="#fff"/>
      <path d="M50 32 l11 19 h-22 Z" fill="{NAVY}"/>
      <line x1="50" y1="38" x2="50" y2="45" stroke="#fff" stroke-width="3"/><circle cx="50" cy="48.5" r="1.7" fill="#fff"/>
      <line x1="36" y1="60" x2="64" y2="60" stroke="{NAVY}" stroke-width="4"/>
      <line x1="36" y1="68" x2="56" y2="68" stroke="{NAVY}" stroke-width="4"/></svg>'''
def picto_mag():    # 원인 분석 (돋보기)
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <circle cx="44" cy="44" r="16" fill="none" stroke="#fff" stroke-width="7"/>
      <line x1="56" y1="56" x2="72" y2="72" stroke="#fff" stroke-width="9" stroke-linecap="round"/></svg>'''
def picto_gear():   # 위험 (기어+손)
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <circle cx="42" cy="52" r="13" fill="none" stroke="#fff" stroke-width="6"/>
      <g stroke="#fff" stroke-width="5" stroke-linecap="round">
        <line x1="42" y1="33" x2="42" y2="27"/><line x1="42" y1="71" x2="42" y2="77"/>
        <line x1="23" y1="52" x2="29" y2="52"/><line x1="55" y1="52" x2="61" y2="52"/>
        <line x1="29" y1="39" x2="33" y2="43"/><line x1="51" y1="61" x2="55" y2="65"/>
        <line x1="29" y1="65" x2="33" y2="61"/><line x1="51" y1="43" x2="55" y2="39"/></g>
      <path d="M62 30 l12 12 M74 30 l-12 12" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>'''
def picto_shieldck():  # 재발 방지 (방패 체크)
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 20 L76 30 V52 q0 20 -26 29 q-26 -9 -26 -29 V30 Z" fill="#fff"/>
      <path d="M39 50 l8 8 l15 -18" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/></svg>'''

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
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:118px;font-weight:900;color:{NAVY};line-height:.95;">10</div>
      <div style="margin-top:14px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:12.5px;font-weight:800;letter-spacing:.34em;height:30px;line-height:30px;padding:0 12px 0 20px;">제 10 과</span></div>
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:46px;font-weight:900;color:{INK};margin-top:22px;">사고 사례</div>
    </div>
    <div style="flex:none;width:322px;height:462px;position:relative;background:#E7EDF6;overflow:hidden;">
      <div style="position:absolute;top:120px;left:24px;width:56px;height:400px;background:#D8E1EF;"></div>
      <div style="position:absolute;top:230px;right:16px;width:70px;height:300px;background:#D1DBEC;"></div>
      <div style="position:absolute;top:-70px;left:150px;width:52px;height:640px;background:{NAVY};transform:rotate(16deg);"></div>
      <div style="position:absolute;top:52px;left:34px;right:34px;background:#fff;border-radius:16px;box-shadow:0 10px 26px rgba(20,35,80,.16);padding:26px 20px;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;justify-items:center;">
          {picto_case()}{picto_mag()}{picto_gear()}{picto_shieldck()}</div></div>
    </div>
  </div>
  <div style="display:flex;gap:26px;margin-top:40px;">
    <div style="flex:1.06;">
      <div style="display:flex;align-items:center;gap:9px;margin-bottom:16px;">
        {G_TARGET}<span style="font-size:16px;font-weight:800;color:{INK};">학습 목표</span>
        <div style="flex:1;border-top:1px solid {HAIR};"></div></div>
      <div style="display:flex;flex-direction:column;gap:13px;font-size:14.5px;line-height:1.6;">
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">1</span><span style="padding-top:2px;">사고 사례에서 <b>원인·경과·결과</b>를 찾아 읽습니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">2</span><span style="padding-top:2px;">위험을 <b>피동+우려 공식</b>으로 바꿔 말합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">3</span><span style="padding-top:2px;">대책과 <b>그 결과</b>를 한 문장으로 잇습니다.</span></div>
      </div>
    </div>
    <div style="flex:1;background:#EDF2FA;border-radius:12px;padding:20px 24px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px;">
        {G_BULB}<span style="font-size:15px;font-weight:800;color:{INK};">생각해 보기</span></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">다른 사람의 사고 이야기에서 무엇을 배울 수 있습니까?</div>
      <div style="border-top:1px dashed #C9D2E2;margin:11px 0;"></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">앞에서 배운 기계(프레스·컨베이어·지게차) 중 무엇이 가장 위험해 보입니까? 왜 그렇습니까?</div>
    </div>
  </div>
  <div style="display:flex;justify-content:center;align-items:flex-start;gap:4px;margin-top:42px;">
    {kcol(G_TALK,'1교시 · 어휘',NAVY,'핵심 어휘 12개 + 연습','사고를 읽는 말')}
    {CHEV}
    {kcol(G_AA,'2교시 · 문형',LIGHT,'-로 인한 · 피동+우려 종합','그 결과 + 종합')}
    {CHEV}
    {kcol(G_BOOK,'3교시 · 읽기',DEEP,'재해 사례 3건 읽기','사례 분석 쓰기 + 정리')}
  </div>
  <div style="position:absolute;top:{FOOTER_Y}px;left:64px;right:64px;border-top:1px solid {HAIR};padding-top:12px;display:flex;justify-content:space-between;align-items:center;">
    <span style="display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800;color:{INK};">
      {G_SHIELD} 남의 사고를 읽는 것 — 그것이 나의 예방입니다.</span>
    <span style="font-size:13px;font-weight:800;color:{NAVY};">01</span>
  </div>"""
page("도비라", dobira)

# ═══ 2쪽 어휘 12 ═══
V = [
 ("원인","기본","일이 일어난 이유입니다.","사고의 <b>원인</b>을 파악합니다."),
 ("결과","기본","일이 끝난 뒤의 모습입니다.","대책의 <b>결과</b>를 확인합니다."),
 ("사례","기본","실제로 있었던 일의 예입니다.","재해 <b>사례</b>를 읽고 배웁니다."),
 ("끼임","기본","기계 사이에 끼이는 사고입니다.","<b>끼임</b> 사고가 가장 많습니다."),
 ("낙하","기본","물건이 위에서 떨어지는 것입니다.","화물 <b>낙하</b>로 인한 부상입니다."),
 ("발생","기본","일이 일어나는 것입니다.","재해가 <b>발생</b>하였습니다."),
 ("방지","기본","일어나지 못하게 막는 것입니다.","재발 <b>방지</b> 대책을 세웁니다."),
 ("대책","기본","문제를 막기 위한 방법입니다.","<b>대책</b>을 세운 후 지킵니다."),
 ("경과","심화","일이 진행된 과정입니다.","재해 <b>경과</b>를 순서대로 씁니다."),
 ("재발","심화","같은 일이 다시 일어나는 것입니다.","<b>재발</b>을 방지하여야 합니다."),
 ("협착","심화","'끼임'의 문서 말입니다.","손이 금형 사이에 <b>협착</b>되었습니다."),
 ("전도","심화","'넘어짐'의 문서 말입니다.","지게차 <b>전도</b> 위험이 있습니다."),
]
v_cards = ''.join(vcard(w, lv, m, e) for w, lv, m, e in V)
p2 = f"""{head_sec('1교시 · 어휘', '핵심 어휘 12')}
  <div style="display:flex; align-items:center; gap:8px; font-size:13px; color:{SUB}; margin-bottom:16px;">
    <span class="lv b">기본</span><span>모든 학생 필수</span>
    <span class="lv a" style="margin-left:10px;">심화</span><span>법규·보고서의 문어 표현 — 읽고 이해할 수 있으면 충분합니다.</span></div>
  <div class="vgrid" style="gap:16px;">{v_cards}</div>
  {foot(2)}"""
page("핵심어휘", p2)

# ═══ 3쪽 어휘 연습 ═══
p3 = f"""{head_sec('1교시 · 어휘', '어휘 연습')}
  {sechead('A','알맞은 단어를 골라 빈칸을 채우십시오.')}
  <div class="wbank" style="margin-bottom:22px;">재발 · 경과 · 협착 · 대책</div>
  <div class="left" style="font-size:15px; line-height:2.75; margin-bottom:{SP_XL}px;">
    ① 같은 사고가 다시 일어나지 않도록 {blank(5)}을 세웁니다.<br>
    ② 손이 금형 사이에 {blank(5)}되는 사고가 있었습니다.<br>
    ③ 사고가 일어난 과정을 {blank(5)}라고 합니다.<br>
    ④ 대책을 지키면 {blank(5)}을 막을 수 있습니다.</div>
  {sechead('B','짝이 되는 말을 선으로 연결하십시오.')}
  <div style="margin-bottom:{SP_XL}px;">
  {connect(
    ["① 사고가", "② 원인을", "③ 재발을", "④ 대책을", "⑤ 결과를"],
    ["㉠ 세우다", "㉡ 발생하다", "㉢ 확인하다", "㉣ 방지하다", "㉤ 파악하다"],
    lw=160, rw=230, rowgap=34)}
  </div>
  {sechead('C','B에서 연결한 표현 중 두 개를 골라 문장을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.4;">
    ① {blank(40)}<br>
    ② {blank(40)}</div>
  {foot(3)}"""
page("어휘연습", p3)

# ═══ 4쪽 개념 — 사례 문서의 3구획 ═══
def zone(n, t, sub, d):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:36px 22px; display:flex; gap:16px; align-items:flex-start;">
      <span class="enc" style="margin-top:2px;">{n}</span>
      <div style="flex:1;">
        <div style="font-weight:800; font-size:16px; color:{DEEP};">{t} <span style="font-size:12.5px; color:{SUB}; font-weight:500;">{sub}</span></div>
        <div style="font-size:14px; line-height:1.65; margin-top:5px;">{d}</div></div></div>'''

p4 = f"""{head_sec('1교시 · 어휘', '사례 문서의 세 구획')}
  <div class="prose" style="margin-bottom:24px;">공단의 재해 사례는 언제나 같은 세 구획으로 쓰여 있습니다. 구획의 이름을 알면 처음 보는 사례도 읽을 수 있습니다.</div>
  <div style="display:flex; flex-direction:column; gap:30px; margin-bottom:{SP_XL}px;">
    {zone('①','재해 개요','— 무슨 일이 있었나','언제, 어디에서, 어떤 일이 어떤 경과로 일어났는지 요약합니다. 부상 내용(결과)까지 씁니다.')}
    {zone('②','발생 원인','— 왜 일어났나','무엇 때문에 일어났는지 씁니다. "N(으)로 인한 사고"의 꼴을 여기에서 만납니다.')}
    {zone('③','재발 방지 대책','— 어떻게 막나','같은 사고가 다시 일어나지 않게 할 방법입니다. 대책을 지킨 "그 결과"까지 이어집니다.')}
  </div>
  <div style="display:flex; align-items:center; justify-content:center; gap:14px; margin-bottom:{SP_L}px;">
    <span style="border:1.5px solid {NAVY}; border-radius:8px; padding:16px 28px; font-weight:800; color:{NAVY};">원인</span>
    <span style="color:{SUB};">→</span>
    <span style="border:1.5px solid {NAVY}; border-radius:8px; padding:12px 26px; font-weight:800; color:{NAVY};">경과</span>
    <span style="color:{SUB};">→</span>
    <span style="background:{NAVY}; border-radius:8px; padding:13px 26px; font-weight:800; color:#fff;">결과</span>
    <span style="font-size:13px; color:{SUB}; margin-left:10px;">— 사례를 읽는 순서이자 쓰는 순서</span>
  </div>
  <div class="tintbox">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">4부가 시작됩니다 — 배운 것으로 읽는 부</div>
    <div style="font-size:14.5px; line-height:1.85;">1~3부에서 표지·절차·권리를 배웠습니다. 4부에서는 그 말들로 <b>실제 사고 기록</b>을 읽습니다. 이번 과의 세 사례는 5과에서 배운 세 기계(프레스·컨베이어·지게차)에서 일어난 일입니다.</div>
  </div>
  {foot(4)}"""
page("개념", p4)

# ═══ 5쪽 확장① — 사고 유형의 말 ═══
p5 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ① — 사고 유형의 말')}
  <div class="prose" style="margin-bottom:24px;">사고에는 정해진 유형 이름이 있습니다. 뉴스와 표지, 사례 문서가 모두 이 이름을 씁니다. 일상의 말과 문서의 말을 짝으로 기억합니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:110px;height:6px;">유형</th><th style="width:190px;">일상의 말</th><th>이번 과 사례</th></tr>
    <tr><td><b>끼임</b></td><td>기계 사이에 끼이다</td><td>[가] 프레스 금형 — 문서에는 <b>협착</b>으로도 씁니다</td></tr>
    <tr><td><b>감김</b> <span style="font-size:12px;color:{SUB};">(3과)</span></td><td>돌아가는 부분에 말리다</td><td>[나] 컨베이어 체인</td></tr>
    <tr><td><b>낙하</b></td><td>물건이 떨어지다</td><td>[다] 지게차 화물</td></tr>
    <tr><td><b>전도</b></td><td>넘어지다 <span style="font-size:12px;color:{SUB};">(3과 '넘어짐')</span></td><td>이번 사례에는 없지만 표지에서 만납니다</td></tr>
  </table>
  {sechead('A','문서의 말을 일상의 말로 바꾸십시오.')}
  <div class="left" style="font-size:15px; line-height:4.15; margin-bottom:{SP_XL}px;">
    ① 손이 <b>협착</b>되었음 → 손이 {blank(5)}<br>
    ② 지게차 <b>전도</b> 위험 → 지게차가 {blank(5)} 위험</div>
  {sechead('B','알맞은 유형 이름을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.6;">
    ① 위에서 떨어진 상자에 맞았습니다. → {blank(4)} 사고<br>
    ② 롤러에 장갑이 말려 들어갔습니다. → {blank(4)} 사고</div>
  {foot(5)}"""
page("어휘확장1", p5)

# ═══ 6쪽 확장② — 함께 쓰는 말 ═══
def collo(a, b, m, e):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:24px 18px;">
      <div style="font-size:17px; font-weight:800; color:{DEEP};">{a} <span style="color:{LIGHT};">+</span> {b}</div>
      <div style="font-size:13.5px; margin-top:5px; line-height:1.6;">{m}</div>
      <div style="font-size:12.5px; color:{SUB}; border-top:1px dashed {HAIR}; margin-top:12px; padding-top:11px; line-height:1.7;">{e}</div></div>'''

p6 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ② — 함께 쓰는 말')}
  <div class="prose" style="margin-bottom:24px;">사례 문서의 말은 짝이 정해져 있습니다. 네 짝이면 세 구획을 다 말할 수 있습니다.</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:26px; margin-bottom:{SP_XL}px;">
    {collo('사고가','발생하다','일이 일어난다는 문서의 말입니다.','재해가 <b>발생</b>한 일시와 장소')}
    {collo('원인을','파악하다','이유를 정확히 안다는 뜻입니다. (3과에서 배운 말)','<b>원인을 파악</b>한 후에 대책을 세웁니다.')}
    {collo('대책을','세우다','막을 방법을 만든다는 뜻입니다.','재발 방지 <b>대책을 세웁니다</b>.')}
    {collo('재발을','방지하다','같은 일이 다시 없게 막는 것입니다.','덮개를 설치하여 <b>재발을 방지</b>합니다.')}
  </div>
  {sechead('A','알맞은 짝을 골라 문장을 완성하십시오.')}
  <div class="wbank" style="margin-bottom:26px;">발생 · 파악 · 대책 · 방지</div>
  <div class="left" style="font-size:15px; line-height:4.05;">
    ① 어제 14시에 끼임 사고가 {blank(4)}하였습니다.<br>
    ② 먼저 사고의 원인을 {blank(4)}합니다.<br>
    ③ 원인에 맞는 {blank(4)}을 세웁니다.<br>
    ④ 대책을 지켜 재발을 {blank(4)}합니다.</div>
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

IMG_TITLE = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <rect x="8" y="12" width="84" height="76" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="5"/>
  <rect x="16" y="22" width="68" height="20" rx="3" fill="{NAVY}"/>
  <text x="50" y="36" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">사고 보고서</text>
  <text x="50" y="62" text-anchor="middle" font-size="12.5" font-weight="bold" fill="{NAVY}">N(으)로 인한 N</text>
  <line x1="22" y1="68" x2="78" y2="68" stroke="{NAVY}" stroke-width="3"/>
  <line x1="22" y1="78" x2="60" y2="78" stroke="{HAIR}" stroke-width="4"/></svg>'''
IMG_HANDGEAR = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <path d="M50 12 L70 46 H30 Z" fill="#F6C344" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
  <line x1="50" y1="24" x2="50" y2="35" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>
  <circle cx="50" cy="41" r="2.2" fill="{INK}"/>
  <circle cx="32" cy="72" r="10" fill="none" stroke="{NAVY}" stroke-width="5"/>
  <circle cx="60" cy="72" r="10" fill="none" stroke="{NAVY}" stroke-width="5"/>
  <line x1="22" y1="60" x2="72" y2="60" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>
  <path d="M80 52 v14 a6 6 0 0 1 -12 0" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/></svg>'''
IMG_ARROW = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <path d="M28 18 L48 26 V42 q0 15 -20 22 q-20 -7 -20 -22 V26 Z" fill="#fff" stroke="{NAVY}" stroke-width="4.5"/>
  <path d="M20 40 l6 6 l11 -13" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>
  <text x="28" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="{NAVY}">대책</text>
  <path d="M52 48 h16 m-6 -7 l7 7 l-7 7" fill="none" stroke="{SUB}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="82" cy="48" r="14" fill="{NAVY}"/>
  <text x="82" y="53" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">0</text>
  <text x="82" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="{NAVY}">재발</text></svg>'''

p7 = gcard('1', 'N(으)로 인한 + N', IMG_TITLE,
  '덮개 미설치<b>로 인한</b> 감김 사고', '재해 사례 보고서 제목',
  """원인을 명사 앞에 붙이는 꼴입니다. 보고서의 제목과 요약이 이 꼴로 쓰입니다. 뒤에 문장이 아니라 <b>명사</b>가 옵니다.""",
  '비교 · 3과와 7과에서 배운 말',
  f"""· 3과 — 부주의<b>로 인해</b> 사고가 났습니다. (뒤에 문장)<br>
      · 7과 — 위험<b>으로 인하여</b> 중지하였습니다. (서류의 긴 꼴)<br>
      · 10과 — 부주의<b>로 인한</b> 사고 (뒤에 명사) — '인해→인한' 한 글자가 바뀝니다.""",
  f"""<span class="x">✗ 덮개 미설치로 인해 사고</span><br>
      ○ 덮개 미설치<b>로 인한</b> 사고 / 미설치<b>로 인해</b> 사고가 났다<br>
      <span style="font-size:13px; color:{SUB};">뒤가 명사면 '인한', 뒤가 문장이면 '인해'입니다.</span>""",
  f"""{enc('①')} 결속 불량{blank(5)} 낙하 사고<br>
      {enc('②')} 연동장치 해제{blank(5)} 끼임 재해<br>
      {enc('③')} (문장으로) 안전모를 써서 부상을 막았다 → 안전모 착용{blank(5)} 예방""", lv='심화', comb='명사')
page("문형1", p7 + foot(7))

p8 = gcard('2', '피동 + -(으)ㄹ 우려가 있다', IMG_HANDGEAR,
  '동력전달부에 손이 <b>말릴 우려가 있다</b>.', '위험 분석 문장',
  """새 문형이 아닙니다. 1과의 공식을 그대로 씁니다. [무엇]이 [피동]-ㄹ <b>우려가 있다</b>. 사례 속 위험을 이 공식으로 바꿉니다. 사고는 과거지만, 우려는 아직 막을 수 있습니다.""",
  '비교 · 이 공식이 걸어온 길',
  f"""1과(표지) → 5과(점검표) → 8과(중지 선언) → <b>10과(사례 분석)</b>.<br>
      끼이다·말리다·떨어지다 — 피동을 쓰는 이유는 <b>기계가 하는 일</b>이기 때문입니다. 내가 끼는 게 아니라, 손이 끼<b>이는</b> 것입니다.""",
  f"""<span class="x">✗ 손을 끼일 우려가 있다.</span><br>
      ○ 손<b>이</b> 끼일 우려가 있다.<br>
      <span style="font-size:13px; color:{SUB};">피동 앞은 이/가입니다. (1과에서 배운 규칙 그대로)</span>""",
  f"""사례에서 위험을 찾아 공식으로 바꾸십시오.<br>
      {enc('①')} [나] 체인 노출 → 머리카락이 {blank(4)} 우려가 있다<br>
      {enc('②')} [다] 결속 불량 → 상자가 {blank(5)} 우려가 있다<br>
      {enc('③')} [가] 연동장치 해제 → 손이 {blank(4)} 우려가 있다""")
page("문형2", p8 + foot(8))

p9 = gcard('3', '-(으)ㄴ 결과 · 그 결과', IMG_ARROW,
  '덮개를 설치하였다. <b>그 결과</b> 동종 재해가 재발하지 않았다.', '재발 방지 대책의 끝 문장',
  """앞의 일이 만든 결과를 잇는 말입니다. 한 문장 안에서는 <b>-(으)ㄴ 결과</b>, 문장을 새로 시작할 때는 <b>그 결과</b>를 씁니다.""",
  '비교 · 6과에서 만난 꼴',
  f"""6과 작업일지에서 읽었습니다 — "점검<b>한 결과</b> 이상이 없어 작업을 다시 시작했습니다."<br>
      그때는 읽기만 했습니다. 이제 대책의 효과를 쓸 때 내가 씁니다.""",
  f"""<span class="x">✗ 덮개를 설치했다. 그 결과로 인해 재발하지 않았다.</span><br>
      ○ 덮개를 설치했다. <b>그 결과</b> 재발하지 않았다.<br>
      <span style="font-size:13px; color:{SUB};">'그 결과' 뒤에 '로 인해'를 겹쳐 쓰지 않습니다.</span>""",
  f"""{enc('①')} 전원을 차단하고 정비하였다. {blank(4)} 끼임 사고가 없었다.<br>
      {enc('②')} 점검{blank(4)} 이상이 발견되어 운전을 정지하였다.<br>
      {enc('③')} 안전모를 착용하였다. 그 결과 {blank(12)}""", wide=False)
page("문형3", p9 + foot(9))

# ═══ 10쪽 문형 종합 ═══
p10 = f"""{head_sec('2교시 · 문형', '문형 종합')}
  {sechead('A','두 문장을 한 제목으로 바꾸십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.95;">
    {enc('①')} 결속이 불량했다. 그래서 낙하 사고가 났다.<br>
    → 결속 불량{blank(5)} 낙하 사고<br>
    {enc('②')} 덮개가 없었다. 그래서 감김 사고가 났다.<br>
    → 덮개 미설치{blank(5)} 감김 사고</div>
  {sechead('B','사례 문장을 읽고 빈칸을 채우십시오.')}
  <div class="lawq" style="margin-bottom:16px; font-size:14.5px; line-height:2.0; padding:16px 18px; background:#FBFCFE; border:1px solid {HAIR}; border-radius:6px;">동력전달부가 노출되어 있었다. 머리카락이 말릴 우려가 있는 상태였다. 안전덮개를 설치하였다. 그 결과 동종 재해가 재발하지 않았다.</div>
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.8;">
    {enc('①')} 위험을 나타낸 공식 문장을 찾아 쓰십시오. → {blank(18)}<br>
    {enc('②')} 대책의 효과를 이은 말: {blank(5)}</div>
  {sechead('C','미니 쓰기 — 세 문장으로 잇습니다.')}
  <div class="drill left" style="font-size:15px; line-height:2.9;">
    (원인) {blank(10)}(으)로 인한 위험이 있다.<br>
    (분석) {blank(10)}이/가 {blank(6)}ㄹ 우려가 있다.<br>
    (대책과 결과) {blank(10)}하였다. 그 결과 {blank(10)}</div>
  {foot(10)}"""
page("문형종합", p10)

print(f"[2/3] {len(PAGES)}쪽")

# ═══ 11쪽 실물 — 재해 사례 3건 ═══
def caserow(tag, title, o, c, m):
    return f'''<div style="border:1px solid {HAIR}; border-radius:9px; padding:24px 22px; margin-bottom:22px;">
      <div style="font-weight:800; color:{NAVY}; font-size:14px; margin-bottom:8px;">{tag} {title}</div>
      <div style="font-size:13.5px; line-height:1.95;">
        <div style="display:flex; gap:9px; margin-bottom:9px;"><span style="flex:none; font-weight:800; color:{DEEP}; width:78px;">재해 개요</span><span>{o}</span></div>
        <div style="display:flex; gap:9px; margin-bottom:9px;"><span style="flex:none; font-weight:800; color:{DEEP}; width:78px;">발생 원인</span><span>{c}</span></div>
        <div style="display:flex; gap:9px;"><span style="flex:none; font-weight:800; color:{DEEP}; width:78px;">방지 대책</span><span>{m}</span></div></div></div>'''

p11 = f"""{head_sec('3교시 · 읽기', '실물 자료 읽기 — 재해 사례 3건')}
  {caserow('[가]','끼임 — 프레스 금형',
    '취출장치 오류를 확인하던 작업자의 손이 하강하는 금형 사이에 <b>협착</b>되어 전치 6주의 부상이 <b>발생</b>함.',
    '연동장치 기능을 해제한 채 금형에 접근함 · 센서 감지<b>로 인한</b> 설비 가동.',
    '정비 시 전원을 차단한 후 작업함(4과) · 방호장치를 정상 작동 상태로 유지함.')}
  {caserow('[나]','감김 — 컨베이어 체인',
    '바닥에 떨어진 제품을 주우려고 몸을 숙이다가 체인에 머리카락이 <b>말려 들어감</b>.',
    '동력전달부(체인)가 노출됨 · 덮개 미설치<b>로 인한</b> 감김.',
    '동력전달부에 안전덮개를 설치함. <b>그 결과</b> 동종 재해가 재발하지 않음.')}
  {caserow('[다]','낙하 — 지게차 화물',
    '지게차가 옮기던 팔레트에서 결속되지 않은 상자가 <b>낙하</b>하여 아래를 지나던 작업자가 어깨에 부상을 입음.',
    '화물 결속 불량 · 지게차 주변 통행 통제가 없었음 · 안전모 미착용.',
    '화물을 결속한 후 운반함 · 화물 아래 통행을 금지함 · 위험 구역에서 안전모를 착용함.')}
  <div class="lnote" style="font-size:11.5px; color:{SUB}; margin-bottom:20px;">KOSHA 재해사례·업종별 실무길잡이를 교육용으로 재구성함(부상 정도 조정) · 세 구획 이름은 원문 형식을 따름</div>
  <div class="tintbox" style="font-size:13.5px; line-height:2.2; padding:22px 26px;">
    <b>읽기 틀</b> — 세 사례 모두 같은 순서입니다: 무슨 일이(<b>개요</b>) → 무엇 때문에(<b>원인</b>, -로 인한) → 어떻게 막나(<b>대책</b>, 그 결과). 이 순서가 12과에서 여러분이 쓸 예방 제안문의 뼈대가 됩니다.</div>
  {foot(11)}"""
page("실물자료읽기", p11)

# ═══ 12쪽 읽고 답하기 ═══
p12 = f"""{head_sec('3교시 · 읽기', '읽고 답하기')}
  <div class="tintbox" style="margin-bottom:{SP_M}px; font-size:14px;">11쪽의 세 사례를 다시 보면서 답하십시오.</div>
  {sechead('A','기본 — 맞으면 ○, 틀리면 ✗를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.75;">
    {enc('①')} [가]의 작업자는 전원을 차단한 후 금형에 접근했다. ( {blank(2)} )<br>
    {enc('②')} [나]의 원인은 동력전달부가 노출되어 있었기 때문이다. ( {blank(2)} )<br>
    {enc('③')} [다]에서 상자는 결속되어 있었다. ( {blank(2)} )</div>
  {sechead('B','심화 — 사례에서 찾아 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.7;">
    {enc('①')} [가]의 대책은 몇 과에서 배운 절차입니까? 무슨 절차입니까?<br>
    → {blank(20)}<br>
    {enc('②')} [나]에서 대책의 효과를 이은 말(두 어절)을 찾아 쓰십시오.<br>
    → {blank(8)}</div>
  {sechead('C','확장 — 생각을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    세 사례의 작업자들은 규칙을 몰라서 다쳤습니까, 알면서 지키지 않아서 다쳤습니까? 하나를 골라 이유를 쓰십시오.<br>
    → {blank(26)}<br>
    {blank(30)}</div>
  {foot(12)}"""
page("읽고답하기", p12)

# ═══ 13쪽 연습 — 사례 분석 틀 ═══
p13 = f"""{head_sec('3교시 · 읽기', '연습 — 사례 분석 틀 채우기')}
  <div class="prose" style="margin-bottom:18px;">[다] 낙하 사례를 분석 틀에 정리합니다. 사례를 다시 읽고 칸을 채우십시오.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:120px;height:6px;">틀</th><th>내용</th></tr>
    <tr><td>유형</td><td>{blank(4)} 사고</td></tr>
    <tr><td>원인</td><td>화물 {blank(6)} · 통행 통제 없음 · 안전모 {blank(5)}</td></tr>
    <tr><td>위험 공식</td><td>상자가 {blank(5)} 우려가 있다</td></tr>
    <tr><td>대책</td><td>화물을 {blank(5)}한 후 운반한다 · 화물 아래 {blank(4)}을 금지한다</td></tr>
  </table>
  {sechead('A','제목을 만드십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.7;">
    {enc('①')} [다]의 보고서 제목: {blank(8)}(으)로 인한 {blank(4)} 사고<br>
    {enc('②')} [가]의 보고서 제목: 연동장치 {blank(4)}로 인한 {blank(4)} 재해</div>
  {sechead('B','대책의 결과를 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:3.3;">
    화물을 결속하고 통행을 금지하였다.<br>
    그 결과 {blank(24)}</div>
  {foot(13)}"""
page("연습", p13)

# ═══ 14쪽 상황 쓰기 — 사례 분석 미니 쓰기 (과제③ 재료) ═══
p14 = f"""{head_sec('3교시 · 쓰기', '상황 쓰기 — 나의 사례 분석')}
  <div class="prose" style="margin-bottom:16px;">세 사례 중 하나를 골라, 남에게 알려 주는 세 문장을 씁니다. 이 글이 14주 과제③(예방 안내문)의 첫 재료가 됩니다.</div>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">분석 쓰기 공식 — 세 문장</div>
    <div style="font-size:14.5px; line-height:2.1;">[원인] N(으)로 인한 N 사고가 발생하였다.<br>[위험] {blank(0)}이/가 -(으)ㄹ 우려가 있(었)다.<br>[대책·결과] -하였다. 그 결과 재발하지 않았다.</div>
  </div>
  {sechead('A','고른 사례를 세 문장으로 분석해 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_M}px; font-size:15px; line-height:3.35;">
    고른 사례: ( 가 · 나 · 다 )<br>
    ① {blank(34)}<br>
    ② {blank(34)}<br>
    ③ {blank(34)}</div>
  {sechead('B','나의 눈 — 한 문장을 더 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_M}px; font-size:15px; line-height:2.9;">
    이 사고를 막기 위해 내가 현장에서 지킬 것 한 가지:<br>
    {blank(34)}</div>
  <div class="caution" style="font-size:14px; line-height:1.95; padding:16px 18px;">
    <b>제출</b> · 완성한 분석 글을 이번 주 <b>LMS 과제방</b>에 제출합니다. 이 글은 <b>과제③(14주 수합, 예방 안내문)</b>의 재료로 다시 씁니다.</div>
  {foot(14)}"""
page("상황쓰기", p14)

# ═══ 15쪽 정리 ═══
def npill(t):
    return f'<div style="margin-bottom:12px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:13px;font-weight:800;height:29px;line-height:29px;padding:0 16px;">{t}</span></div>'
vgrid12 = ''.join(f'<div style="border:1px solid {HAIR};border-radius:6px;padding:8px 12px;font-size:13.5px;">☐ {w}</div>'
    for w in ['원인','결과','사례','끼임','낙하','발생','방지','대책','경과','재발','협착','전도'])

p15 = f"""{head_sec('3교시 · 읽기', '정리')}
  <div style="display:flex;flex-direction:column;gap:10px;font-size:15px;line-height:1.55;margin-bottom:14px;">
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">1</span><span style="padding-top:2px;">사례는 세 구획이다 — <b>개요</b>(무슨 일) → <b>원인</b>(왜) → <b>대책</b>(어떻게 막나).</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">2</span><span style="padding-top:2px;">뒤가 명사면 <b>-로 인한</b>, 뒤가 문장이면 -로 인해 — 한 글자가 다르다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">3</span><span style="padding-top:2px;">위험은 <b>피동+우려</b>로 분석하고, 대책의 효과는 <b>그 결과</b>로 잇는다.</span></div>
  </div>
  <div style="border-top:1px solid {HAIR};margin-bottom:16px;"></div>
  {npill('자가 점검 ① 체크리스트')}
  <div class="left" style="display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;font-size:14.5px;line-height:1.55;margin-bottom:{SP_M}px;">
    <div>☐ 사례 문서의 세 구획 이름을 말할 수 있다</div>
    <div>☐ '인한'과 '인해'를 구별해 쓸 수 있다</div>
    <div>☐ 사고 유형 다섯 가지를 말할 수 있다</div>
    <div>☐ 위험을 피동+우려 공식으로 쓸 수 있다</div>
    <div>☐ 세 문장 분석 글을 쓸 수 있다</div>
  </div>
  {npill('자가 점검 ② 문제로 확인')}
  <div class="left" style="font-size:15px;line-height:2.1;margin-bottom:{SP_M}px;">
    ① '끼임'의 문서 말을 쓰십시오. → {blank(4)}<br>
    ② "덮개가 없어서 난 사고"를 제목으로 바꾸십시오. → 덮개 미설치{blank(5)} 사고<br>
    ③ 다음 중 <u>틀린</u> 문장을 고르십시오. ( {blank(2)} )<br>
    <span style="display:block; padding-left:26px; font-size:14.5px; line-height:1.8;">㉮ 손이 끼일 우려가 있다.<br>㉯ 결속 불량으로 인한 낙하 사고.<br>㉰ 덮개를 설치했다. 그 결과로 인해 재발하지 않았다.</span>
    ④ '손<span class="x">을</span> 끼일 우려가 있다'에서 틀린 부분을 바르게 고치십시오. → {blank(4)}<br>
    ⑤ 재해가 다시 일어나는 것을 무엇이라고 합니까? → {blank(4)}</div>
  {npill('10초 어휘 셀프 체크')}
  <div style="font-size:13px;color:{SUB};margin-bottom:10px;">각 단어의 뜻이 3초 안에 떠오르지 않으면 ☐에 ✔ 하십시오. ✔한 단어는 2쪽으로 돌아가 예문과 함께 다시 읽으십시오.</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">{vgrid12}</div>
  {foot(15)}"""
page("정리", p15)

html = HEAD + '<body>' + ''.join(PAGES) + '</body></html>'
open('/home/claude/sik/ch10_full_15pages.html', 'w', encoding='utf-8').write(html)
print(f"[3/3] {len(PAGES)}쪽 → ch10_full_15pages.html")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file:///home/claude/sik/ch10_full_15pages.html')
    pg.wait_for_timeout(1200)
    pg.pdf(path='/home/claude/sik/ch10.pdf', width='794px', height='1123px', print_background=True, page_ranges='1-15')
    b.close()
print("PDF ok")
