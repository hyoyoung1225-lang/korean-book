# -*- coding: utf-8 -*-
"""build_ch11.py — 산업안전한국어 제11과 「신고와 구조 요청」 (4부 사례 · 13주차 · Q11 · 유일 구어 주간)
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

FOOT_L = "산업안전한국어 · 4부 사례 제11과 신고와 구조 요청"
def foot(n): return footer(FOOT_L, f"{n:02d}")
def enc(t): return f'<span class="enc">{t}</span>'
PAGES = []
def page(label, body):
    PAGES.append(f'<div class="page" data-document-role="page" data-label="{label}">{body}</div>')




# ═══ 픽토 4종 — 11과 (전화 신고·위치·구급차·침착) ═══
def picto_call():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M34 26 q-8 2 -6 12 q3 18 16 30 q12 12 28 14 q10 1 11 -7 l1 -8 -13 -5 -6 6 q-9 -4 -15 -10 q-6 -6 -10 -15 l6 -6 -5 -13 Z" fill="#fff"/>
      <text x="64" y="36" text-anchor="middle" font-size="17" font-weight="bold" fill="#fff">119</text></svg>'''
def picto_pin():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 20 a20 20 0 0 1 20 20 q0 14 -20 38 q-20 -24 -20 -38 a20 20 0 0 1 20 -20 Z" fill="#fff"/>
      <circle cx="50" cy="40" r="8" fill="{NAVY}"/></svg>'''
def picto_amb():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <rect x="20" y="42" width="38" height="22" rx="3" fill="#fff"/>
      <path d="M58 46 h14 l8 10 v8 h-22 Z" fill="#fff"/>
      <circle cx="32" cy="68" r="6" fill="{NAVY}" stroke="#fff" stroke-width="3"/>
      <circle cx="66" cy="68" r="6" fill="{NAVY}" stroke="#fff" stroke-width="3"/>
      <line x1="33" y1="53" x2="45" y2="53" stroke="{NAVY}" stroke-width="4"/>
      <line x1="39" y1="47" x2="39" y2="59" stroke="{NAVY}" stroke-width="4"/></svg>'''
def picto_calm():
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <circle cx="50" cy="48" r="20" fill="none" stroke="#fff" stroke-width="6"/>
      <line x1="50" y1="48" x2="50" y2="36" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
      <line x1="50" y1="48" x2="59" y2="53" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
      <path d="M30 76 q20 10 40 0" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>'''

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
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:118px;font-weight:900;color:{NAVY};line-height:.95;">11</div>
      <div style="margin-top:14px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:12.5px;font-weight:800;letter-spacing:.34em;height:30px;line-height:30px;padding:0 12px 0 20px;">제 11 과</span></div>
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:42px;font-weight:900;color:{INK};margin-top:22px;">신고와 구조 요청</div>
    </div>
    <div style="flex:none;width:322px;height:462px;position:relative;background:#E7EDF6;overflow:hidden;">
      <div style="position:absolute;top:120px;left:24px;width:56px;height:400px;background:#D8E1EF;"></div>
      <div style="position:absolute;top:230px;right:16px;width:70px;height:300px;background:#D1DBEC;"></div>
      <div style="position:absolute;top:-70px;left:150px;width:52px;height:640px;background:{NAVY};transform:rotate(16deg);"></div>
      <div style="position:absolute;top:52px;left:34px;right:34px;background:#fff;border-radius:16px;box-shadow:0 10px 26px rgba(20,35,80,.16);padding:26px 20px;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;justify-items:center;">
          {picto_call()}{picto_pin()}{picto_amb()}{picto_calm()}</div></div>
    </div>
  </div>
  <div style="display:flex;gap:26px;margin-top:40px;">
    <div style="flex:1.06;">
      <div style="display:flex;align-items:center;gap:9px;margin-bottom:16px;">
        {G_TARGET}<span style="font-size:16px;font-weight:800;color:{INK};">학습 목표</span>
        <div style="flex:1;border-top:1px solid {HAIR};"></div></div>
      <div style="display:flex;flex-direction:column;gap:13px;font-size:14.5px;line-height:1.6;">
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">1</span><span style="padding-top:2px;"><b>위치·인원·상태</b> 세 가지를 순서대로 신고합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">2</span><span style="padding-top:2px;">"-고 있다·-아 있다"로 상황을 <b>정확히 묘사</b>합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">3</span><span style="padding-top:2px;">비상 방송을 <b>알아듣고</b> 그대로 행동합니다.</span></div>
      </div>
    </div>
    <div style="flex:1;background:#EDF2FA;border-radius:12px;padding:20px 24px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px;">
        {G_BULB}<span style="font-size:15px;font-weight:800;color:{INK};">생각해 보기</span></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">눈앞에서 동료가 쓰러지면, 한국어로 뭐라고 말하겠습니까?</div>
      <div style="border-top:1px dashed #C9D2E2;margin:11px 0;"></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">지금 일하는 곳의 주소를 한국어로 말할 수 있습니까?</div>
    </div>
  </div>
  <div style="display:flex;justify-content:center;align-items:flex-start;gap:4px;margin-top:42px;">
    {kcol(G_TALK,'1교시 · 어휘',NAVY,'핵심 어휘 12개 + 연습','신고의 말')}
    {CHEV}
    {kcol(G_AA,'2교시 · 문형',LIGHT,'-고 있다·-아 있다 · 인데요','주시기 바랍니다 + 종합')}
    {CHEV}
    {kcol(G_BOOK,'3교시 · 읽기',DEEP,'신고 담화 + 행동 수칙','신고문 말하기·쓰기 + 정리')}
  </div>
  <div style="position:absolute;top:{FOOTER_Y}px;left:64px;right:64px;border-top:1px solid {HAIR};padding-top:12px;display:flex;justify-content:space-between;align-items:center;">
    <span style="display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800;color:{INK};">
      {G_SHIELD} 세 마디면 됩니다 — 어디, 몇 명, 어떤 상태.</span>
    <span style="font-size:13px;font-weight:800;color:{NAVY};">01</span>
  </div>"""
