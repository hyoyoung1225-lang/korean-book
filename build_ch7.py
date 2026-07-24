# -*- coding: utf-8 -*-
"""build_ch7.py — 산업안전한국어 제7과 「권리와 의무」 (3부 권리 · 9주차 · Q7)
   kit_sik_v3 기반 + 확정 오버라이드(표제어 돋움·예문 볼드 강제·전각 밑줄 빈칸).
   내용 확정: 2026-07-17 교수 확정본 (진행DB 7과 행·색인DB·중복 점검 기록 9번 참조)
   실물 근거: 산업안전보건법 제52조·제37조①·제29조①②·제6조 (law.go.kr 검색 대조,
             제6조는 2026-02-19 법률 제21374호 개정 확인 — 발췌 구간 영향 없음)
"""
import re, sys
sys.path.insert(0, '/home/claude/sik')
exec(open('/home/claude/sik/kit_sik_v3_UPLOAD_ME.py').read())  # tokens + kit

# ═══ 확정 오버라이드 (오류기록 7번 · Canva 텍스트 신뢰 규칙 5번) ═══
# 1) 어휘 표제어 = 돋움 굵게 (키트 v3 세리프 정의는 오류)
# 2) 빈칸 = 전각 밑줄 문자 (CSS .bl 금지)
OVERRIDE_CSS = f"""
.vcard .w{{font-family:'Arimo','Noto Sans KR','Noto Sans CJK KR',sans-serif !important;
  font-size:18px; font-weight:800; color:{DEEP};}}
.vcard .ex b{{color:{NAVY};}}
.rightrow{{display:flex; align-items:flex-start; gap:14px;}}
.who{{flex:none; width:64px; text-align:center; font-size:12px; font-weight:800;
  letter-spacing:.08em; padding:5px 0; border-radius:4px;}}
.who.co{{background:{NAVY}; color:#fff;}}
.who.me{{background:{TINT}; color:{NAVY}; border:1px solid {NAVY};}}
.lawq{{font-size:13.5px; line-height:1.72; color:{INK}; background:#FBFCFE;
  border:1px solid {HAIR}; border-radius:6px; padding:11px 14px;}}
.easyq{{font-size:14.5px; line-height:1.72; color:{INK};}}
.rtitle{{font-weight:800; font-size:14.5px; color:{DEEP}; margin-bottom:8px;}}
.lnote{{font-size:11.5px; color:{SUB}; margin-top:4px;}}
"""
HEAD = HEAD.replace('</style>\n</head>', OVERRIDE_CSS + '</style>\n</head>')

def connect(left, right, lw=140, rw=150, gap=96, rowgap=18):
    """kit connect 오버라이드 — 번호는 평문으로 받고 내부에서 .enc로 감싼다(태그 절단 방지)."""
    dot = '<span style="color:#8A929E;font-size:14px;line-height:1;flex:none;">&middot;</span>'
    def L(t):
        n, w = t.split(" ", 1)
        return (f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:{rowgap}px;width:{lw}px;">'
                f'<span class="enc">{n}</span><span style="flex:1;">{w}</span>{dot}</div>')
    def R(t):
        n, w = t.split(" ", 1)
        return (f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:{rowgap}px;width:{rw}px;">'
                f'{dot}<span class="enc">{n}</span><span>{w}</span></div>')
    return f'<div style="display:flex;gap:{gap}px;">' +            f'<div>{"".join(L(t) for t in left)}</div><div>{"".join(R(t) for t in right)}</div></div>'

def blank(n=8):  # 전각 밑줄 텍스트 (kit v3 blank 오버라이드)
    return '<span style="letter-spacing:0;">' + '＿' * n + '</span>'

FOOT_L = "산업안전한국어 · 3부 권리 제7과 권리와 의무"
def foot(n): return footer(FOOT_L, f"{n:02d}")

def enc(t): return f'<span class="enc">{t}</span>'
PAGES = []
def page(label, body):
    PAGES.append(f'<div class="page" data-document-role="page" data-label="{label}">{body}</div>')

# ═══════════ 1쪽 도비라 — 3부 전환 (라벨·픽토4·문형배지·태그라인 신규) ═══════════
def picto_stop():   # 손바닥 — 멈출 권리
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M38 70 V46 a4 4 0 0 1 8 0 V42 a4 4 0 0 1 8 0 V44 a4 4 0 0 1 8 0 V50 l6 -6 a4 4 0 0 1 6 6 L62 64 a14 14 0 0 1 -24 8 Z" fill="#fff"/></svg>'''
def picto_lang():   # 말풍선 — 모국어 표지
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M26 34 h48 v28 h-30 l-10 10 v-10 h-8 Z" fill="#fff"/>
      <text x="50" y="54" text-anchor="middle" font-size="15" font-weight="bold" fill="{NAVY}">가 A</text></svg>'''
def picto_edu():    # 교육 — 받을 권리
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 28 L78 40 L50 52 L22 40 Z" fill="#fff"/>
      <path d="M34 46 v14 q16 10 32 0 v-14" fill="none" stroke="#fff" stroke-width="5"/></svg>'''
def picto_shield(): # 방패 — 불리한 처우 금지
    return f'''<svg width="84" height="84" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="{NAVY}"/>
      <path d="M50 24 L72 32 V52 q0 18 -22 26 q-22 -8 -22 -26 V32 Z" fill="#fff"/>
      <path d="M40 50 l8 8 l14 -16" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/></svg>'''

def klass_icon(glyph):
    return f"""<div style="width:62px;height:62px;border-radius:50%;background:{TINT};
      display:flex;align-items:center;justify-content:center;margin:0 auto 10px auto;">{glyph}</div>"""

