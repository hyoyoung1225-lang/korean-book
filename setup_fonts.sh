#!/usr/bin/env bash
# 산업안전한국어 — 폰트 세팅 (매 세션 0단계). 1·2과와 동일 렌더를 위해 로컬 폰트 사용.
# Noto Serif/Sans CJK KR 는 보통 이미 설치됨. Pretendard 만 로컬 설치한다. (CDN·구글폰트 쓰지 말 것)
set -e
mkdir -p ~/.fonts && cd ~/.fonts
base="https://raw.githubusercontent.com/orioncactus/pretendard/main/packages/pretendard/dist/public/static"
for w in Regular Medium SemiBold Bold Black; do
  [ -f "Pretendard-$w.otf" ] || curl -fsSL "$base/Pretendard-$w.otf" -o "Pretendard-$w.otf"
done
fc-cache -f ~/.fonts >/dev/null 2>&1
echo "폰트 준비 완료:"; fc-list | grep -iE "pretendard|noto serif cjk kr" | sort -u | head