page("도비라", dobira)

# ═══ 2쪽 어휘 12 ═══
V = [
 ("신고","기본","위급한 일을 119에 알리는 것입니다.","사고를 발견하면 즉시 <b>신고</b>합니다."),
 ("부상","기본","몸을 다치는 것입니다.","<b>부상</b>을 입은 사람이 한 명 있습니다."),
 ("응급","기본","아주 급한 상황입니다.","<b>응급</b> 상황에서는 119를 누릅니다."),
 ("구조","기본","위험에서 구해 내는 것입니다.","<b>구조</b>를 요청합니다."),
 ("위치","기본","있는 곳입니다. 신고의 첫 번째 정보입니다.","<b>위치</b>를 먼저 말합니다."),
 ("인원","기본","사람의 수입니다. 신고의 두 번째 정보입니다.","다친 <b>인원</b>은 한 명입니다."),
 ("상태","기본","지금 어떤 모습인지입니다. 세 번째 정보입니다.","환자의 <b>상태</b>를 말합니다."),
 ("환자","기본","다치거나 아픈 사람입니다.","<b>환자</b>는 의식이 있습니다."),
 ("의식","심화","정신이 깨어 있는 것입니다.","<b>의식</b>이 있습니까? — 네, 있습니다."),
 ("출혈","심화","피가 나는 것입니다.","팔에 <b>출혈</b>이 있습니다."),
 ("화상","심화","불이나 뜨거운 것에 데는 것입니다.","손에 <b>화상</b>을 입었습니다."),
 ("침착","심화","당황하지 않고 차분한 것입니다.","<b>침착</b>하게 묻는 말에 답합니다."),
]
v_cards = ''.join(vcard(w, lv, m, e) for w, lv, m, e in V)
p2 = f"""{head_sec('1교시 · 어휘', '핵심 어휘 12')}
  <div style="display:flex; align-items:center; gap:8px; font-size:13px; color:{SUB}; margin-bottom:16px;">
    <span class="lv b">기본</span><span>모든 학생 필수</span>
    <span class="lv a" style="margin-left:10px;">심화</span><span>구급대·병원에서 만나는 말 — 듣고 답할 수 있으면 충분합니다.</span></div>
  <div class="vgrid" style="gap:16px;">{v_cards}</div>
  {foot(2)}"""
page("핵심어휘", p2)