G_TALK = f'<svg width="30" height="30" viewBox="0 0 100 100"><path d="M14 22 h72 v44 h-40 l-16 16 v-16 h-16 Z" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/><line x1="30" y1="38" x2="70" y2="38" stroke="{NAVY}" stroke-width="7"/><line x1="30" y1="52" x2="58" y2="52" stroke="{NAVY}" stroke-width="7"/></svg>'
G_AA   = f'<span style="font-family:\'Noto Serif KR\',serif;font-size:24px;font-weight:900;color:{NAVY};">Aa</span>'
G_BOOK = f'<svg width="30" height="30" viewBox="0 0 100 100"><path d="M50 26 q-16 -10 -34 -4 v52 q18 -6 34 4 q16 -10 34 -4 v-52 q-18 -6 -34 4 Z M50 26 v52" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/></svg>'
G_TARGET = f'<svg width="19" height="19" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="{NAVY}" stroke-width="10"/><circle cx="50" cy="50" r="16" fill="{NAVY}"/></svg>'
G_BULB = f'<svg width="17" height="17" viewBox="0 0 100 100"><path d="M50 12 a26 26 0 0 1 14 48 v10 h-28 v-10 a26 26 0 0 1 14 -48 Z" fill="none" stroke="{NAVY}" stroke-width="9"/><line x1="40" y1="82" x2="60" y2="82" stroke="{NAVY}" stroke-width="8"/></svg>'
G_SHIELD = f'<svg width="15" height="15" viewBox="0 0 100 100"><path d="M50 8 L86 20 V52 q0 28 -36 40 q-36 -12 -36 -40 V20 Z" fill="{NAVY}"/><path d="M36 50 l10 10 l20 -22" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/></svg>'

def kcol(glyph, pilltxt, pillbg, cap1, cap2):
    return f"""<div style="width:200px;text-align:center;">{klass_icon(glyph)}
      <div><span style="display:inline-block;background:{pillbg};color:#fff;font-size:12.5px;font-weight:800;height:27px;line-height:27px;padding:0 16px;border-radius:14px;">{pilltxt}</span></div>
      <div style="font-size:12px;color:{SUB};line-height:1.6;margin-top:9px;">{cap1}<br>{cap2}</div></div>"""

CHEV = f'<div style="color:#C4CBD7;font-size:15px;margin-top:26px;">〉</div>'

dobira = f"""
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid {NAVY};padding-bottom:11px;">
    <span style="font-size:13px;font-weight:700;letter-spacing:.5em;color:{INK};">산업안전한국어</span>
    <span style="font-size:13px;font-weight:800;letter-spacing:.14em;color:{NAVY};">3부 · 권리</span>
  </div>
  <div style="display:flex;gap:26px;margin-top:34px;">
    <div style="flex:1;padding-top:20px;">
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:118px;font-weight:900;
        color:{NAVY};line-height:.95;">07</div>
      <div style="margin-top:14px;"><span style="display:inline-block;background:{DEEP};color:#fff;
        font-size:12.5px;font-weight:800;letter-spacing:.34em;height:30px;line-height:30px;padding:0 12px 0 20px;">제 7 과</span></div>
      <div style="font-family:'Noto Serif KR','Noto Serif CJK KR',serif;font-size:46px;font-weight:900;
        color:{INK};margin-top:22px;">권리와 의무</div>
    </div>
    <div style="flex:none;width:322px;height:462px;position:relative;background:#E7EDF6;overflow:hidden;">
      <div style="position:absolute;top:120px;left:24px;width:56px;height:400px;background:#D8E1EF;"></div>
      <div style="position:absolute;top:230px;right:16px;width:70px;height:300px;background:#D1DBEC;"></div>
      <div style="position:absolute;top:-70px;left:150px;width:52px;height:640px;background:{NAVY};transform:rotate(16deg);"></div>
      <div style="position:absolute;top:52px;left:34px;right:34px;background:#fff;border-radius:16px;
        box-shadow:0 10px 26px rgba(20,35,80,.16);padding:26px 20px;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;justify-items:center;">
          {picto_stop()}{picto_edu()}{picto_lang()}{picto_shield()}</div></div>
    </div>
  </div>
  <div style="display:flex;gap:26px;margin-top:40px;">
    <div style="flex:1.06;">
      <div style="display:flex;align-items:center;gap:9px;margin-bottom:16px;">
        {G_TARGET}<span style="font-size:16px;font-weight:800;color:{INK};">학습 목표</span>
        <div style="flex:1;border-top:1px solid {HAIR};"></div></div>
      <div style="display:flex;flex-direction:column;gap:13px;font-size:14.5px;line-height:1.6;">
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">1</span><span style="padding-top:2px;">법이 정한 나의 권리 세 가지를 말할 수 있습니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">2</span><span style="padding-top:2px;">규정문의 <b>권리(-ㄹ 수 있다)</b>와 <b>의무(-여야 한다)</b>를 구별하며 읽습니다.</span></div>
        <div style="display:flex;gap:11px;"><span class="num" style="flex:none;width:26px;height:26px;font-size:14px;">3</span><span style="padding-top:2px;">조문 발췌를 쉬운 말과 대조하며 이해합니다.</span></div>
      </div>
    </div>
    <div style="flex:1;background:#EDF2FA;border-radius:12px;padding:20px 24px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px;">
        {G_BULB}<span style="font-size:15px;font-weight:800;color:{INK};">생각해 보기</span></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">위험해서 일을 멈추면, 회사가 나를 해고할 수 있을까요?</div>
      <div style="border-top:1px dashed #C9D2E2;margin:11px 0;"></div>
      <div style="font-size:13.5px;line-height:1.75;color:{INK};">우리 회사의 안전보건표지에는 어떤 언어가 있습니까?</div>
    </div>
  </div>
  <div style="display:flex;justify-content:center;align-items:flex-start;gap:4px;margin-top:42px;">
    {kcol(G_TALK,'1교시 · 어휘',NAVY,'핵심 어휘 12개 + 연습','법 문서 속 사람들')}
    {CHEV}
    {kcol(G_AA,'2교시 · 문형',LIGHT,'N에 따라 · -여야 하며','-(으)ㄹ 수 있다 + 종합')}
    {CHEV}
    {kcol(G_BOOK,'3교시 · 읽기',DEEP,'조문·쉬운 말 대조 독해','상황 쓰기 + 정리')}
  </div>
  <div style="position:absolute;top:{FOOTER_Y}px;left:64px;right:64px;border-top:1px solid {HAIR};
    padding-top:12px;display:flex;justify-content:space-between;align-items:center;">
    <span style="display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800;color:{INK};">
      {G_SHIELD} 권리를 알면 나를 지킬 수 있습니다.</span>
    <span style="font-size:13px;font-weight:800;color:{NAVY};">01</span>
  </div>"""
