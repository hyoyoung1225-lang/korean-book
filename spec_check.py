# -*- coding: utf-8 -*-
"""spec_check.py — 산업안전한국어 교재 통합 규격 검사기 (2026-07-17)
사용: python3 spec_check.py <chapter.html> [chapter.pdf]
지금까지 확정된 모든 규격을 한 번에 검사한다. 하나라도 실패하면 exit 1.
새 규격이 확정되면 반드시 이 파일에 추가한다.
"""
import re, sys, json

def check(html_path, pdf_path=None):
    h = open(html_path, encoding='utf-8').read()
    errs, warns = [], []
    T = re.sub(r'<[^>]+>', ' ', h)

    # 1. 페이지 수 15
    n = h.count('data-document-role="page"')
    if n != 15: errs.append(f"페이지 수 {n} (기준 15)")

    # 2. 리터럴 코드 노출 0
    lit = h.count('{blank') + h.count('{enc') + h.count('{dturn') + h.count("f'") + 0
    lit = h.count('{blank') + h.count('{enc') + h.count('{dturn')
    if lit: errs.append(f"리터럴 코드 노출 {lit}건")

    # 3. 배지(.el) 내부 .enc 금지
    bad = re.findall(r'<div class="el"><span>(?:(?!</span>).)*?<span class="enc"', h, re.S)
    if bad: errs.append(f"배지 내부 .enc {len(bad)}건")

    # 4. CSS 빈칸(class=bl)·border 빈칸 금지 — 빈칸은 전각 밑줄 텍스트만
    if re.findall(r'class="bl"', h): errs.append("CSS 빈칸(.bl) 사용")
    if re.findall(r'border-bottom:[^;]*;height:3[0-9]px', h): errs.append("border 빈칸 div 사용")

    # 5. 어휘 표제어 = 돋움 굵게 (세리프 금지)
    m = re.search(r"\.vcard \.w\s*\{[^}]*\}", h)
    if m and 'Serif' in m.group(0) and 'sans' not in m.group(0):
        # 오버라이드 스타일이 뒤에 있는지 확인
        if ".vcard .w{font-family:'Arimo'" not in h and '.vcard .w{font-family:"Arimo"' not in h:
            errs.append("어휘 표제어가 세리프 (1·2과 기준: 돋움 굵게)")

    # 6. 어휘 예문 속 표제어 볼드
    exs = re.findall(r'class="ex">(.*?)</div>', h, re.S)
    nb = [e[:24] for e in exs if '<b>' not in e]
    if nb: errs.append(f"예문 표제어 볼드 누락 {len(nb)}건: {nb[:3]}")

    # 7. 비표준 문법 용어 (창작 용어 금지)
    STANDARD = {'격식체','문어체','구어체','한다체','높임법','사동법','피동법','간접화법','명사문','정의문',
     '의문문','평서문','명령문','부정문','안내문','설명문','지시문','인용문','조문','전문','본문','원문',
     '기본형','확장형','존댓말','표현','문형','문법','방법','어법','용법','평서','의문','명령','준말'}
    CONTENT_OK = {'금형','유형','대형','소형','원형','도형','성형','조형','전형','작업법','점검법','신고법','체형','자형','모형','인화성'}
    BAD_KNOWN = {'조문체','압축형','문어형','격식형','현장형','보고체','수칙체'}
    sus = {}
    for mm in re.finditer(r'[가-힣]{1,4}(?:체|형|법)\b', T):
        w = mm.group(0)
        if w in BAD_KNOWN: errs.append(f"비표준 문법 용어: {w}")
        elif w not in STANDARD and w not in CONTENT_OK: sus[w] = sus.get(w,0)+1
    generic = {'물체','신체','교체','해체','전체','자체','단체','업체','삼각형','사각형','마름모형'}
    sus = {k:v for k,v in sus.items() if k not in generic}
    if sus: warns.append(f"메타언어 확인 필요(수동 판단): {sus}")

    # 8. 종이 전제 문구 금지 (과제는 디지털)
    for k in ('노트에 옮겨','과제 노트','공책','종이에 쓰'):
        if k in T: errs.append(f"종이 전제 문구: '{k}'")

    # 9. 설명문 문장 길이 (25자 안팎, 45자 초과 오류)
    lens = []
    for p in re.findall(r'class="prose"[^>]*>(.*?)</div>', h, re.S):
        t = re.sub(r'<[^>]+>','',p)
        for sent in re.split(r'(?<=다)[.!?]', t):
            sent = sent.strip()
            if len(sent) > 5: lens.append((len(sent), sent))
    over = [(l,s[:30]) for l,s in lens if l > 45]
    avg = sum(l for l,_ in lens)/max(1,len(lens))
    if avg > 32: errs.append(f"설명문 평균 {avg:.1f}자 (기준 ~25자)")
    if over: warns.append(f"45자 초과 설명문 {len(over)}건: {over[:2]}")

    # 10. 문형 제목 한 줄 (nowrap 필수)
    for mm in re.finditer(r'class="formbig"([^>]*)>', h):
        if 'nowrap' not in mm.group(1): errs.append("문형 제목 nowrap 누락")

    # 11. 실물읽기 폰트 ≥ 문제 폰트 (p11 drill에 font-size 명시 확인 — 축소 지정 여부만 검사)
    p11 = re.split(r'(?=<div class="page")', h)
    p11 = [x for x in p11 if 'data-label="실물자료읽기"' in x]
    if p11:
        drill = re.search(r'class="drill"[^>]*style="([^"]*)"', p11[0])
        doc_fs = re.findall(r'font-size:(1[0-9](?:\.\d)?)px', p11[0])
        if drill and 'font-size' not in drill.group(1):
            warns.append("실물읽기 문제부 크기 미지정 — 실물≥문제 확인 필요")

    # 12. 도비라 라벨·푸터 존재
    if '2부 · 작업절차' not in T and '1부' not in T and '3부' not in T and '4부' not in T:
        errs.append("부 라벨 없음")

    print(f"═══ spec_check: {html_path} ═══")
    for e in errs: print("  ✗", e)
    for w in warns: print("  ⚠", w)
    if not errs and not warns: print("  전체 통과 ✓ (오류 0 · 확인 0)")
    elif not errs: print(f"  통과 (오류 0 · 수동 확인 {len(warns)})")
    print(f"  [설명문 {len(lens)}문장 · 평균 {avg:.1f}자]")
    return 1 if errs else 0

if __name__ == '__main__':
    sys.exit(check(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None))