# ═══ 3쪽 어휘 연습 ═══
p3 = f"""{head_sec('1교시 · 어휘', '어휘 연습')}
  {sechead('A','알맞은 단어를 골라 빈칸을 채우십시오.')}
  <div class="wbank" style="margin-bottom:22px;">의식 · 출혈 · 침착 · 인원</div>
  <div class="left" style="font-size:15px; line-height:2.75; margin-bottom:{SP_XL}px;">
    ① 환자가 눈을 뜨고 말을 합니다. {blank(4)}이 있습니다.<br>
    ② 팔에서 피가 나고 있습니다. {blank(4)}이 있습니다.<br>
    ③ 다친 사람의 수를 {blank(4)}이라고 합니다.<br>
    ④ 당황하지 말고 {blank(4)}하게 답하십시오.</div>
  {sechead('B','짝이 되는 말을 선으로 연결하십시오.')}
  <div style="margin-bottom:{SP_XL}px;">
  {connect(
    ["① 사고를", "② 구조를", "③ 부상을", "④ 위치를", "⑤ 화상을"],
    ["㉠ 입다", "㉡ 신고하다", "㉢ 말하다", "㉣ 요청하다", "㉤ 당하다"],
    lw=160, rw=230, rowgap=34)}
  </div>
  {sechead('C','B에서 연결한 표현 중 두 개를 골라 문장을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.4;">
    ① {blank(40)}<br>
    ② {blank(40)}</div>
  {foot(3)}"""
page("어휘연습", p3)

# ═══ 4쪽 개념 — 신고 3정보 ═══
def infocard(pic, n, t, ex):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:34px 22px; display:flex; gap:18px; align-items:center;">
      <div style="flex:none;">{pic}</div>
      <div style="flex:1;">
        <div style="display:flex; align-items:baseline; gap:10px;">
          <span class="enc">{n}</span><span style="font-weight:800; font-size:16px; color:{DEEP};">{t}</span></div>
        <div style="font-size:14px; line-height:1.65; margin-top:5px;">{ex}</div></div></div>'''

p4 = f"""{head_sec('1교시 · 어휘', '신고는 세 마디입니다')}
  <div class="prose" style="margin-bottom:26px;">119에 전화하면 상황실이 묻습니다. 내가 길게 말하지 않아도 됩니다. 세 가지 정보만 준비하면 됩니다 — 어디, 몇 명, 어떤 상태.</div>
  <div style="display:flex; flex-direction:column; gap:30px; margin-bottom:{SP_XL}px;">
    {infocard(picto_pin(),'①','위치 — 어디입니까?', '"○○공단 ○○정밀 제2공장입니다." 회사 이름과 동 이름을 미리 알아 둡니다.')}
    {infocard(picto_amb(),'②','인원 — 몇 명입니까?', '"다친 사람은 한 명입니다." 숫자만 말하면 됩니다.')}
    {infocard(picto_calm(),'③','상태 — 어떻습니까?', '"의식은 있고, 팔에서 피가 나고 있습니다." 보이는 대로 말합니다.')}
  </div>
  <div class="tintbox">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">말이 안 나오면 — 문자·사진·앱으로도 신고할 수 있습니다</div>
    <div style="font-size:14.5px; line-height:1.85;">119는 전화만이 아닙니다. <b>문자와 사진</b>으로 신고할 수 있고, '긴급신고 바로' 앱은 <b>그림을 누르면</b> 내 위치와 함께 신고됩니다. 외국인을 위해 만들어진 제도입니다.</div>
  </div>
  {foot(4)}"""
page("개념", p4)

# ═══ 5쪽 확장① — 상태를 말하는 표현 ═══
p5 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ① — 상태를 말하는 표현')}
  <div class="prose" style="margin-bottom:24px;">상황실이 가장 알고 싶은 것은 환자의 상태입니다. 자주 쓰는 상태 표현을 질문과 답의 짝으로 기억합니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:230px;height:8px;">상황실의 질문</th><th>나의 답</th></tr>
    <tr><td>의식이 있습니까?</td><td>네, 의식이 있습니다. / 아니요, 의식이 없습니다.</td></tr>
    <tr><td>숨을 쉬고 있습니까?</td><td>네, 숨을 쉬고 있습니다.</td></tr>
    <tr><td>피가 많이 납니까?</td><td>팔에서 피가 나고 있습니다. / 출혈이 심합니다.</td></tr>
    <tr><td>환자가 어떤 상태입니까?</td><td>바닥에 쓰러져 있습니다. / 손이 기계에 끼여 있습니다.</td></tr>
  </table>
  {sechead('A','질문에 알맞은 답을 고르십시오.')}
  <div class="left" style="font-size:15px; line-height:4.1; margin-bottom:{SP_XL}px;">
    ① 의식이 있습니까? → ( 네, 쓰러져 있습니다 · 네, 눈을 뜨고 말을 합니다 )<br>
    ② 어떤 상태입니까? → ( 제2공장입니다 · 다리에 화상을 입었습니다 )</div>
  {sechead('B','답을 완성해 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:4.15;">
    ① 피가 많이 납니까? → 손에서 피가 {blank(6)}<br>
    ② 환자가 어떤 상태입니까? → 바닥에 {blank(6)}</div>
  {foot(5)}"""
page("어휘확장1", p5)

# ═══ 6쪽 확장② — 함께 쓰는 말 ═══
def collo(a, b, m, e):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:24px 18px;">
      <div style="font-size:17px; font-weight:800; color:{DEEP};">{a} <span style="color:{LIGHT};">+</span> {b}</div>
      <div style="font-size:13.5px; margin-top:5px; line-height:1.6;">{m}</div>
      <div style="font-size:12.5px; color:{SUB}; border-top:1px dashed {HAIR}; margin-top:12px; padding-top:11px; line-height:1.7;">{e}</div></div>'''