page("도비라", dobira)

# ═══════════ 2쪽 핵심 어휘 12 ═══════════
V = [
 ("권리","기본","법이 나에게 주는 힘입니다. 내가 요구할 수 있는 것입니다.",
  "일을 멈출 <b>권리</b>는 법이 정한 것입니다."),
 ("의무","기본","반드시 해야 하는 일입니다. 법이 정한 책임입니다.",
  "안전 기준을 지키는 것은 나의 <b>의무</b>입니다."),
 ("근로자","기본","회사에서 일하고 임금을 받는 사람입니다. 법률 문서의 말입니다.",
  "<b>근로자</b>는 작업을 중지하고 대피할 수 있습니다."),
 ("사업주","기본","사업의 주인입니다. 법에서 회사 쪽을 가리키는 말입니다.",
  "<b>사업주</b>는 안전 교육을 하여야 합니다."),
 ("중지","기본","하던 일을 멈추는 것입니다.",
  "위험하면 작업 <b>중지</b>를 말할 수 있습니다."),
 ("해고","기본","회사가 근로자를 내보내는 것입니다.",
  "정당한 이유 없는 <b>해고</b>는 할 수 없습니다."),
 ("모국어","기본","내가 태어나서 배운 나의 나라 말입니다.",
  "표지를 <b>모국어</b>로도 만들어야 합니다."),
 ("채용","기본","회사가 사람을 뽑는 것입니다.",
  "<b>채용</b>될 때 안전 교육을 받습니다."),
 ("급박하다","심화","위험이 아주 가까이 왔다는 뜻입니다.",
  "<b>급박한</b> 위험이 있으면 피할 수 있습니다."),
 ("처우","심화","사람을 대하는 방법입니다. '불리한 처우'로 자주 씁니다.",
  "불리한 <b>처우</b>를 해서는 안 됩니다."),
 ("관리감독자","심화","현장을 관리하는 책임자입니다. 반장님의 법률 이름입니다.",
  "<b>관리감독자</b>에게 바로 보고합니다."),
 ("유해","심화","몸에 해롭다는 뜻입니다. '유해하거나 위험한'으로 씁니다.",
  "<b>유해</b>하거나 위험한 장소에 표지를 붙입니다."),
]
v_cards = ''.join(vcard(w, lv, m, e) for w, lv, m, e in V)
p2 = f"""{head_sec('1교시 · 어휘', '핵심 어휘 12')}
  <div style="display:flex; align-items:center; gap:8px; font-size:13px; color:{SUB}; margin-bottom:16px;">
    <span class="lv b">기본</span><span>모든 학생 필수</span>
    <span class="lv a" style="margin-left:10px;">심화</span><span>법규·보고서의 문어 표현 — 읽고 이해할 수 있으면 충분합니다.</span></div>
  <div class="vgrid" style="gap:10px;">{v_cards}</div>
  {foot(2)}"""
page("핵심어휘", p2)

# ═══════════ 3쪽 어휘 연습 ═══════════
p3 = f"""{head_sec('1교시 · 어휘', '어휘 연습')}
  {sechead('A','알맞은 단어를 골라 빈칸을 채우십시오.')}
  <div class="wbank" style="margin-bottom:22px;">급박 · 채용 · 관리감독자 · 유해</div>
  <div class="left" style="font-size:15px; line-height:2.75; margin-bottom:{SP_XL}px;">
    ① {blank(6)}될 때와 작업 내용이 바뀔 때 안전 교육을 받습니다.<br>
    ② 기계가 이상하면 {blank(8)}에게 바로 보고하십시오.<br>
    ③ {blank(6)}한 위험이 있으면 작업을 중지할 수 있습니다.<br>
    ④ {blank(6)}하거나 위험한 물질에는 경고 표지가 있습니다.</div>
  {sechead('B','짝이 되는 말을 선으로 연결하십시오.')}
  <div style="margin-bottom:{SP_XL}px;">
  {connect(
    ["① 작업을", "② 교육을", "③ 표지를", "④ 사실을", "⑤ 기준을"],
    ["㉠ 받다", "㉡ 지키다", "㉢ 중지하다", "㉣ 읽다", "㉤ 보고하다"],
    lw=150, rw=230, rowgap=30)}
  </div>
  {sechead('C','B에서 연결한 표현 중 두 개를 골라 문장을 쓰십시오.')}
  <div class="left" style="font-size:15px; line-height:3.4;">
    ① {blank(40)}<br>
    ② {blank(40)}</div>
  {foot(3)}"""
page("어휘연습", p3)

