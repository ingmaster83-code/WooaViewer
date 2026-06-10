"""
WooaViewer JA 파일 구조 수정
- related-tools + wooa-orig-anchor 를 page-with-sidebar 밖에서 → tool-page 안(tips-panel 앞)으로 이동
"""
import os, re

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

BAD_FILES = [
    'csv-viewer.html', 'diff-viewer.html', 'dxf-viewer.html',
    'eml-viewer.html', 'epub-viewer.html', 'font-viewer.html',
    'gcode-viewer.html', 'heic-viewer.html', 'json-viewer.html',
    'markdown-viewer.html', 'pdf-viewer.html', 'pptx-viewer.html',
    'psd-viewer.html', 'stl-viewer.html', 'svg-viewer.html',
    'xml-viewer.html', 'yaml-viewer.html', 'zip-viewer.html',
]

ok = 0
err = 0

for fname in BAD_FILES:
    fpath = os.path.join(JA_DIR, fname)
    if not os.path.exists(fpath):
        print(f'  MISSING: {fname}')
        err += 1
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # page-with-sidebar 닫기 이후에 있는 related-tools + wooa-orig-anchor 블록 추출
    # 패턴: </aside>\n</div>\n\n[related-tools block]\n<div class="wooa-orig-anchor"></div>\n
    m = re.search(
        r'(</aside>\n</div>\n\n)'
        r'(\s*<div class="related-tools">.*?</div>\n)'
        r'(<div class="wooa-orig-anchor"></div>\n)',
        content, re.DOTALL
    )

    if not m:
        print(f'  SKIP (패턴 없음): {fname}')
        err += 1
        continue

    sidebar_end = m.group(1)    # </aside>\n</div>\n\n
    related_block = m.group(2)  # related-tools 블록 (앞 공백 포함)
    anchor = m.group(3)         # <div class="wooa-orig-anchor"></div>\n

    # related-tools의 앞 공백 제거 (tool-page 안으로 이동할 때 indent 통일)
    related_clean = re.sub(r'^\s+', '', related_block)

    # 1. 원래 위치(sidebar 밖)에서 제거: related-tools + anchor 제거
    new_sidebar_end = '</aside>\n</div>\n\n'
    content = content.replace(
        sidebar_end + related_block + anchor,
        new_sidebar_end,
        1
    )

    # 2. tips-panel 바로 앞에 삽입
    content = content.replace(
        '\n<div class="tips-panel">',
        '\n' + related_clean.rstrip('\n') + '\n' + anchor.rstrip('\n') + '\n<div class="tips-panel">',
        1
    )

    if content == original:
        print(f'  WARN (변경없음): {fname}')
        err += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {fname}')
    ok += 1

print(f'\n완료: {ok}개 수정, {err}개 오류/스킵')