p6 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ② — 함께 쓰는 말')}
  <div class="prose" style="margin-bottom:24px;">신고의 말도 짝으로 다닙니다. 네 짝이면 신고 전화 하나를 처음부터 끝까지 말할 수 있습니다.</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:26px; margin-bottom:{SP_XL}px;">
    {collo('사고를','신고하다','119에 알리는 것입니다.','발견하는 즉시 <b>신고합니다</b>.')}
    {collo('구조를','요청하다','구해 달라고 부탁하는 것입니다. (8과 요청)','<b>구조를 요청</b>합니다. 빨리 와 주세요.')}
    {collo('부상을','입다','다쳤다는 뜻의 짝입니다.','한 명이 <b>부상을 입었습니다</b>.')}
    {collo('의식이','있다·없다','깨어 있는지를 말하는 짝입니다.','<b>의식은 있습니다</b>. 말도 합니다.')}
  </div>
  {sechead('A','알맞은 짝을 골라 문장을 완성하십시오.')}
  <div class="wbank" style="margin-bottom:26px;">신고 · 요청 · 부상 · 의식</div>
  <div class="left" style="font-size:15px; line-height:4.05;">
    ① 사고를 발견하고 바로 119에 {blank(4)}하였습니다.<br>
    ② 동료가 팔에 {blank(4)}을 입었습니다.<br>
    ③ 환자는 {blank(4)}이 없습니다. 빨리 와 주세요.<br>
    ④ 상황실에 구조를 {blank(4)}하였습니다.</div>
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

IMG_TWO = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <rect x="6" y="18" width="42" height="28" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="4"/>
  <text x="27" y="36" text-anchor="middle" font-size="11" font-weight="bold" fill="{NAVY}">나고 있다</text>
  <rect x="52" y="54" width="42" height="28" rx="4" fill="{NAVY}"/>
  <text x="73" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">쓰러져 있다</text>
  <path d="M27 50 v8 q0 8 8 8 h13" fill="none" stroke="{SUB}" stroke-width="4" stroke-linecap="round"/></svg>'''
IMG_SPEAKER = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <path d="M20 40 h14 l18 -14 v48 l-18 -14 h-14 Z" fill="{NAVY}"/>
  <path d="M62 36 a18 18 0 0 1 0 28 M70 28 a30 30 0 0 1 0 44" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/></svg>'''
IMG_PHONE119 = f'''<svg width="96" height="96" viewBox="0 0 100 100">
  <rect x="28" y="8" width="44" height="84" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="5"/>
  <text x="50" y="42" text-anchor="middle" font-size="19" font-weight="bold" fill="{NAVY}">119</text>
  <line x1="38" y1="56" x2="62" y2="56" stroke="{HAIR}" stroke-width="4"/>
  <line x1="38" y1="66" x2="62" y2="66" stroke="{HAIR}" stroke-width="4"/>
  <circle cx="50" cy="82" r="4" fill="{NAVY}"/></svg>'''