# ═══════════ 4쪽 개념 — 권리·의무 지도 ═══════════
def rightcard(pic, title, law, desc):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:19px 18px; display:flex; gap:18px; align-items:center;">
      <div style="flex:none;">{pic}</div>
      <div style="flex:1;">
        <div style="display:flex; align-items:baseline; gap:10px;">
          <span style="font-weight:800; font-size:16.5px; color:{DEEP};">{title}</span>
          <span style="font-size:12px; color:{SUB};">{law}</span></div>
        <div style="font-size:14px; line-height:1.6; margin-top:5px;">{desc}</div></div></div>'''

p4 = f"""{head_sec('1교시 · 어휘', '나의 권리 세 가지, 나의 의무 하나')}
  <div class="prose" style="margin-bottom:18px;">산업안전보건법은 근로자에게 세 가지 권리를 줍니다. 그리고 한 가지 의무도 정합니다. 이 지도를 먼저 봅니다.</div>
  <div style="display:flex; flex-direction:column; gap:21px; margin-bottom:{SP_L}px;">
    {rightcard(picto_stop(), '일을 멈출 권리', '제52조',
      '급박한 위험이 있으면 작업을 중지하고 피할 수 있습니다.')}
    {rightcard(picto_edu(), '안전 교육을 받을 권리', '제29조',
      '회사는 정기적으로, 그리고 채용할 때 교육을 해야 합니다.')}
    {rightcard(picto_lang(), '모국어 표지를 볼 권리', '제37조',
      '회사는 안전보건표지를 내 모국어로도 만들어야 합니다.')}
    {rightcard(picto_shield(), '나의 의무', '제6조',
      '나도 안전 기준을 지켜야 하며, 안전 조치에 따라야 합니다.')}
  </div>
  <div class="tintbox">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">주어를 보면 알 수 있어요</div>
    <div style="font-size:14.5px; line-height:1.85;">법 문장의 주어를 봅니다. 주어가 <b>사업주</b>이면 회사의 의무입니다. 회사의 의무는 곧 나의 권리입니다. 주어가 <b>근로자</b>이면 나의 권리 또는 나의 의무입니다.</div>
  <div style="height:14px;"></div>
  </div>
  {foot(4)}"""
page("개념", p4)

# ═══════════ 5쪽 어휘 확장 1 — 법 문서 속 사람들 ═══════════
p5 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ① — 법 문서 속 사람들')}
  <div class="prose" style="margin-bottom:18px;">법률과 규정에는 사람을 부르는 이름이 따로 있습니다. 현장의 말과 짝을 지어 기억합니다.</div>
  <table class="f cellwide" style="margin-bottom:{SP_L}px;">
    <tr><th style="width:150px;">법률의 말</th><th style="width:150px;">현장의 말</th><th>누구입니까?</th></tr>
    <tr><td><b>근로자</b></td><td>직원, 사원, 나</td><td>일하고 임금을 받는 사람</td></tr>
    <tr><td><b>사업주</b></td><td>회사, 사장님</td><td>사업의 주인, 회사 쪽</td></tr>
    <tr><td><b>관리감독자</b></td><td>반장님, 팀장님</td><td>현장을 직접 관리하는 책임자</td></tr>
  </table>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">6과에서 배운 '반장님'</div>
    <div style="font-size:14.5px; line-height:1.85;">6과에서 반장님에게 보고하는 법을 배웠습니다. 법 문서에서는 그 반장님을 <b>관리감독자</b>라고 부릅니다. 같은 사람의 두 이름입니다.</div>
  </div>
  {sechead('A','법률의 말로 바꿔 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.85;">
    {enc('①')} 저는 이 회사 직원입니다. → 저는 이 회사 {blank(6)}입니다.<br>
    {enc('②')} 반장님에게 보고했습니다. → {blank(10)}에게 보고했습니다.<br>
    {enc('③')} 회사는 교육을 해야 합니다. → {blank(6)}는 교육을 하여야 합니다.</div>
  <div style="height:{SP_L}px;"></div>
  {sechead('B','누가 합니까? 알맞은 사람을 고르십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.85;">
    {enc('①')} 안전보건교육을 실시합니다. ( 근로자 · 사업주 )<br>
    {enc('②')} 작업 중지를 보고합니다. ( 근로자 · 관리감독자 )</div>
  {foot(5)}"""
page("어휘확장1", p5)

# ═══════════ 6쪽 어휘 확장 2 — 함께 쓰는 말(연어) ═══════════
def collo(a, b, meaning, ex):
    return f'''<div style="border:1px solid {HAIR}; border-radius:8px; padding:18px 17px;">
      <div style="font-size:17px; font-weight:800; color:{DEEP};">{a} <span style="color:{LIGHT};">+</span> {b}</div>
      <div style="font-size:13.5px; margin-top:5px; line-height:1.6;">{meaning}</div>
      <div style="font-size:12.5px; color:{SUB}; border-top:1px dashed {HAIR}; margin-top:8px; padding-top:7px;">{ex}</div></div>'''

p6 = f"""{head_sec('1교시 · 어휘', '어휘 확장 ② — 함께 쓰는 말')}
  <div class="prose" style="margin-bottom:18px;">법률의 말은 정해진 짝과 함께 다닙니다. 짝을 통째로 기억하면 문서가 빨리 읽힙니다.</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:17px; margin-bottom:{SP_L}px;">
    {collo('급박한','위험','위험이 아주 가까이 온 상태입니다. 멈출 권리의 조건입니다.','<b>급박한 위험</b>이 있는 경우에는 대피할 수 있다.')}
    {collo('불리한','처우','나에게 나쁘게 대하는 것입니다. 해고, 감봉 등입니다.','해고나 그 밖의 <b>불리한 처우</b>를 할 수 없습니다.')}
    {collo('유해하거나','위험한','몸에 해롭거나 다칠 수 있는 곳을 말합니다.','<b>유해하거나 위험한</b> 장소에 표지를 붙입니다.')}
    {collo('작업','중지','하던 일을 멈추는 것입니다. 나의 권리입니다.','<b>작업 중지</b>를 보고하였습니다.')}
  </div>
  {sechead('A','알맞은 짝을 골라 문장을 완성하십시오.')}
  <div class="wbank" style="margin-bottom:20px;">급박한 · 불리한 · 유해하거나 · 작업</div>
  <div class="drill left" style="font-size:15px; line-height:2.5;">
    {enc('①')} {blank(5)} 위험이 있으면 일을 멈출 수 있습니다.<br>
    {enc('②')} 회사는 {blank(5)} 처우를 할 수 없습니다.<br>
    {enc('③')} {blank(7)} 위험한 물질에는 경고 표지가 있습니다.<br>
    {enc('④')} {blank(4)} 중지를 지체 없이 보고하였습니다.</div>
  <div style="height:{SP_L}px;"></div>
  {sechead('B','짝을 넣어 한 문장을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.8;">
    '급박한 위험'을 넣어서 — {blank(28)}</div>
  {foot(6)}"""
page("어휘확장2", p6)

print(f"[1/3] 1교시 {len(PAGES)}쪽 구성 완료")

# ═══════════ 7~9쪽 문형 카드 공통 ═══════════
def pillrow(*ps):
    # 1·2과식: 키트 pill() = .el 네이비 칩 (자작 스타일 금지)
    return '<div style="display:flex; gap:8px; margin:10px 0 4px 0;">' + \
        ''.join(pill(t) for t in ps) + '</div>'

def gcard(num, title, site_img, quote, source, mean_html, comp_pill, comp_html, err_html, drill_html, wide=True, lv='심화', comb='명사'):
    sb, mm, cm, dl = (30, 21, 28, 2.95) if wide else (18, 10, 16, 2.25)
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

# SVG: 게시판 문서(규정 게시)
IMG_DOC = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <rect x="18" y="12" width="64" height="76" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="4"/>
  <rect x="26" y="22" width="48" height="7" fill="{NAVY}"/>
  <line x1="26" y1="40" x2="74" y2="40" stroke="{HAIR}" stroke-width="4"/>
  <line x1="26" y1="52" x2="74" y2="52" stroke="{HAIR}" stroke-width="4"/>
  <line x1="26" y1="64" x2="60" y2="64" stroke="{HAIR}" stroke-width="4"/></svg>'''
