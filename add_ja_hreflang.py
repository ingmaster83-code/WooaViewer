"""
WooaViewer KO + EN 파일에 JA hreflang 추가 및 lang-switcher 업데이트
"""
import os, re

BASE = 'C:/개인/wooahouse/WooaViewer'
EN_DIR = os.path.join(BASE, 'en')

ok = 0
miss = 0


def process_file(fpath, lang, fname):
    global ok, miss
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 이미 JA hreflang이 있으면 스킵
    if 'hreflang="ja"' in content:
        print(f'  SKIP (이미 있음): {os.path.relpath(fpath, BASE)}')
        return

    ja_url = f'https://wooaviewer.wooahouse.com/ja/{fname}'
    ja_hreflang = f'  <link rel="alternate" hreflang="ja" href="{ja_url}">\n'

    # x-default 앞에 JA hreflang 삽입
    if 'hreflang="x-default"' in content:
        content = content.replace(
            '  <link rel="alternate" hreflang="x-default"',
            ja_hreflang + '  <link rel="alternate" hreflang="x-default"',
            1
        )
    else:
        # x-default 없으면 en hreflang 뒤에 삽입
        en_href_pattern = r'(<link rel="alternate" hreflang="en"[^>]+>)'
        content = re.sub(
            en_href_pattern,
            r'\1\n' + ja_hreflang.rstrip(),
            content,
            count=1
        )

    # lang-switcher 업데이트
    if lang == 'ko':
        # KO: KO(active)|EN → KO(active)|EN|JA
        ko_rel = fname
        en_rel = f'en/{fname}'
        ja_rel = f'ja/{fname}'
        new_switcher = (
            '<div class="lang-switcher">\n'
            f'        <a href="{ko_rel}" class="active">KO</a>\n'
            '        <span>|</span>\n'
            f'        <a href="{en_rel}">EN</a>\n'
            '        <span>|</span>\n'
            f'        <a href="{ja_rel}">JA</a>\n'
            '      </div>'
        )
    else:
        # EN: KO|EN(active) → KO|EN(active)|JA
        ko_rel = f'../{fname}'
        en_rel = fname
        ja_rel = f'../ja/{fname}'
        new_switcher = (
            '<div class="lang-switcher">\n'
            f'        <a href="{ko_rel}">KO</a>\n'
            '        <span>|</span>\n'
            f'        <a href="{en_rel}" class="active">EN</a>\n'
            '        <span>|</span>\n'
            f'        <a href="{ja_rel}">JA</a>\n'
            '      </div>'
        )

    # 기존 lang-switcher 교체
    content = re.sub(
        r'<div class="lang-switcher">.*?</div>',
        new_switcher,
        content,
        flags=re.DOTALL,
        count=1
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {os.path.relpath(fpath, BASE)}')
    ok += 1


# KO 파일들 처리
print('── KO 파일 처리 ────────────────────────────────')
ko_files = sorted([f for f in os.listdir(BASE) if f.endswith('.html') and f != '404.html'])
for fname in ko_files:
    fpath = os.path.join(BASE, fname)
    process_file(fpath, 'ko', fname)

# EN 파일들 처리
print('\n── EN 파일 처리 ────────────────────────────────')
en_files = sorted([f for f in os.listdir(EN_DIR) if f.endswith('.html')])
for fname in en_files:
    fpath = os.path.join(EN_DIR, fname)
    process_file(fpath, 'en', fname)

print(f'\n완료: {ok}개 업데이트')