p7 = gcard('1', '-고 있다 ↔ -아/어 있다', IMG_TWO,
  '피가 <b>나고 있습니다</b>. 동료가 바닥에 <b>쓰러져 있습니다</b>.', '119 신고 전화',
  """상황을 눈에 보이는 대로 말하는 두 꼴입니다. 계속되는 움직임은 <b>-고 있다</b>입니다. 끝난 뒤 남은 모습은 <b>-아/어 있다</b>입니다.""",
  '비교 · 나란히 놓으면 보입니다',
  f"""· 피가 <b>나고 있다</b> — 지금도 계속 나옵니다. (움직임)<br>
      · 쓰러<b>져 있다</b> — 쓰러진 뒤 그대로입니다. (모습)<br>
      · 손이 끼<b>여 있다</b> — 끼인 채 그대로입니다. 5과의 '끼이다'가 여기서 다시 나옵니다.""",
  f"""<span class="x">✗ 동료가 쓰러지고 있습니다.</span> (지금 넘어지는 중이라는 뜻이 됩니다)<br>
      ○ 동료가 쓰러<b>져 있습니다</b>.<br>
      <span style="font-size:13px; color:{SUB};">이미 일어난 일의 모습은 -아/어 있다로 말합니다.</span>""",
  f"""보이는 대로 말해 보십시오.<br>
      {enc('①')} (팔에서 피가 계속 나옴) → 피가 {blank(6)}<br>
      {enc('②')} (환자가 바닥에 누운 모습) → 바닥에 {blank(6)}<br>
      {enc('③')} (손이 기계에 낀 모습) → 손이 기계에 {blank(6)}""", lv='기본')
page("문형1", p7 + foot(7))

p8 = gcard('2', '-아/어 주시기 바랍니다', IMG_SPEAKER,
  '전 직원은 즉시 비상구로 대피해 <b>주시기 바랍니다</b>.', '사내 비상 방송',
  """부탁을 격식 있게 하는 꼴입니다. 비상 방송과 안내문이 이 꼴로 말합니다. 방송이 들리면 <b>그대로 행동</b>하면 됩니다 — 알아듣는 것이 곧 안전입니다.""",
  '비교 · 부탁의 세 단계',
  f"""· 신고 전화에서 — 빨리 와 <b>주세요</b>. (짧고 빠르게)<br>
      · 방송·안내문에서 — 대피해 <b>주시기 바랍니다</b>. (격식)<br>
      · 2과에서 배운 지시 — 대피하<b>십시오</b>. (위에서 아래로) — 부탁이 아니라 지시입니다.""",
  f"""<span class="x">✗ (119에 전화해서) 구급차를 보내 주시기 바랍니다.</span><br>
      ○ 구급차를 빨리 보내 <b>주세요</b>.<br>
      <span style="font-size:13px; color:{SUB};">급할 때는 짧은 말이 맞는 말입니다. 격식형은 방송과 문서의 말입니다.</span>""",
  f"""{enc('①')} (방송) 화재가 발생하였습니다. 즉시 대피해 {blank(8)}.<br>
      {enc('②')} (방송) 엘리베이터를 이용하지 말아 {blank(8)}.<br>
      {enc('③')} (신고 전화) 구급차를 빨리 {blank(6)}.""")
page("문형2", p8 + foot(8))

p9 = gcard('3', '-(으)ㄴ/는데요', IMG_PHONE119,
  '여기 ○○공단 ○○정밀 제2공장<b>인데요</b>, 사람이 다쳤습니다.', '119 신고 첫 문장',
  """말을 시작할 때 배경을 먼저 놓는 꼴입니다. 신고 전화의 첫 문장이 이 꼴입니다. 위치를 먼저 놓고, 본론으로 들어갑니다.""",
  '비교 · 신고의 순서 공식',
  f"""<b>[위치]인데요</b> → [무슨 일] → [인원·상태]<br>
      "제2공장<b>인데요</b>, 끼임 사고가 <b>발생했습니다</b>.(10과) 다친 사람은 한 명이고, 의식은 있습니다."<br>
      이 세 문장이 기말 말하기 90초의 뼈대입니다.""",
  f"""<span class="x">✗ 여기 제2공장입니다만,</span> (문서의 말입니다)<br>
      ○ 여기 제2공장<b>인데요</b>,<br>
      <span style="font-size:13px; color:{SUB};">전화에서는 -인데요가 자연스럽습니다.</span>""",
  f"""{enc('①')} 여기 ○○식품 포장동{blank(5)}, 사고가 났습니다.<br>
      {enc('②')} 동료가 다쳤{blank(5)}, 구급차를 보내 주세요.<br>
      {enc('③')} (내 일터로) 여기 {blank(10)}인데요, {blank(10)}""", lv='기본')
page("문형3", p9 + foot(9))