IMG_BOARD = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <rect x="10" y="16" width="80" height="56" rx="4" fill="{TINT}" stroke="{NAVY}" stroke-width="4"/>
  <rect x="18" y="24" width="30" height="40" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>
  <rect x="54" y="24" width="28" height="18" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>
  <path d="M46 88 L50 72 L54 88" stroke="{NAVY}" stroke-width="4" fill="none"/></svg>'''
IMG_HANDUP = f'''<svg width="92" height="92" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="42" fill="{TINT}" stroke="{NAVY}" stroke-width="4"/>
  <path d="M40 68 V46 a4 4 0 0 1 8 0 V42 a4 4 0 0 1 8 0 V44 a4 4 0 0 1 8 0 V50 l5 -5 a4 4 0 0 1 6 6 L63 63 a13 13 0 0 1 -23 7 Z" fill="{NAVY}"/></svg>'''

# ── 7쪽 문형① N에 따라 / N(으)로 인하여 ──
p7 = gcard('1', 'N에 따라 · N(으)로 인하여', IMG_DOC,
  '규정<b>에 따라</b> 안전 교육을 실시합니다.', '사내 게시문',
  """<b>N에 따라</b>는 'N이 정한 대로'라는 뜻입니다. 법과 규정을 말할 때 씁니다. <b>N(으)로 인하여</b>는 'N 때문에'의 문어입니다. 서류와 규정문에서 만납니다.""",
  '비교 · 3과에서 배운 말',
  f"""3과에서 <b>N(으)로 인해</b>를 배웠습니다. 서류에서는 더 긴 꼴 <b>N(으)로 인하여</b>로 씁니다. 뜻은 같습니다. 격이 더 높은 글에 씁니다.""",
  f"""<span class="x">✗ 위험에 인하여 작업을 중지했습니다.</span><br>
      ○ 위험<b>으로 인하여</b> 작업을 중지했습니다.<br>
      <span style="font-size:13px; color:{SUB};">'인하여' 앞에는 (으)로가 옵니다. '에'가 아닙니다.</span>""",
  f"""{enc('①')} 법{blank(4)} 안전보건표지를 붙입니다. (따라)<br>
      {enc('②')} 급박한 위험{blank(5)} 작업을 중지하였습니다. (인하여)<br>
      {enc('③')} 회사 규정{blank(4)} 보호구를 착용합니다. (따라)""", lv='심화', comb='명사')
page("문형1", p7 + foot(7))

# ── 8쪽 문형② -여야 하며, …-여야 한다 ──
p8 = gcard('2', '-여야 하며, …-여야 한다', IMG_BOARD,
  '기준을 지켜<b>야 하며</b>, 조치에 따라<b>야 한다</b>.', '안전보건관리규정',
  """규정문이 의무를 말하는 꼴입니다. <b>하여야</b>는 '해야'의 문어입니다. <b>-며</b>로 의무를 이어서 나열합니다. 회사 규정과 법에서 이 꼴로 만납니다.""",
  '비교 · 2과에서 배운 말',
  f"""2과에서 <b>반드시 -아/어야 하다</b>를 배웠습니다. 말로 할 때는 "지켜야 해요"라고 합니다. 규정문에서는 "지켜<b>야 하며</b> … 따라<b>야 한다</b>"로 씁니다.""",
  f"""<span class="x">✗ 기준을 지켜야 하며를 조치에 따라야 한다.</span><br>
      ○ 기준을 지켜야 하며<b>,</b> 조치에 따라야 한다.<br>
      <span style="font-size:13px; color:{SUB};">'-며' 뒤에는 쉼표를 찍고 문장을 잇습니다.</span>""",
  f"""{enc('①')} 사업주는 교육을 하{blank(4)} 하며, 표지를 붙{blank(4)} 한다.<br>
      {enc('②')} 근로자는 기준을 지{blank(4)} 하며, 조치에 따{blank(4)} 한다.<br>
      {enc('③')} (말→규정문) "교육을 꼭 해야 해요." → 교육을 하{blank(6)}""", lv='심화', comb='동사')
page("문형2", p8 + foot(8))

# ── 9쪽 문형③ -(으)ㄹ 수 있다(권리) ↔ -(으)ㄹ 수 없다 ──
p9 = gcard('3', '-(으)ㄹ 수 있다 ↔ -(으)ㄹ 수 없다', IMG_HANDUP,
  '근로자는 작업을 중지하고 대피<b>할 수 있다</b>.', '산업안전보건법 제52조',
  """규정문의 <b>-(으)ㄹ 수 있다</b>는 능력이 아니라 <b>권리</b>입니다. 해도 되고, 안 해도 됩니다. 내가 정합니다. <b>-(으)ㄹ 수 없다</b>는 금지입니다. 회사도 나도 할 수 없습니다.""",
  '비교 · 규정문의 세 가지 끝',
  f"""규정문은 문장의 끝이 뜻을 정합니다.<br>
      · <b>-ㄹ 수 있다</b> → 권리입니다. 내가 선택합니다.<br>
      · <b>-여야 한다</b> → 의무입니다. 반드시 합니다.<br>
      · <b>-ㄹ 수 없다</b> → 금지입니다. 하면 안 됩니다.""",
  f"""대피<b>할 수 있다</b>는 권리입니다.<br>
      <span class="x">✗ '대피해야 한다'로 읽으면 의무가 됩니다.</span><br>
      <span style="font-size:13px; color:{SUB};">권리를 의무로 읽지 않습니다. 끝을 정확히 봅니다.</span>""",
  f"""문장 끝을 보고 쓰십시오. (권리 / 의무 / 금지)<br>
      {enc('①')} 작업을 중지하고 대피할 수 있다. → {blank(4)}<br>
      {enc('②')} 모국어로 작성하여야 한다. → {blank(4)}<br>
      {enc('③')} 불리한 처우를 할 수 없다. → {blank(4)}""", wide=False, lv='기본', comb='동사')
page("문형3", p9 + foot(9))

# ═══════════ 10쪽 문형 종합 ═══════════
p10 = f"""{head_sec('2교시 · 문형', '문형 종합')}
  {sechead('A','말을 규정문으로 바꿔 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.95;">
    {enc('①')} "위험하면 멈춰도 돼요." → 위험한 경우 작업을 중지{blank(8)}<br>
    {enc('②')} "교육은 꼭 해야 해요." → 사업주는 교육을 하{blank(6)}<br>
    {enc('③')} "위험 때문에 멈췄어요." → 위험{blank(6)} 작업을 중지하였다.</div>
  {sechead('B','규정문에서 찾아 쓰십시오.')}
  <div class="lawq" style="margin-bottom:16px; font-size:14.5px; line-height:2.0; padding:16px 18px;">근로자는 산업재해가 발생할 급박한 위험이 있는 경우에는 작업을 중지하고 대피할 수 있다. 작업을 중지한 근로자는 지체 없이 그 사실을 관리감독자에게 보고하여야 한다.</div>
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.8;">
    {enc('①')} 권리를 나타내는 문장 끝: {blank(9)}<br>
    {enc('②')} 의무를 나타내는 문장 끝: {blank(9)}</div>
  {sechead('C','미니 쓰기 — 한 문장으로 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.7;">
    나의 권리 한 가지를 규정문 꼴로 씁니다.<br>
    근로자는 {blank(24)}<br>
    {blank(30)}<br>
    {blank(30)}</div>
  {foot(10)}"""
page("문형종합", p10)

print(f"[2/3] 2교시까지 {len(PAGES)}쪽 구성 완료")

# ═══════════ 11쪽 실물 읽기 — 조문·쉬운 말 대조 (3단) ═══════════
def lawrow(law_html, who, who_cls, easy_html, note=""):
    n = f'<div class="lnote">{note}</div>' if note else ''
    return f'''<div class="rightrow" style="margin-bottom:10px;">
      <div style="flex:1.15;"><div class="lawq">{law_html}</div>{n}</div>
      <div class="who {who_cls}">{who}</div>
      <div style="flex:1;" class="easyq">{easy_html}</div></div>'''

def lawblock(title, src, rows):
    return f'''<div style="margin-bottom:25px;">
      <div class="rtitle">{title} <span style="font-weight:500; color:{SUB}; font-size:12px;">· {src}</span></div>{rows}</div>'''

p11 = f"""{head_sec('3교시 · 읽기', '실물 읽기 — 법이 말하는 나의 권리')}
  <div style="display:flex; gap:14px; font-size:12px; color:{SUB}; margin-bottom:12px;">
    <span>왼쪽 = 법 원문 발췌</span><span>가운데 = 누구에게 말합니까?</span><span>오른쪽 = 쉬운 말</span></div>
  {lawblock('권리 1 · 일을 멈출 권리', '산업안전보건법 제52조',
    lawrow('① 근로자는 산업재해가 발생할 급박한 위험이 있는 경우에는 작업을 중지하고 <b>대피할 수 있다</b>.',
      '나','me','위험이 급박하면 일을 멈추고 피<b>할 수 있습니다</b>.')
    + lawrow('② 제1항<b>에 따라</b> 작업을 중지하고 대피한 근로자는 지체 없이 그 사실을 관리감독자 등에게 보고<b>하여야 한다</b>.',
      '나','me','위험<b>으로 인하여</b> 일을 멈추었으면, 바로 관리감독자(반장님)에게 알려야 합니다.')
    + lawrow('④ 사업주는 … 작업을 중지하고 대피한 근로자에 대하여 해고나 그 밖의 불리한 처우를 해서는 아니 된다.',
      '회사','co','멈추었다는 이유로 회사는 나를 해고<b>할 수 없습니다</b>.',
      "아니 된다 = '안 된다'의 법률 말투"))}
  {lawblock('권리 2 · 내 말로 된 표지를 볼 권리', '제37조 제1항',
    lawrow('외국인근로자를 사용하는 사업주는 안전보건표지를 … 해당 외국인근로자의 모국어로 작성<b>하여야 한다</b>.',
      '회사','co','회사는 안전보건표지를 내 모국어로도 만들어야 합니다. 이것은 법이 정한 회사의 의무입니다.'))}
  {lawblock('권리 3 · 교육을 받을 권리', '제29조',
    lawrow('① 사업주는 소속 근로자에게 … 정기적으로 안전보건교육을 <b>하여야 한다</b>. ② 사업주는 근로자를 채용할 때와 작업내용을 변경할 때에는 … 안전보건교육을 <b>하여야 한다</b>.',
      '회사','co','회사는 정기적으로 안전 교육을 해야 합니다. 채용될 때와 작업이 바뀔 때에도 교육을 받습니다.'))}
  {lawblock('그리고 나의 의무', '제6조',
    lawrow('근로자는 … 산업재해 예방을 위한 기준을 <b>지켜야 하며</b>, … 산업재해 예방에 관한 조치에 <b>따라야 한다</b>.',
      '나','me','나도 안전 기준을 <b>지켜야 하며</b>, 회사의 안전 조치에 <b>따라야 합니다</b>.'))}
  {foot(11)}"""
page("실물자료읽기", p11)

# ═══════════ 12쪽 읽고 답하기 ═══════════
p12 = f"""{head_sec('3교시 · 읽기', '읽고 답하기')}
  <div class="tintbox" style="margin-bottom:{SP_M}px; font-size:14px;">11쪽의 법 원문과 쉬운 말을 다시 보면서 답하십시오.</div>
  {sechead('A','기본 — 맞으면 ○, 틀리면 ✗를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.75;">
    {enc('①')} 급박한 위험이 있으면 작업을 중지할 수 있다. ( {blank(2)} )<br>
    {enc('②')} 작업을 중지한 것을 이유로 회사는 근로자를 해고할 수 있다. ( {blank(2)} )<br>
    {enc('③')} 안전보건표지는 한국어로만 만든다. ( {blank(2)} )</div>
  {sechead('B','심화 — 원문에서 찾아 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.7;">
    {enc('①')} 작업을 중지하고 대피한 다음, 누구에게 보고합니까?<br>
    → {blank(20)}<br>
    {enc('②')} 안전보건교육은 언제 받습니까? 두 가지를 쓰십시오.<br>
    → {blank(10)} · {blank(10)}</div>
  {sechead('C','확장 — 생각을 쓰십시오.')}
  <div class="drill left" style="font-size:15px; line-height:2.6;">
    제52조 ①은 권리이고, ②는 의무입니다. 문장의 어느 부분을 보고 알 수 있습니까?<br>
    → {blank(26)}<br>
    {blank(30)}</div>
  {foot(12)}"""
page("읽고답하기", p12)

# ═══════════ 13쪽 연습 ═══════════
p13 = f"""{head_sec('3교시 · 읽기', '연습')}
  {sechead('A','규정문을 읽고 권리·의무·금지를 고르십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.9;">
    {enc('①')} 근로자는 보호구를 착용하여야 한다. ( 권리 · 의무 · 금지 )<br>
    {enc('②')} 근로자는 작업을 중지하고 대피할 수 있다. ( 권리 · 의무 · 금지 )<br>
    {enc('③')} 불리한 처우를 할 수 없다. ( 권리 · 의무 · 금지 )</div>
  {sechead('B','쉬운 말을 규정문으로 바꿔 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_XL}px; font-size:15px; line-height:2.9;">
    {enc('①')} "회사는 표지를 제 모국어로도 만들어야 해요."<br>
    → 사업주는 안전보건표지를 모국어로 작성{blank(8)}<br>
    {enc('②')} "위험 때문에 일을 멈췄고, 반장님께 바로 말했어요."<br>
    → 급박한 위험{blank(6)} 작업을 중지하고, 관리감독자에게 보고{blank(8)}</div>
  {sechead('C','상황을 읽고 답을 쓰십시오.')}
  <div class="tintbox" style="margin-bottom:18px; font-size:14.5px;">기계에서 이상한 소리가 나고 연기가 납니다. 반장님은 지금 자리에 없습니다.</div>
  <div class="drill left" style="font-size:15px; line-height:2.9;">
    {enc('①')} 지금 무엇을 할 수 있습니까? → {blank(18)}<br>
    {enc('②')} 그다음에 무엇을 하여야 합니까? → {blank(18)}</div>
  {foot(13)}"""
page("연습", p13)

# ═══════════ 14쪽 상황 쓰기 ═══════════
p14 = f"""{head_sec('3교시 · 쓰기', '상황 쓰기 — 나에게 이런 권리가 있습니다')}
  <div class="prose" style="margin-bottom:16px;">이번 과에서 배운 나의 권리를 내 문장으로 씁니다. 회사와 기계를 내 작업장으로 바꿔서 씁니다.</div>
  <div class="tintbox" style="margin-bottom:{SP_M}px;">
    <div style="font-weight:800; color:{DEEP}; margin-bottom:6px;">쓰기 공식</div>
    <div style="font-size:14.5px; line-height:1.9;">[상황]{enc('＋')}[나는 …-(으)ㄹ 수 있습니다]{enc('＋')}[그리고 …-여야 합니다]<br><br>
    <span style="font-size:13px; color:{SUB};">예: 급박한 위험이 있으면 저는 작업을 중지할 수 있습니다. 그리고 관리감독자에게 보고하여야 합니다.</span></div>
  </div>
  {sechead('A','권리 문장 세 개를 쓰십시오.')}
  <div class="drill left" style="margin-bottom:{SP_L}px; font-size:15px; line-height:3.15;">
    {enc('①')} 일을 멈출 권리 — {blank(26)}<br>
    {blank(34)}<br>
    {blank(34)}<br>
    {enc('②')} 교육받을 권리 — {blank(26)}<br>
    {blank(34)}<br>
    {blank(34)}<br>
    {enc('③')} 모국어 표지 — {blank(26)}<br>
    {blank(34)}<br>
    {blank(34)}</div>
  <div class="caution" style="font-size:14px; line-height:1.8;">
    <b>제출</b> · 완성한 문장 세 개를 이번 주 <b>LMS 과제방</b>에 제출합니다. 이 글은 과제②(11주)에 함께 수합됩니다.</div>
  {foot(14)}"""
page("상황쓰기", p14)

# ═══════════ 15쪽 정리 + 자가점검 ═══════════
def npill(t):
    return f'<div style="margin-bottom:12px;"><span style="display:inline-block;background:{DEEP};color:#fff;font-size:13px;font-weight:800;height:29px;line-height:29px;padding:0 16px;">{t}</span></div>'

vgrid12 = ''.join(f'<div style="border:1px solid {HAIR};border-radius:6px;padding:8px 12px;font-size:13.5px;">☐ {w}</div>'
    for w in ['권리','의무','근로자','사업주','중지','해고','모국어','채용','급박','처우','관리감독자','유해'])

p15 = f"""{head_sec('3교시 · 읽기', '정리')}
  <div style="display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:1.6;margin-bottom:18px;">
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">1</span><span style="padding-top:2px;"><b>-ㄹ 수 있다</b>는 권리, <b>-여야 한다</b>는 의무, <b>-ㄹ 수 없다</b>는 금지 — 문장의 끝이 먼저 말한다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">2</span><span style="padding-top:2px;">법의 주어가 <b>사업주</b>이면 회사의 의무 — 회사의 의무는 곧 나의 권리다.</span></div>
    <div style="display:flex;gap:12px;align-items:flex-start;"><span class="num">3</span><span style="padding-top:2px;">멈추면 지체 없이 <b>관리감독자</b>에게 보고한다 — 멈췄다는 이유로 해고할 수 없다.</span></div>
  </div>
  <div style="border-top:1px solid {HAIR};margin-bottom:16px;"></div>
  {npill('자가 점검 ① 체크리스트')}
  <div class="left" style="display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;font-size:14.5px;line-height:1.55;margin-bottom:{SP_M}px;">
    <div>☐ 나의 권리 세 가지를 말할 수 있다</div>
    <div>☐ 규정문 끝에서 권리·의무·금지를 구별할 수 있다</div>
    <div>☐ 작업을 중지한 다음 할 일을 말할 수 있다</div>
    <div>☐ '하여야 한다'를 쉬운 말로 바꿀 수 있다</div>
    <div>☐ 나의 권리를 문장 세 개로 쓸 수 있다</div>
  </div>
  {npill('자가 점검 ② 문제로 확인')}
  <div class="left" style="font-size:15px;line-height:2.25;margin-bottom:{SP_M}px;">
    ① 규정문에서 권리를 나타내는 문장 끝을 쓰십시오. → {blank(12)}<br>
    ② '대피할 수 있다'를 쉬운 말로 바꾸십시오. → {blank(14)}<br>
    ③ 다음 중 <u>틀린</u> 문장을 고르십시오. ( {blank(2)} )<br>
    <span style="font-size:14.5px;">㉮ 표지를 모국어로 작성하여야 한다 ㉯ 근로자는 안전보건교육을 실시하여야 한다 ㉰ 급박한 위험이 있으면 대피할 수 있다</span><br>
    ④ '위험<span class="x">에 인하여</span> 작업을 중지했다'에서 틀린 부분을 바르게 고치십시오. → {blank(8)}<br>
    ⑤ "위험하면 멈춰도 돼요."를 규정문으로 바꾸십시오. → 작업을 중지{blank(10)}.</div>
  {npill('10초 어휘 셀프 체크')}
  <div style="font-size:13px;color:{SUB};margin-bottom:12px;">각 단어의 뜻이 3초 안에 떠오르지 않으면 ☐에 ✔ 하십시오. ✔한 단어는 2쪽으로 돌아가 예문과 함께 다시 읽으십시오.</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">{vgrid12}</div>
  {foot(15)}"""
page("정리", p15)

# ═══════════ 출력 ═══════════
html = HEAD + '<body>' + ''.join(PAGES) + '</body></html>'
open('/home/claude/sik/ch7_full_15pages.html', 'w', encoding='utf-8').write(html)
print(f"[3/3] 전체 {len(PAGES)}쪽 HTML 생성 → ch7_full_15pages.html ({len(html)} bytes)")

# PDF 렌더
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file:///home/claude/sik/ch7_full_15pages.html')
    pg.wait_for_timeout(1200)
    pg.pdf(path='/home/claude/sik/ch7.pdf', width='794px', height='1123px',
           print_background=True, page_ranges='1-15')
    b.close()
print("PDF 렌더 완료 → ch7.pdf")
