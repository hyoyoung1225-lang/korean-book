# -*- coding: utf-8 -*-
"""build_ch8.py — 산업안전한국어 제8과 「작업 중지와 거절」 (3부 권리 · 10주차 · Q8)
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
table.cellwide td{{padding:16px 12px !important;}}
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

FOOT_L = "산업안전한국어 · 3부 권리 제8과 작업 중지와 거절"
def foot(n): return footer(FOOT_L, f"{n:02d}")
def enc(t): return f'<span class="enc">{t}</span>'
PAGES = []
def page(label, body):
    PAGES.append(f'<div class="page" data-document-role="page" data-label="{label}">{body}</div>')

# ═══ 픽토 4종 — 8과 절차 (부 중간 과: 3부 라벨·틀 계승, 픽토는 과 내용) ═══
def picto_eye():   # 발견
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M22 50 q28 -26 56 0 q-28 26 -56 0 Z" fill="#fff"/><circle cx="50" cy="50" r="11" fill="{NAVY}"/></svg>'''
def picto_stop():  # 중지 = 팔각 STOP 표지
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M36 22 h28 l14 14 v28 l-14 14 h-28 l-14 -14 v-28 Z" fill="#fff"/>
      <text x="50" y="56" text-anchor="middle" font-size="15" font-weight="bold" fill="{NAVY}">STOP</text></svg>'''
def picto_no():    # 거절 = 말풍선 ✗ (말로 하는 거절)
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M26 30 h48 v30 h-28 l-11 11 v-11 h-9 Z" fill="#fff"/>
      <path d="M43 38 l14 14 M57 38 l-14 14" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/></svg>'''
def picto_redo():  # 확인 후 재개
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M67 42 a20 20 0 1 0 4 16" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
      <path d="M67 26 v16 h-16" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

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
      <div><span style="display:inline-block;background:{pillbg};color:#fff;font-size:12.5px;font-weight:800;letter-spacing:.1em;padding:6px 15px;border-radius:15px;">{pilltxt}</span></div>
      <div style="font-size:12px;color:{SUB};line-height:1.6;margin-top:9px;">{c1}<br>{c2}</div></div>'''
CHEV = '<div style="color:#C4CBD7;font-size:15px;margin-top:26px;">〉</div>'

# ═══ 1쪽 도비라 (1과·7과 검증 구성 승계 · 3부 계승) ═══
dobira = f"""
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid {NAVY};padding-bottom:11px;">
    <span style="font-size:13px;font-weight:700;letter-spacing:.5em;color:{INK};">산업안전한국어</span>
    <span style="font-size:13px;font-weight:800;letter-spacing:.14em;color:{NAVY};">3부 · 권리</span>
  </div>
  <div style="display:flex;gap:26px;margin-top:34px;">
    <div style="flex:1;padding-top:20px;">
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:118px;font-weight:900;color:{NAVY};line-height:.95;">08</div>
      <div style="margin-top:14px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:12.5px;font-weight:800;letter-spacing:.34em;padding:7px 16px 7px 20px;">제 8 과</span></div>
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:42px;font-weight:900;color:{INK};margin-top:22px;">작업 중지와 거절</div>
    </div>
    <div style="flex:none;width:322px;height:462px;position:relative;background:#E7EDF6;overflow:hidden;">
      <div style="position:absolute;top:120px;left:24px;width:56px;height:400px;background:#D8E1EF;"></div>
      <div style="position:absolute;top:230px;right:16px;width:70px;height:300px;background:#D1DBEC;"></div>
      <div style="position:absolute;top:-70px;left:150px;width:52px;height:640px;background:{NAVY};transform:rotate(16deg);"></div>
      <div style="position:absolute;top:52px;left:34px;right:34px;background:#fff;border-radius:16px;box-shadow:0 10px 26px rgba(20,35,80,.16);padding:26px 20px;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;justify-items:center;">
          {picto_eye()}{picto_stop()}{picto_no()}{picto_redo()}</div></div>
    </div>
  </div>
  <div style="display:flex;gap:26px;margin-top:40px;">
    <div style="flex:1.06;">
      <div style="display:flex;align-items:center;gap:9px;margin-bottom:16px;">
        {G_TARGET}<span style="font-size:16px;font-weight:800;color:{INK};">학습 목표</span>
        <div style="flex:1;border-top:1px solid {HAIR};"></div></div>
      <div style="display:flex;flex-direction:column;gap:13px;font-size:14.5px;line-height:1.6;">
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">1</span><span style="padding-top:2px;">"<b>우려가 있으므로 중지하겠습니다</b>"라고 격식체로 말합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">2</span><span style="padding-top:2px;">무리한 요구를 <b>조건을 붙여</b> 정중하게 거절합니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">3</span><span style="padding-top:2px;">조치 완료 <b>여부를 확인</b>한 후에 작업을 재개합니다.</span></div>
      </div>
    </div>
    <div style="flex:1;background:#EDF2FA;border-radius:12px;padding:20px 24px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px;">
        {G_BULB}<span style="font-size:15px;font-weight:800;color:{INK};">생각해 보기</span></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">기계가 이상한데 물량이 급합니다. 뭐라고 말하겠습니까?</div>
      <div style="border-top:1px dashed #C9D2E2;margin:11px 0;"></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">"그냥 계속하세요"라는 말을 들으면, 어떻게 거절하겠습니까?</div>
    </div>
  </div>
  <div style="display:flex;justify-content:center;align-items:flex-start;gap:4px;margin-top:42px;">
    {kcol(G_TALK,'1교시 · 어휘',NAVY,'핵심 어휘 12개 + 연습','중지 절차의 말')}
    {CHEV}
    {kcol(G_AA,'2교시 · 문형',LIGHT,'우려가 있으므로 · -기 전에는','N 여부 확인 + 종합')}
    {CHEV}
    {kcol(G_BOOK,'3교시 · 읽기',DEEP,'절차 안내문 + 현장 대화','중지 통보문 쓰기 + 정리')}
  </div>
  <div style="position:absolute;top:{FOOTER_Y}px;left:64px;right:64px;border-top:1px solid {HAIR};padding-top:12px;display:flex;justify-content:space-between;align-items:center;">
    <span style="display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800;color:{INK};">
      {G_SHIELD} 멈춘다고 말하는 것 — 그것도 권리입니다.</span>
    <span style="font-size:13px;font-weight:800;color:{NAVY};">01</span>
  </div>"""
page("도비라", dobira)

# ═══ 2쪽 핵심 어휘 12 ═══
V = [
 ("거절","기본","하지 않겠다고 말하는 것입니다.","위험한 지시는 <b>거절</b>할 수 있습니다."),
 ("요청","기본","해 달라고 부탁하는 것입니다.","수리를 <b>요청</b>드립니다."),
 ("상급자","기본","나보다 위에 있는 사람입니다. 반장님, 팀장님입니다.","<b>상급자</b>에게 바로 알립니다."),
 ("즉시","기본","바로, 그 자리에서라는 뜻입니다.","위험하면 <b>즉시</b> 멈춥니다."),
 ("발견","기본","찾아서 알게 되는 것입니다.","위험을 <b>발견</b>하면 작업을 중지합니다."),
 ("동료","기본","같이 일하는 사람입니다.","<b>동료</b>의 위험도 중지 사유가 됩니다."),
 ("판단","기본","생각해서 결정하는 것입니다.","위험한지 스스로 <b>판단</b>합니다."),
 ("재개","기본","멈춘 일을 다시 시작하는 것입니다.","확인한 후에 작업을 <b>재개</b>합니다."),
 ("행사","심화","권리를 실제로 쓰는 것입니다.","작업중지권을 <b>행사</b>하였습니다."),
 ("통보","심화","공식적으로 알리는 것입니다.","중지 사실을 <b>통보</b>하였습니다."),
 ("불이익","심화","나에게 손해가 되는 대우입니다.","중지를 이유로 <b>불이익</b>을 줄 수 없습니다."),
 ("손실","심화","잃어버린 돈이나 시간입니다.","중지로 인한 <b>손실</b>은 회사가 부담합니다."),
]
v_cards = ''.join(vcard(w, lv, m, e) for w, lv, m, e in V)
p2 = f"""{head_sec('1교시 · 어휘', '핵심 어휘 12')}
  <div style="display:flex; align-items:center; gap:8px; font-size:13px; color:{SUB}; margin-bottom:16px;">
    <span class="lv b">기본</span><span>모든 학생 필수</span>
    <span class="lv a" style="margin-left:10px;">심화</span><span>법규·보고서의 문어 표현 — 읽고 이해할 수 있으면 충분합니다.</span></div>
  <div class="vgrid" style="gap:16px;">{v_cards}</div>
  {foot(2)}"""
page("핵심어휘", p2)

# ═══ 3쪽 어휘 연습 (1과 형식) ═══
p3 = f"""{head_sec('1교시 · 어휘', '어휘 연습')}
  {sechead('A','알맞은 단어를 골라 빈칸을 채우십시오.')}
  <div class="wbank" style="margin-bottom:22px;">판단 · 통보 · 재개 · 불이익</div>
  <div class="left" style="font-size:15px; line-height:2.75; margin-bottom:{SP_XL}px;">
    ① 위험한지 스스로 {blank(5)}하여 작업을 중지할 수 있습니다.<br>
    ② 작업을 중지하였으면 관리감독자에게 {blank(5)}합니다.<br>
    ③ 조치가 끝난 후에 작업을 {blank(5)}합니다.<br>
    ④ 작업을 중지하였다는 이유로 {blank(6)}을 줄 수 없습니다.</div>
  {sechead('B','짝이 되는 말을 선으로 연결하십시오.')}
  <div style="margin-bottom:{SP_XL}px;">
  {connect(
    ["① 위험을", "② 권리를", "③ 여부를", "④ 중지를", "⑤ 작업을"],
    ["㉠ 행사하다", "㉡ 재개하다", "㉢ 발견하다", "㉣ 통보하다", "㉤ 확인하다"],
    lw=150, rw=230, rowgap=34)}
  </div>
  {sechead('C','B에서 연결한 표현 중 두 개를 골라 문장을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.4;">
    ① {blank(40)}<br>
    ② {blank(40)}</div>
  {foot(3)}"""
page("어휘연습", p3)

# ═══ 4쪽 개념 — 중지 절차 5단계 지도 ═══
def stepcard(pic, num, title, desc):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:19px 18px; display:flex; gap:18px; align-items:center;">
      <div style="flex:none;">{pic}</div>
      <div style="flex:1;">
        <div style="display:flex; align-items:baseline; gap:10px;">
          <span class="enc">{num}</span><span style="font-weight:800; font-size:16px; color:{DEEP};">{title}</span></div>
        <div style="font-size:14px; line-height:1.6; margin-top:5px;">{desc}</div></div></div>'''

p4 = f"""{head_sec('1교시 · 어휘', '작업 중지의 다섯 단계')}
  <div class="prose" style="margin-bottom:24px;">작업 중지는 한 번의 말이 아니라 절차입니다. 다섯 단계를 순서대로 기억합니다. 이번 과의 어휘가 이 지도 위에 있습니다.</div>
  <div style="display:flex; flex-direction:column; gap:18px; margin-bottom:{SP_L}px;">
    {stepcard(picto_eye(),'①','발견', '위험을 발견합니다. 내 위험도, 동료의 위험도 됩니다.')}
    {stepcard(picto_stop(),'②','중지·통보', '즉시 멈추고, 지체 없이 상급자에게 통보합니다.')}
    {stepcard(picto_no(),'③','거절', '조치 전에 계속하라는 요구는 정중하게 거절합니다.')}
    {stepcard(picto_redo(),'④','확인·재개', '조치 완료 여부를 확인한 후에 작업을 재개합니다.')}
  </div>
  <div class="tintbox">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">7과와 이어집니다</div>
    <div style="font-size:14.5px; line-height:1.85;">7과에서 이 권리를 <b>법(제52조)</b>으로 읽었습니다. 8과에서는 같은 권리를 <b>말과 문서</b>로 씁니다. 법이 준 권리는 말할 수 있을 때 내 것이 됩니다.</div>
  </div>
  {foot(4)}"""
page("개념", p4)

# ═══ 5쪽 어휘 확장 ① — 절차의 말 ═══
p5 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ① — 누가, 무엇을 합니까?')}
  <div class="prose" style="margin-bottom:18px;">중지 절차의 단계마다 하는 사람과 하는 일이 정해져 있습니다. 주어를 보면서 표를 읽습니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_XL}px;">
    <tr><th style="width:110px;">단계</th><th style="width:120px;">누가</th><th>무엇을</th></tr>
    <tr><td>발견·판단</td><td><b>나</b></td><td>위험을 발견하고 스스로 판단합니다.</td></tr>
    <tr><td>중지·통보</td><td><b>나</b></td><td>즉시 중지하고 상급자에게 통보합니다.</td></tr>
    <tr><td>조치</td><td><b>회사</b></td><td>위험 요인을 즉시 확인하고 조치합니다.</td></tr>
    <tr><td>확인·재개</td><td><b>나 + 회사</b></td><td>조치 완료 여부를 확인한 후에 재개합니다.</td></tr>
  </table>
  {sechead('A','알맞은 사람을 고르십시오.')}
  <div class="left" style="font-size:15px; line-height:3.15; margin-bottom:{SP_XL}px;">
    ① 위험한지 판단하는 사람 ( 나 · 회사 · 나와 회사 )<br>
    ② 위험 요인을 조치하는 쪽 ( 나 · 회사 · 나와 회사 )<br>
    ③ 조치 완료 여부를 확인하는 쪽 ( 나 · 회사 · 나와 회사 )</div>
  {sechead('B','문장을 완성해 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.1;">
    ① 위험을 발견하면 즉시 {blank(10)}.<br>
    ② 중지한 사실을 상급자에게 {blank(10)}.<br>
    ③ 조치가 끝난 후에 작업을 {blank(10)}.</div>
  {foot(5)}"""
page("어휘확장1", p5)

# ═══ 6쪽 어휘 확장 ② — 함께 쓰는 말 ═══
def collo(a, b, m, e):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:24px 18px;">
      <div style="font-size:17px; font-weight:800; color:{DEEP};">{a} <span style="color:{LIGHT};">+</span> {b}</div>
      <div style="font-size:13.5px; margin-top:5px; line-height:1.6;">{m}</div>
      <div style="font-size:12.5px; color:{SUB}; border-top:1px dashed {HAIR}; margin-top:12px; padding-top:11px; line-height:1.7;">{e}</div></div>'''

p6 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ② — 함께 쓰는 말')}
  <div class="prose" style="margin-bottom:24px;">권리의 말도 짝과 함께 다닙니다. 짝을 통째로 기억하면 문서와 대화가 빨라집니다.</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-bottom:{SP_XL}px;">
    {collo('권리를','행사하다','권리를 실제로 쓴다는 뜻입니다. 문서의 말입니다.','작업중지권을 <b>행사</b>한 근로자')}
    {collo('불이익을','주다·받다','손해가 되는 대우를 한다는 뜻입니다.','중지를 이유로 <b>불이익을 줄</b> 수 없습니다.')}
    {collo('손실을','부담하다','손해를 책임진다는 뜻입니다.','중지로 인한 <b>손실은</b> 회사가 <b>부담</b>합니다.')}
    {collo('이상','유무','이상이 있는지 없는지를 말합니다. 점검표의 말입니다.','설비 <b>이상 유무</b>를 확인하였습니다.')}
  </div>
  {sechead('A','알맞은 짝을 골라 문장을 완성하십시오.')}
  <div class="wbank" style="margin-bottom:26px;">행사 · 불이익 · 손실 · 유무</div>
  <div class="left" style="font-size:15px; line-height:3.45;">
    ① 근로자는 작업중지권을 {blank(4)}할 수 있습니다.<br>
    ② 중지를 이유로 {blank(5)}을 주어서는 안 됩니다.<br>
    ③ 설비의 이상 {blank(4)}를 먼저 확인하십시오.<br>
    ④ 중지로 인한 {blank(4)}은 회사가 부담합니다.</div>
  {foot(6)}"""
page("어휘확장2", p6)

print(f"[1/3] 1교시 {len(PAGES)}쪽 구성")

# ═══ 7~9쪽 문형 카드 (1과식 헤더 · 7과 검증 구조) ═══
def pillrow(*ps):
    return '<div style="display:flex; gap:8px; margin:10px 0 4px 0;">' + ''.join(pill(t) for t in ps) + '</div>'

def gcard(num, title, site_img, quote, source, mean_html, comp_pill, comp_html, err_html, drill_html, wide=True, lv='심화', comb='동사'):
    sb, mm, cm, dl = (28, 20, 26, 3.0) if wide else (26, 18, 24, 2.95)
    return f"""<div style="display:flex; align-items:center; gap:13px; margin-bottom:18px;">
    <span class="num">{num}</span>
    <span class="formbig" style="white-space:nowrap;">{title}</span>
    <span class="lv {'b' if lv=='기본' else 'a'}">{lv}</span>
    <span style="margin-left:auto; font-size:13.5px; color:{SUB};">결합: <b style="color:{INK};">{comb}</b></span></div>
  <div style="margin-bottom:{sb}px;">{sitebox_img(site_img, quote, source)}</div>
  {pillrow('의미와 쓰임')}
  <div class="prose" style="margin-bottom:{mm}px;">{mean_html}</div>
  {pillrow(comp_pill)}
  <div style="font-size:14.5px; line-height:{1.8 if wide else 1.65}; margin-bottom:{mm}px;">{comp_html}</div>
  {pillrow('자주 하는 오류')}
  <div class="caution" style="font-size:14.5px; line-height:{2.0 if wide else 1.75}; margin-bottom:{cm}px;">{err_html}</div>
  {pillrow('연습')}
  <div class="drill left" style="font-size:15px; line-height:{dl};">{drill_html}</div>"""

IMG_MEMO = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <rect x="18" y="12" width="64" height="76" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="4"/>
  <rect x="26" y="22" width="48" height="7" fill="{NAVY}"/>
  <line x1="26" y1="40" x2="74" y2="40" stroke="{HAIR}" stroke-width="4"/>
  <line x1="26" y1="52" x2="74" y2="52" stroke="{HAIR}" stroke-width="4"/>
  <line x1="26" y1="64" x2="60" y2="64" stroke="{HAIR}" stroke-width="4"/></svg>'''
IMG_HANDX = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <path d="M34 14 h32 l20 20 v32 l-20 20 h-32 l-20 -20 v-32 Z" fill="#C62828" stroke="#fff" stroke-width="3"/>
  <text x="50" y="57" text-anchor="middle" font-size="17" font-weight="bold" fill="#fff">STOP</text></svg>'''
IMG_CHECK = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <rect x="14" y="16" width="72" height="68" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="4"/>
  <rect x="24" y="28" width="14" height="14" fill="none" stroke="{NAVY}" stroke-width="3"/>
  <path d="M26 34 l5 5 l8 -10" stroke="{NAVY}" stroke-width="4" fill="none"/>
  <line x1="46" y1="35" x2="76" y2="35" stroke="{HAIR}" stroke-width="4"/>
  <rect x="24" y="52" width="14" height="14" fill="none" stroke="{NAVY}" stroke-width="3"/>
  <line x1="46" y1="59" x2="76" y2="59" stroke="{HAIR}" stroke-width="4"/></svg>'''

# ── 7쪽 문형① ──
p7 = gcard('1', '-(으)ㄹ 우려가 있으므로 …-겠습니다', IMG_MEMO,
  '말려들 <b>우려가 있으므로</b> 작업을 중지<b>하겠습니다</b>.', '작업 중지 통보문',
  """중지를 선언하는 공식입니다. 앞에는 이유(<b>우려가 있으므로</b>), 뒤에는 나의 결정(<b>-겠습니다</b>)이 옵니다. 허락을 구하는 말이 아니라 권리를 쓰는 말입니다.""",
  '비교 · 말할 때와 쓸 때',
  f"""'우려'는 1과와 5과에서 배웠습니다. 이제 내 문장의 재료가 됩니다.<br>
      · 말할 때 — 우려가 있<b>어서</b> 중지하겠습니다.<br>
      · 통보문에 쓸 때 — 우려가 있<b>으므로</b> 중지하겠습니다.<br>
      · 조치를 부탁할 때 — 수리를 <b>요청드립니다</b>. (권리 행사와 구별)""",
  f"""<span class="x">✗ 우려가 있으니까 중지하겠습니다.</span><br>
      ○ 우려가 있<b>으므로</b> 중지하겠습니다.<br>
      <span style="font-size:13px; color:{SUB};">'-니까'는 대화의 말입니다. 통보문에는 '-으므로'를 씁니다.</span>""",
  f"""{enc('①')} 손이 끼일 {blank(8)} 작업을 중지하겠습니다.<br>
      {enc('②')} 부품이 떨어질 우려가 있으므로 {blank(10)}.<br>
      {enc('③')} (말→통보문) "감전될 것 같아서 멈추겠습니다." → 감전될 {blank(12)}""")
page("문형1", p7 + foot(7))

# ── 8쪽 문형② ──
p8 = gcard('2', '-기 전에는 -(으)ㄹ 수 없습니다', IMG_HANDX,
  '죄송하지만, 방호장치가 고쳐지<b>기 전에는</b> 작업<b>할 수 없습니다</b>.', '현장 대화',
  """조건을 붙여 거절하는 공식입니다. 무엇이 되기 <b>전에는</b> 할 수 <b>없다</b>고 말합니다. 조건이 있어서 정중하고, '없습니다'가 있어서 명확합니다. 앞에 "죄송하지만"을 붙이면 더 부드럽습니다.""",
  '비교 · 7과에서 배운 말',
  f"""7과에서 규정문의 <b>-ㄹ 수 없다</b>(금지)를 읽었습니다. 8과에서는 같은 형태로 내가 <b>거절</b>합니다. 읽던 말이 내 말이 됩니다.""",
  f"""<span class="x">✗ 좀 어려울 것 같습니다.</span> — 애매한 거절은 다시 요구가 옵니다.<br>
      ○ 고쳐지<b>기 전에는</b> 작업<b>할 수 없습니다</b>.<br>
      <span style="font-size:13px; color:{SUB};">안전 거절은 애매하게 말하지 않습니다. 조건을 말합니다.</span>""",
  f"""{enc('①')} 방호장치가 수리되{blank(5)} 라인을 켤 수 없습니다.<br>
      {enc('②')} 안전 확인이 끝나{blank(5)} 들어갈 수 없습니다.<br>
      {enc('③')} "그냥 계속하세요." → 죄송하지만, {blank(16)}""")
page("문형2", p8 + foot(8))

# ── 9쪽 문형③ ──
p9 = gcard('3', 'N 여부를 확인하다', IMG_CHECK,
  '조치 완료 <b>여부를 확인</b>한 후에 재개합니다.', '작업 재개 점검표',
  """<b>여부</b>는 '했는지 안 했는지'를 한 단어로 줄인 말입니다. 점검표와 보고서의 말입니다. 완료 여부, 작동 여부처럼 명사 뒤에 붙습니다.""",
  '비교 · 비슷한 말',
  f"""· 말할 때 — 조치가 끝났<b>는지</b> 확인하겠습니다.<br>
      · 문서에 쓸 때 — 조치 완료 <b>여부</b>를 확인하였습니다.<br>
      · <b>유무</b> — 있는지 없는지. "설비 이상 <b>유무</b> 확인" (5과 점검표에서 봤습니다)""",
  f"""<span class="x">✗ 완료했는지 여부를 확인합니다.</span><br>
      ○ 완료 <b>여부</b>를 확인합니다. / 완료했<b>는지</b> 확인합니다.<br>
      <span style="font-size:13px; color:{SUB};">'-는지'와 '여부'는 같은 일을 합니다. 둘 중 하나만 씁니다.</span>""",
  f"""{enc('①')} 방호장치 작동 {blank(4)}를 확인한 후에야 재개할 수 있습니다.<br>
      {enc('②')} 설비 이상 {blank(4)}를 점검하였습니다.<br>
      {enc('③')} (문서로) "다 고쳤는지 확인했어요." → 수리 완료 {blank(10)}""", wide=False, lv='심화', comb='명사')
page("문형3", p9 + foot(9))

# ═══ 10쪽 문형 종합 ═══
p10 = f"""{head_sec('2교시 · 문형', '문형 종합')}
  {sechead('A','말을 통보문으로 바꿔 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.95;">
    {enc('①')} "컨베이어에 말려들 것 같아서 멈출게요."<br>
    → 말려들 {blank(8)} 작업을 {blank(8)}<br>
    {enc('②')} "고치기 전엔 못 해요."<br>
    → 수리가 완료되{blank(5)} 작업{blank(8)}</div>
  {sechead('B','안내문에서 찾아 쓰십시오.')}
  <div class="lawq" style="margin-bottom:16px; font-size:14.5px; line-height:2.0; padding:16px 18px; background:#FBFCFE; border:1px solid {HAIR}; border-radius:6px;">위험을 발견한 근로자는 즉시 작업을 중지할 수 있습니다. 중지 사실을 관리감독자에게 통보합니다. 조치 완료 여부를 확인한 후에 작업을 재개합니다.</div>
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.8;">
    {enc('①')} '했는지 안 했는지'를 줄인 한 단어: {blank(4)}<br>
    {enc('②')} 재개의 조건이 되는 일: {blank(8)}</div>
  {sechead('C','미니 쓰기 — 한 문장으로 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.9;">
    내 작업장의 위험 하나로 중지 문장을 씁니다.<br>
    {blank(14)} 우려가 있으므로 {blank(14)}<br>
    {blank(30)}</div>
  {foot(10)}"""
page("문형종합", p10)

print(f"[2/3] 2교시까지 {len(PAGES)}쪽 구성")

# ═══ 11쪽 실물 읽기 — 절차 안내문 + 현장 대화 ═══
def stepline(n, t, d):
    return f'''<div style="display:flex; gap:11px; margin-bottom:16px; align-items:flex-start;">
      <span class="enc">{n}</span>
      <div style="flex:1;"><span style="font-weight:800; color:{DEEP};">{t}</span>
      <span style="font-size:14px;"> — {d}</span></div></div>'''

def bubble(who, cls, text):
    bg = TINT if cls=='me' else '#F4F5F8'
    return f'''<div style="display:flex; gap:10px; margin-bottom:12px;">
      <span style="flex:none; width:86px; font-size:12.5px; font-weight:800; color:{DEEP}; padding-top:8px;">{who}</span>
      <div style="flex:1; background:{bg}; border-radius:8px; padding:11px 14px; font-size:14px; line-height:1.7;">{text}</div></div>'''

SPEAKER_C = {'작업자': NAVY, '김 반장': '#0F766E', '동료': '#92400E'}
def srow(who, text):
    c = SPEAKER_C.get(who, NAVY)
    return (f'<div style="display:flex;gap:14px;margin-bottom:19px;align-items:flex-start;">'
            f'<span style="flex:none;font-weight:800;color:{c};width:64px;padding-top:1px;">{who}</span>'
            f'<span style="line-height:1.9;flex:1;">{text}</span></div>')
def scene(t):
    return f'<div style="text-align:center;color:{SUB};font-size:12px;margin:10px 0 20px;">— {t} —</div>'

p11 = f"""{head_sec('3교시 · 읽기', '실물 자료 읽기')}
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[가] 작업중지권 행사 절차 안내 — 현장 게시문</div>
  <div style="border:1.5px solid {NAVY}; border-radius:9px; padding:18px 22px; margin-bottom:6px;">
    <div style="text-align:center; font-weight:900; font-size:16px; color:{DEEP}; margin-bottom:4px;">작업중지권 행사 절차 안내</div>
    <div style="text-align:center; font-size:13px; color:{SUB}; margin-bottom:14px;">위험하면 즉시 멈추십시오. 작업 중지는 근로자의 권리입니다.</div>
    {stepline('①','발견','위험을 발견하면 즉시 작업을 중지할 수 있습니다. 동료의 위험도 됩니다.')}
    {stepline('②','통보','작업을 중지하였으면 지체 없이 관리감독자에게 통보합니다.')}
    {stepline('③','조치','회사는 위험 요인을 즉시 확인하고 조치하여야 합니다.')}
    {stepline('④','확인·재개','조치 완료 여부를 확인한 후에야 작업을 재개할 수 있습니다.')}
    {stepline('⑤','보호','중지를 이유로 불이익을 줄 수 없습니다. 손실은 회사가 부담합니다.')}</div>
  <div class="lnote" style="font-size:11.5px; color:{SUB}; margin-bottom:24px;">근거: 산업안전보건법 제52조(7과) · 기업 현장의 행사 절차 안내(삼성물산·삼성중공업 공개 자료)를 교육용으로 재구성함</div>
  <div style="font-weight:800;color:{NAVY};font-size:13.5px;margin-bottom:8px;">[나] 위험 상황 대화 — 제2공장 컨베이어 라인</div>
  <div style="border:1.2px solid {HAIR};border-radius:9px;padding:26px 28px 10px;margin-bottom:6px;font-size:15.5px;">
    {srow('작업자','"반장님, 컨베이어에서 이상한 소리가 납니다. 방호장치도 작동하지 않습니다.<br>손이 <b>말려들 우려가 있으므로</b> 작업을 <b>중지하겠습니다</b>."')}
    {srow('김 반장','"알겠습니다. 잘 판단했습니다. 라인에서 나오세요."')}
    {srow('동료','"오늘 물량이 많은데, 그냥 계속하면 안 됩니까?"')}
    {srow('작업자','"죄송하지만, 방호장치가 <b>고쳐지기 전에는</b> 작업<b>할 수 없습니다</b>."')}
    {scene('수리 후')}
    {srow('김 반장','"수리가 끝났습니다. 확인해 보세요."')}
    {srow('작업자','"방호장치 작동 <b>여부를 확인</b>한 후에 재개하겠습니다."')}
  </div>
  <div class="lnote" style="font-size:11.5px; color:{SUB};">실제 행사 사례(발견→요청→조치→재개)의 담화 구조를 제조 현장 상황으로 재구성함</div>
  {foot(11)}"""
page("실물자료읽기", p11)

# ═══ 12쪽 읽고 답하기 ═══
p12 = f"""{head_sec('3교시 · 읽기', '읽고 답하기')}
  <div class="tintbox" style="margin-bottom:{SP_M}px; font-size:14px;">11쪽의 안내문과 대화를 다시 보면서 답하십시오.</div>
  {sechead('A','기본 — 맞으면 ○, 틀리면 ✗를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.75;">
    {enc('①')} 동료의 위험을 발견해도 작업을 중지할 수 있다. ( {blank(2)} )<br>
    {enc('②')} 조치가 끝나기 전에도 물량이 급하면 재개할 수 있다. ( {blank(2)} )<br>
    {enc('③')} 중지로 인한 손실은 근로자가 부담한다. ( {blank(2)} )</div>
  {sechead('B','심화 — 안내문·대화에서 찾아 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.7;">
    {enc('①')} 작업을 중지한 다음, 누구에게 무엇을 합니까?<br>
    → {blank(20)}<br>
    {enc('②')} 작업자가 동료의 요구를 거절할 때 붙인 조건은 무엇입니까?<br>
    → {blank(20)}</div>
  {sechead('C','확장 — 생각을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    작업자는 "안 됩니다"라고만 하지 않고 조건을 말했습니다. 조건을 말하면 무엇이 좋습니까?<br>
    → {blank(26)}<br>
    {blank(30)}</div>
  {foot(12)}"""
page("읽고답하기", p12)

# ═══ 13쪽 연습 ═══
p13 = f"""{head_sec('3교시 · 읽기', '연습')}
  {sechead('A','상황을 읽고 알맞은 말을 고르십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.05;">
    {enc('①')} 프레스에서 연기가 납니다. → ( 계속 지켜본다 · 즉시 중지한다 )<br>
    {enc('②')} 조치가 아직 안 끝났는데 재개 지시가 옵니다. → ( 재개한다 · 정중히 거절한다 )<br>
    {enc('③')} 수리가 끝났습니다. → ( 바로 재개한다 · 작동 여부를 확인한 후 재개한다 )</div>
  {sechead('B','대화를 완성해 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:3.1;">
    {enc('①')} 지게차 브레이크가 밀립니다.<br>
    → 부딪힐 {blank(8)} 운행을 {blank(8)}<br>
    {enc('②')} "안전 교육 아직인데 그냥 투입하죠."<br>
    → 죄송하지만, 교육을 받{blank(5)} 작업{blank(9)}</div>
  {sechead('C','통보문의 순서를 바로잡아 번호를 쓰십시오.')}
  <div class="tintbox" style="margin-bottom:14px; font-size:14.5px; line-height:1.9;">
    ㉮ 조치 완료 여부를 확인한 후에 재개하겠습니다. ㉯ 컨베이어 방호장치가 작동하지 않습니다. ㉰ 말려들 우려가 있으므로 작업을 중지하였습니다.</div>
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    올바른 순서: ( {blank(2)} ) → ( {blank(2)} ) → ( {blank(2)} )</div>
  {foot(13)}"""
page("연습", p13)

# ═══ 14쪽 상황 쓰기 — 중지 통보문 ═══
p14 = f"""{head_sec('3교시 · 쓰기', '상황 쓰기 — 작업 중지 통보문')}
  <div class="prose" style="margin-bottom:16px;">내 작업장의 위험 상황 하나를 정해 중지 통보문을 씁니다. 이 글은 상급자에게 보내는 문서입니다.</div>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">통보문 공식 — 세 문장</div>
    <div style="font-size:14.5px; line-height:2.1;">[상황]{enc('＋')}[{blank(0)}우려가 있으므로 …중지하겠습니다]{enc('＋')}[완료 여부를 확인한 후에 재개하겠습니다]<br><br>
    <span style="font-size:13px; color:{SUB};">예: 컨베이어 방호장치가 작동하지 않습니다. 손이 말려들 우려가 있으므로 작업을 중지하겠습니다. 조치 완료 여부를 확인한 후에 재개하겠습니다.</span></div>
  </div>
  {sechead('A','통보문을 쓰십시오. (세 문장)')}
  <div class="drill left" style="margin-bottom:{SP_L}px; font-size:15px; line-height:3.75;">
    상황: {blank(30)}<br>
    {blank(34)}<br>
    중지: {blank(30)}<br>
    {blank(34)}<br>
    재개: {blank(30)}<br>
    {blank(34)}</div>
  <div class="caution" style="font-size:14px; line-height:1.95; padding:16px 18px;">
    <b>제출</b> · 완성한 통보문을 이번 주 <b>LMS 과제방</b>에 제출합니다. 이 글은 <b>과제②(11주)의 필수 구성요소</b>입니다.</div>
  {foot(14)}"""
page("상황쓰기", p14)

# ═══ 15쪽 정리 (1과 확정 틀) ═══
def npill(t):
    return f'<div style="margin-bottom:12px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:13px;font-weight:800;letter-spacing:.18em;padding:7px 16px;">{t}</span></div>'
vgrid12 = ''.join(f'<div style="border:1px solid {HAIR};border-radius:6px;padding:8px 12px;font-size:13.5px;">☐ {w}</div>'
    for w in ['거절','요청','상급자','즉시','발견','동료','판단','재개','행사','통보','불이익','손실'])

p15 = f"""{head_sec('3교시 · 읽기', '정리')}
  <div style="display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:1.6;margin-bottom:18px;">
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">1</span><span style="padding-top:2px;">중지는 선언이다 — <b>우려가 있으므로 중지하겠습니다</b>. 허락을 구하지 않는다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">2</span><span style="padding-top:2px;">거절은 조건이다 — <b>-기 전에는 할 수 없습니다</b>. 애매하게 말하지 않는다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">3</span><span style="padding-top:2px;">재개는 확인 뒤다 — 조치 완료 <b>여부를 확인</b>한 후에야 다시 시작한다.</span></div>
  </div>
  <div style="border-top:1px solid {HAIR};margin-bottom:16px;"></div>
  {npill('자가 점검 ① 체크리스트')}
  <div class="left" style="display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;font-size:14.5px;line-height:1.55;margin-bottom:{SP_M}px;">
    <div>☐ 중지 선언을 격식체로 말할 수 있다</div>
    <div>☐ 조건을 붙여 정중하게 거절할 수 있다</div>
    <div>☐ 중지 절차 다섯 단계를 말할 수 있다</div>
    <div>☐ '여부'를 써서 점검 문장을 쓸 수 있다</div>
    <div>☐ 세 문장 통보문을 쓸 수 있다</div>
  </div>
  {npill('자가 점검 ② 문제로 확인')}
  <div class="left" style="font-size:15px;line-height:2.25;margin-bottom:{SP_M}px;">
    ① 중지 선언의 문장 끝을 쓰십시오. → {blank(8)}<br>
    ② '했는지 안 했는지'를 한 단어로 쓰십시오. → {blank(4)}<br>
    ③ 다음 중 <u>틀린</u> 문장을 고르십시오. ( {blank(2)} )<br>
    <span style="font-size:14.5px;">㉮ 말려들 우려가 있으므로 중지하겠습니다 ㉯ 조치가 끝나기 전에는 재개할 수 없습니다 ㉰ 물량이 많으므로 조치 전에 재개하겠습니다</span><br>
    ④ '우려가 있<span class="x">으니까</span> 중지하겠습니다'에서 틀린 부분을 바르게 고치십시오. → {blank(6)}<br>
    ⑤ "좀 어려울 것 같아요."를 명확한 거절로 바꾸십시오. → 수리되기 {blank(12)}.</div>
  {npill('10초 어휘 셀프 체크')}
  <div style="font-size:13px;color:{SUB};margin-bottom:10px;">각 단어의 뜻이 3초 안에 떠오르지 않으면 ☐에 ✔ 하십시오. ✔한 단어는 2쪽으로 돌아가 예문과 함께 다시 읽으십시오.</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">{vgrid12}</div>
  {foot(15)}"""
page("정리", p15)

html = HEAD + '<body>' + ''.join(PAGES) + '</body></html>'
open('/home/claude/sik/ch8_full_15pages.html', 'w', encoding='utf-8').write(html)
print(f"[3/3] 전체 {len(PAGES)}쪽 → ch8_full_15pages.html ({len(html)} bytes)")

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file:///home/claude/sik/ch8_full_15pages.html')
    pg.wait_for_timeout(1200)
    pg.pdf(path='/home/claude/sik/ch8.pdf', width='794px', height='1123px',
           print_background=True, page_ranges='1-15')
    b.close()
print("PDF 렌더 완료")