# ═══ 10쪽 문형 종합 ═══
p10 = f"""{head_sec('2교시 · 문형', '문형 종합')}
  {sechead('A','그림처럼 보이는 상황을 말로 바꾸십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.95;">
    {enc('①')} (연기가 계속 나옴) → 창고에서 연기가 {blank(6)}<br>
    {enc('②')} (동료가 바닥에 누워 움직이지 않음) → 동료가 {blank(8)}</div>
  {sechead('B','방송을 듣고 할 일을 고르십시오.')}
  <div class="lawq" style="margin-bottom:16px; font-size:14.5px; line-height:2.0; padding:16px 18px; background:#FBFCFE; border:1px solid {HAIR}; border-radius:6px;">"안내 말씀 드립니다. 2공장에서 화재가 발생하였습니다. 전 직원은 작업을 멈추고 즉시 비상구로 대피해 주시기 바랍니다. 엘리베이터는 이용하지 말아 주시기 바랍니다."</div>
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.9;">
    {enc('①')} 지금 해야 할 일: ( 계속 작업한다 · 비상구로 대피한다 )<br>
    {enc('②')} 하지 말아야 할 일: ( 계단 이용 · 엘리베이터 이용 )</div>
  {sechead('C','신고 전화를 완성하십시오. (세 문장)')}
  <div class="drill left" style="font-size:15px; line-height:3.8;">
    여기 {blank(12)}인데요, {blank(8)} 사고가 발생했습니다.<br>
    다친 사람은 {blank(4)}이고, {blank(14)}.<br>
    구급차를 빨리 {blank(8)}.</div>
  {foot(10)}"""
page("문형종합", p10)

print(f"[2/3] {len(PAGES)}쪽")

# ═══ 11쪽 실물 — 신고 담화 + 행동 수칙 ═══
SPEAKER_C = {'신고자': NAVY, '상황실': '#0F766E'}
def srow(who, text):
    c = SPEAKER_C.get(who, NAVY)
    return (f'<div style="display:flex;gap:14px;margin-bottom:22px;align-items:flex-start;">'
            f'<span style="flex:none;font-weight:800;color:{c};width:64px;padding-top:1px;">{who}</span>'
            f'<span style="line-height:1.85;flex:1;">{text}</span></div>')

def ruleline(n, t):
    return f'''<div style="display:flex; gap:11px; margin-bottom:17px; align-items:flex-start;">
      <span class="enc">{n}</span><div style="flex:1; font-size:14px; line-height:1.7;">{t}</div></div>'''

p11 = f"""{head_sec('3교시 · 읽기', '실물 자료 읽기')}
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[가] 119 신고 전화 — 제2공장 끼임 사고</div>
  <div style="border:1.2px solid {HAIR};border-radius:9px;padding:22px 26px 8px;margin-bottom:6px;font-size:15px;">
    {srow('상황실','"119입니다. 무엇을 도와드릴까요?"')}
    {srow('신고자','"여기 ○○공단 ○○정밀 제2공장<b>인데요</b>, 프레스에 끼임 사고가 <b>발생했습니다</b>."')}
    {srow('상황실','"다친 분이 몇 명입니까?"')}
    {srow('신고자','"한 명입니다. 손이 기계에 <b>끼여 있습니다</b>."')}
    {srow('상황실','"환자가 의식이 있습니까?"')}
    {srow('신고자','"네, 의식은 있습니다. 그런데 피가 많이 <b>나고 있습니다</b>."')}
    {srow('상황실','"구급대가 출동했습니다. 환자를 옮기지 마시고 기다려 주세요."')}
    {srow('신고자','"네, 알겠습니다. 빨리 와 <b>주세요</b>."')}
  </div>
  <div class="lnote" style="font-size:11.5px; color:{SUB}; margin-bottom:18px;">119 신고 요령(위치·인원·상태 전달)의 문답 구조를 제조 현장 상황으로 재구성함</div>
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[나] 응급 행동 수칙 — 현장 게시문</div>
  <div style="border:1.5px solid {NAVY}; border-radius:8px; padding:24px 24px; margin-bottom:6px;">
    {ruleline('①','<b>침착</b>하게 행동합니다. 당황하면 아는 것도 못 합니다.')}
    {ruleline('②','혼자 해결하려 하지 말고 즉시 119에 <b>신고</b>합니다. 구급대는 접수 후 5분 안에 출동합니다.')}
    {ruleline('③','환자를 함부로 옮기지 않습니다. 무리하게 옮기면 부상이 나빠질 수 있습니다. 구급대를 기다립니다.')}
    {ruleline('④','말이 어려우면 <b>문자·사진·앱</b>으로 신고합니다. 그림을 누르면 위치와 함께 신고됩니다.')}
  </div>
  <div class="lnote" style="font-size:11.5px; color:{SUB};">국민재난안전포털 응급처치 요령·119 다매체 신고 안내를 교육용으로 재구성함</div>
  {foot(11)}"""
