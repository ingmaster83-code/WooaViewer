"""
JA 파일에 남아 있는 KO 텍스트 교체
1. related-cards 한국어 → 일본어
2. inLanguage:"ko" → "ja"
3. LD+JSON name/desc KO → JA
4. 브레드크럼 KO 텍스트
"""
import os, re

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

# related-card 텍스트 KO → JA 매핑
RELATED_MAP = {
    'DOCX 뷰어': 'DOCX ビューア',
    'XLSX 뷰어': 'XLSX ビューア',
    'Markdown 뷰어': 'Markdown ビューア',
    'EPUB 뷰어': 'EPUB ビューア',
    'PPTX 뷰어': 'PPTX ビューア',
    'EML 뷰어': 'EML ビューア',
    'PDF 뷰어': 'PDF ビューア',
    'RTF 뷰어': 'RTF ビューア',
    'VCF 뷰어': 'VCF ビューア',
    'ICS 뷰어': 'ICS ビューア',
    'MSG 뷰어': 'MSG ビューア',
    'ODT 뷰어': 'ODT ビューア',
    'DXF 뷰어': 'DXF ビューア',
    'PSD 뷰어': 'PSD ビューア',
    'HEIC 뷰어': 'HEIC ビューア',
    'TIFF 뷰어': 'TIFF ビューア',
    'SVG 뷰어': 'SVG ビューア',
    '폰트 뷰어': 'フォント ビューア',
    'JSON 뷰어': 'JSON ビューア',
    'XML 뷰어': 'XML ビューア',
    'CSV 뷰어': 'CSV ビューア',
    'YAML 뷰어': 'YAML ビューア',
    'HEX 뷰어': 'HEX ビューア',
    'Diff 뷰어': 'Diff ビューア',
    'LOG 뷰어': 'LOG ビューア',
    'ZIP 뷰어': 'ZIP ビューア',
    'TAR 뷰어': 'TAR ビューア',
    'STL 뷰어': 'STL ビューア',
    'GCode 뷰어': 'GCode ビューア',
    'GPX 뷰어': 'GPX ビューア',
    'CBZ 뷰어': 'CBZ ビューア',
    'SRT 뷰어': 'SRT ビューア',
    'M3U 뷰어': 'M3U ビューア',
    'INI 뷰어': 'INI ビューア',
    '토렌트 뷰어': 'トレント ビューア',
}

# LD+JSON name KO → JA 매핑
LDJSON_NAME_MAP = {
    '"name":"DOCX 뷰어"': '"name":"DOCX ビューア"',
    '"name":"XLSX 뷰어"': '"name":"XLSX ビューア"',
    '"name":"Markdown 뷰어"': '"name":"Markdown ビューア"',
    '"name":"EPUB 뷰어"': '"name":"EPUB ビューア"',
    '"name":"PPTX 뷰어"': '"name":"PPTX ビューア"',
    '"name":"EML 뷰어"': '"name":"EML ビューア"',
    '"name":"PDF 뷰어"': '"name":"PDF ビューア"',
    '"name":"RTF 뷰어"': '"name":"RTF ビューア"',
    '"name":"VCF 뷰어"': '"name":"VCF ビューア"',
    '"name":"ICS 뷰어"': '"name":"ICS ビューア"',
    '"name":"MSG 뷰어"': '"name":"MSG ビューア"',
    '"name":"ODT 뷰어"': '"name":"ODT ビューア"',
    '"name":"DXF 뷰어"': '"name":"DXF ビューア"',
    '"name":"PSD 뷰어"': '"name":"PSD ビューア"',
    '"name":"HEIC 뷰어"': '"name":"HEIC ビューア"',
    '"name":"TIFF 뷰어"': '"name":"TIFF ビューア"',
    '"name":"SVG 뷰어"': '"name":"SVG ビューア"',
    '"name":"폰트 뷰어"': '"name":"フォント ビューア"',
    '"name":"JSON 뷰어"': '"name":"JSON ビューア"',
    '"name":"XML 뷰어"': '"name":"XML ビューア"',
    '"name":"CSV 뷰어"': '"name":"CSV ビューア"',
    '"name":"YAML 뷰어"': '"name":"YAML ビューア"',
    '"name":"HEX 뷰어"': '"name":"HEX ビューア"',
    '"name":"Diff 뷰어"': '"name":"Diff ビューア"',
    '"name":"LOG 뷰어"': '"name":"LOG ビューア"',
    '"name":"ZIP 뷰어"': '"name":"ZIP ビューア"',
    '"name":"TAR 뷰어"': '"name":"TAR ビューア"',
    '"name":"STL 뷰어"': '"name":"STL ビューア"',
    '"name":"GCode 뷰어"': '"name":"GCode ビューア"',
    '"name":"GPX 뷰어"': '"name":"GPX ビューア"',
    '"name":"CBZ 뷰어"': '"name":"CBZ ビューア"',
    '"name":"SRT 뷰어"': '"name":"SRT ビューア"',
    '"name":"M3U 뷰어"': '"name":"M3U ビューア"',
    '"name":"INI 뷰어"': '"name":"INI ビューア"',
    '"name":"토렌트 뷰어"': '"name":"トレント ビューア"',
    '"name":"GPX 메이커"': '"name":"GPX メーカー"',
    '"name":"폰트 뷰어"': '"name":"フォント ビューア"',
}

ok = 0
for fname in sorted(os.listdir(JA_DIR)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(JA_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. related-card KO → JA
    for ko, ja in RELATED_MAP.items():
        content = content.replace(f'<span>{ko}</span>', f'<span>{ja}</span>')

    # 2. inLanguage:"ko" → "ja"
    content = content.replace('"inLanguage":"ko"', '"inLanguage":"ja"')

    # 3. LD+JSON name KO → JA
    for ko, ja in LDJSON_NAME_MAP.items():
        content = content.replace(ko, ja)

    # 4. LD+JSON description KO → 간단 교체 (브라우저에서 처리 문구)
    content = content.replace(
        '"description":"Word 없이 .docx 파일을 브라우저에서 무료로 열어보는 온라인 뷰어"',
        '"description":"Microsoft Wordなしで.docxファイルをブラウザで無料で開くオンラインビューア"'
    )
    content = content.replace(
        '"description":"Excel 없이 .xlsx 파일을 브라우저에서 무료로 열어보는 온라인 뷰어. 다중 시트 지원."',
        '"description":"Microsoft Excelなしで.xlsxファイルをブラウザで無料で開くオンラインビューア"'
    )

    # 5. drop-zone 안 KO 문구 교체 (자주 나오는 것들)
    content = content.replace('.docx 형식만 지원합니다', '.docx 形式のみ対応')
    content = content.replace('.xlsx, .xls 형식만 지원합니다', '.xlsx, .xls 形式のみ対応')
    content = content.replace('파일을 읽는 중 오류가 발생했습니다', 'ファイルの読み込み中にエラーが発生しました')
    content = content.replace('내용이 없는 문서입니다.', '内容がないドキュメントです。')
    content = content.replace('.docx 파일만 지원합니다.', '.docxファイルのみ対応しています。')

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK: {fname}')
        ok += 1
    else:
        print(f'  -: {fname} (변경 없음)')

print(f'\n완료: {ok}개 수정')