page("실물자료읽기", p11)

# ═══ 12쪽 읽고 답하기 ═══
p12 = f"""{head_sec('3교시 · 읽기', '읽고 답하기')}
  <div class="tintbox" style="margin-bottom:{SP_M}px; font-size:14px;">11쪽의 신고 전화와 수칙을 다시 보면서 답하십시오.</div>
  {sechead('A','기본 — 맞으면 ○, 틀리면 ✗를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.75;">
    {enc('①')} 신고자는 위치를 가장 먼저 말했다. ( {blank(2)} )<br>
    {enc('②')} 구급대가 오기 전에 환자를 빨리 옮겨야 한다. ( {blank(2)} )<br>
    {enc('③')} 말이 어려우면 사진으로도 신고할 수 있다. ( {blank(2)} )</div>
  {sechead('B','심화 — 대화에서 찾아 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.7;">
    {enc('①')} 신고자가 '상태'를 말한 문장 두 개를 찾아 쓰십시오.<br>
    → {blank(20)}<br>
    → {blank(20)}<br>
    {enc('②')} 상황실이 신고자에게 하지 말라고 한 것은 무엇입니까?<br>
    → {blank(16)}</div>
  {sechead('C','확장 — 생각을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    신고자는 긴 말을 하지 않았습니다. 그런데도 신고가 잘 되었습니다. 왜 그렇습니까?<br>
    → {blank(26)}</div>
  {foot(12)}"""
page("읽고답하기", p12)

# ═══ 13쪽 연습 ═══
p13 = f"""{head_sec('3교시 · 읽기', '연습 — 상황을 신고로')}
  {sechead('A','상황을 읽고 신고 3정보를 정리하십시오.')}
  <div class="tintbox" style="margin-bottom:16px; font-size:14.5px; line-height:1.9;">포장동에서 지게차 화물이 낙하하여 동료 한 명이 어깨를 다쳤습니다. 동료는 앉아서 말을 하고 있지만, 어깨를 움직이지 못합니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:110px;height:6px;">정보</th><th>말할 내용</th></tr>
    <tr><td>① 위치</td><td>{blank(16)}</td></tr>
    <tr><td>② 인원</td><td>{blank(10)}</td></tr>
    <tr><td>③ 상태</td><td>의식은 {blank(4)} · 어깨를 {blank(8)}</td></tr>
  </table>
  {sechead('B','신고 전화의 첫 문장을 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.3;">
    여기 {blank(10)}{blank(4)}, 낙하 사고가 {blank(8)}.<br>{blank(30)}</div>
  {sechead('C','상황실의 질문에 답하십시오.')}
  <div class="drill left" style="font-size:15px; line-height:3.5;">
    {enc('①')} "환자가 의식이 있습니까?" → {blank(14)}<br>
    {enc('②')} "피가 납니까?" → 아니요, {blank(12)}</div>
  {foot(13)}"""
page("연습", p13)

# ═══ 14쪽 상황 말하기·쓰기 (기말 예행) ═══
p14 = f"""{head_sec('3교시 · 쓰기', '상황 말하기 — 나의 신고문')}
  <div class="prose" style="margin-bottom:16px;">기말 말하기(사진을 보고 90초 음성)의 예행입니다. 내 일터(또는 실습장)를 상황으로 정해, 신고문을 쓰고 소리 내어 읽으십시오.</div>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">신고문 공식 — 세 문장 + 한 마디</div>
    <div style="font-size:14.5px; line-height:2.15;">여기 [위치]<b>인데요</b>, [무슨] 사고가 <b>발생했습니다</b>.<br>다친 사람은 [인원]이고, [상태 — -고 있다 / -아 있다].<br>구급차를 빨리 보내 <b>주세요</b>.</div>
  </div>
  {sechead('A','나의 신고문을 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_M}px; font-size:15px; line-height:4.35;">
    ① 여기 {blank(30)}<br>
    ② {blank(34)}<br>
    ③ {blank(34)}</div>
  {sechead('B','소리 내어 세 번 읽으십시오.')}
  <div class="left" style="font-size:14.5px; line-height:2.1; margin-bottom:{SP_M}px;">☐ 1회 — 보면서 천천히 &nbsp;&nbsp; ☐ 2회 — 보면서 빠르게 &nbsp;&nbsp; ☐ 3회 — 안 보고 말하기</div>
  <div style="height:14px;"></div>
  <div class="caution" style="font-size:14px; line-height:1.95; padding:16px 18px;">
    <b>제출</b> · 완성한 신고문을 이번 주 <b>LMS 과제방</b>에 제출합니다. 이 문장은 <b>기말 말하기 90초</b>의 뼈대이자, 과제③(14주)의 재료입니다.</div>
  {foot(14)}"""
page("상황쓰기", p14)

# ═══ 15쪽 정리 ═══
def npill(t):
    return f'<div style="margin-bottom:12px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:13px;font-weight:800;height:29px;line-height:29px;padding:0 16px;">{t}</span></div>'
vgrid12 = ''.join(f'<div style="border:1px solid {HAIR};border-radius:6px;padding:8px 12px;font-size:13.5px;">☐ {w}</div>'
    for w in ['신고','부상','응급','구조','위치','인원','상태','환자','의식','출혈','화상','침착'])

p15 = f"""{head_sec('3교시 · 읽기', '정리')}
  <div style="display:flex;flex-direction:column;gap:10px;font-size:15px;line-height:1.55;margin-bottom:14px;">
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">1</span><span style="padding-top:2px;">신고는 세 마디다 — <b>위치 · 인원 · 상태</b>. 상황실이 물으면 침착하게 답한다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">2</span><span style="padding-top:2px;">움직임은 <b>-고 있다</b>, 남은 모습은 <b>-아/어 있다</b> — 보이는 대로 말한다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">3</span><span style="padding-top:2px;">환자를 옮기지 않는다 · 말이 어려우면 <b>문자·사진·앱</b>으로 신고한다.</span></div>
  </div>
  <div style="border-top:1px solid {HAIR};margin-bottom:16px;"></div>
  {npill('자가 점검 ① 체크리스트')}
  <div class="left" style="display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;font-size:14.5px;line-height:1.55;margin-bottom:{SP_M}px;">
    <div>☐ 신고 3정보를 순서대로 말할 수 있다</div>
    <div>☐ -고 있다와 -아 있다를 구별해 쓸 수 있다</div>
    <div>☐ 비상 방송을 듣고 할 일을 안다</div>
    <div>☐ 내 일터의 위치를 한국어로 말할 수 있다</div>
    <div>☐ 신고문 세 문장을 안 보고 말할 수 있다</div>
  </div>
  {npill('자가 점검 ② 문제로 확인')}
  <div class="left" style="font-size:15px;line-height:2.1;margin-bottom:{SP_M}px;">
    ① 신고의 세 정보를 순서대로 쓰십시오. → {blank(12)}<br>
    ② (동료가 바닥에 누워 있는 모습) → 동료가 바닥에 {blank(6)}<br>
    ③ 다음 중 <u>틀린</u> 문장을 고르십시오. ( {blank(2)} )<br>
    <span style="display:block; padding-left:26px; font-size:14.5px; line-height:1.8;">㉮ 피가 나고 있습니다.<br>㉯ 손이 기계에 끼여 있습니다.<br>㉰ (119에 전화해서) 구급차를 보내 주시기 바랍니다.</span>
    ④ '동료가 <span class="x">쓰러지고 있습니다</span>'를 바르게 고치십시오. → 동료가 {blank(6)}<br>
    ⑤ 말이 어려울 때 신고하는 방법 하나를 쓰십시오. → {blank(10)}</div>
  {npill('10초 어휘 셀프 체크')}
  <div style="font-size:13px;color:{SUB};margin-bottom:10px;">각 단어의 뜻이 3초 안에 떠오르지 않으면 ☐에 ✔ 하십시오. ✔한 단어는 2쪽으로 돌아가 예문과 함께 다시 읽으십시오.</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">{vgrid12}</div>
  {foot(15)}"""
page("정리", p15)

html = HEAD + '<body>' + ''.join(PAGES) + '</body></html>'
open('/home/claude/sik/ch11_full_15pages.html', 'w', encoding='utf-8').write(html)
print(f"[3/3] {len(PAGES)}쪽")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file:///home/claude/sik/ch11_full_15pages.html')
    pg.wait_for_timeout(1200)
    pg.pdf(path='/home/claude/sik/ch11.pdf', width='794px', height='1123px', print_background=True, page_ranges='1-15')
    b.close()
print("PDF ok")
