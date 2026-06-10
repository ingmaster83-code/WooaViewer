"""
WooaViewer JA 파일 drop-zone 텍스트 영어 → 일본어 교체
"""
import os

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

# (영어 원문, 일본어 번역) 교체 목록
REPLACEMENTS = [
    # ── 버튼 ────────────────────────────────────────────────────
    ('Choose File\n      <input', 'ファイルを選択\n      <input'),
    ('Choose File\n    <input',   'ファイルを選択\n    <input'),
    ('>Choose File<',             '>ファイルを選択<'),
    ('Select File\n      <input', 'ファイルを選択\n      <input'),
    ('Select File\n    <input',   'ファイルを選択\n    <input'),
    ('>Select File<',             '>ファイルを選択<'),

    # ── h3 ──────────────────────────────────────────────────────
    ('<h3>Drop a CBZ file here</h3>',            '<h3>CBZファイルをここにドロップ</h3>'),
    ('<h3>CSV Drop your file here</h3>',          '<h3>CSVファイルをここにドロップ</h3>'),
    ('<h3>DOCX Drop your file here</h3>',         '<h3>DOCXファイルをここにドロップ</h3>'),
    ('<h3>DXF Drop your file here</h3>',          '<h3>DXFファイルをここにドロップ</h3>'),
    ('<h3>EML Drop your file here</h3>',          '<h3>EMLファイルをここにドロップ</h3>'),
    ('<h3>EPUB Drop your file here</h3>',         '<h3>EPUBファイルをここにドロップ</h3>'),
    ('<h3>폰트 Drop your file here</h3>',         '<h3>フォントファイルをここにドロップ</h3>'),
    ('<h3>GCode Drop your file here</h3>',        '<h3>GCodeファイルをここにドロップ</h3>'),
    ('<h3>Drop a GPX file here</h3>',             '<h3>GPXファイルをここにドロップ</h3>'),
    ('<h3>HEIC Drop your file here</h3>',         '<h3>HEICファイルをここにドロップ</h3>'),
    ('<h3>Drop any file here</h3>',               '<h3>ファイルをここにドロップ</h3>'),
    ('<h3>Drop an ICS file here</h3>',            '<h3>ICSファイルをここにドロップ</h3>'),
    ('<h3>Drop an INI / CFG file here</h3>',      '<h3>INI / CFGファイルをここにドロップ</h3>'),
    ('<h3>JSON Drop your file here</h3>',         '<h3>JSONファイルをここにドロップ</h3>'),
    ('<h3>Drop a LOG file here</h3>',             '<h3>LOGファイルをここにドロップ</h3>'),
    ('<h3>Drop an M3U or M3U8 file here</h3>',   '<h3>M3U / M3U8ファイルをここにドロップ</h3>'),
    ('<h3>Markdown Drop your file here</h3>',     '<h3>Markdownファイルをここにドロップ</h3>'),
    ('<h3>Drop an MSG file here</h3>',            '<h3>MSGファイルをここにドロップ</h3>'),
    ('<h3>Drop an ODT / ODS file here</h3>',      '<h3>ODT / ODSファイルをここにドロップ</h3>'),
    ('<h3>PPTX Drop your file here</h3>',         '<h3>PPTXファイルをここにドロップ</h3>'),
    ('<h3>PSD Drop your file here</h3>',          '<h3>PSDファイルをここにドロップ</h3>'),
    ('<h3>Drop an RTF file here</h3>',            '<h3>RTFファイルをここにドロップ</h3>'),
    ('<h3>Drop an SRT or VTT file here</h3>',     '<h3>SRT / VTTファイルをここにドロップ</h3>'),
    ('<h3>STL Drop your file here</h3>',          '<h3>STLファイルをここにドロップ</h3>'),
    ('<h3>SVG Drop your file here</h3>',          '<h3>SVGファイルをここにドロップ</h3>'),
    ('<h3>Drop a TAR / TAR.GZ / TGZ file here</h3>', '<h3>TAR / TAR.GZ / TGZファイルをここにドロップ</h3>'),
    ('<h3>Drop a TIFF file here</h3>',            '<h3>TIFFファイルをここにドロップ</h3>'),
    ('<h3>Drop a Torrent file here</h3>',         '<h3>Torrentファイルをここにドロップ</h3>'),
    ('<h3>Drop a VCF file here</h3>',             '<h3>VCFファイルをここにドロップ</h3>'),
    ('<h3>XML Drop your file here</h3>',          '<h3>XMLファイルをここにドロップ</h3>'),
    ('<h3>YAML Drop your file here</h3>',         '<h3>YAMLファイルをここにドロップ</h3>'),
    ('<h3>ZIP Drop your file here</h3>',          '<h3>ZIPファイルをここにドロップ</h3>'),

    # ── p (설명 텍스트) ───────────────────────────────────────────
    ('<p>.cbz format · Files never sent to server</p>',
     '<p>.cbz 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>Supports .csv format</p>',
     '<p>.csv 形式に対応</p>'),
    ('<p>.dxf 형식만 지원합니다 (DWG는 미지원)</p>',
     '<p>.dxf 形式対応（DWGは非対応）</p>'),
    ('<p>Supports .eml format</p>',
     '<p>.eml 形式に対応</p>'),
    ('<p>.epub 형식만 지원합니다</p>',
     '<p>.epub 形式のみ対応</p>'),
    ('<p>.ttf · .otf · .woff · .woff2 형식을 지원합니다</p>',
     '<p>.ttf · .otf · .woff · .woff2 形式に対応</p>'),
    ('<p>.gcode / .nc / .cnc 형식 지원</p>',
     '<p>.gcode / .nc / .cnc 形式に対応</p>'),
    ('<p>.gpx format · Files never sent to server</p>',
     '<p>.gpx 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.heic / .heif 형식 지원</p>',
     '<p>.heic / .heif 形式に対応</p>'),
    ('<p>Any binary file format · Files never sent to server</p>',
     '<p>バイナリファイル対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.ics format · Files never sent to server</p>',
     '<p>.ics 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.ini,.cfg,.conf,.properties format · Files never sent to server</p>',
     '<p>.ini,.cfg,.conf,.properties 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>Supports .json format</p>',
     '<p>.json 形式に対応</p>'),
    ('<p>.log,.txt,.out,.err format · Files never sent to server</p>',
     '<p>.log,.txt,.out,.err 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.m3u,.m3u8 format · Files never sent to server</p>',
     '<p>.m3u,.m3u8 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.md .markdown .txt 형식을 지원합니다</p>',
     '<p>.md .markdown .txt 形式に対応</p>'),
    ('<p>.msg format · Files never sent to server</p>',
     '<p>.msg 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.odt,.ods,.odp format · Files never sent to server</p>',
     '<p>.odt,.ods,.odp 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>Supports .pptx format</p>',
     '<p>.pptx 形式に対応</p>'),
    ('<p>.psd 형식만 지원합니다</p>',
     '<p>.psd 形式のみ対応</p>'),
    ('<p>.rtf format · Files never sent to server</p>',
     '<p>.rtf 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.srt,.vtt format · Files never sent to server</p>',
     '<p>.srt,.vtt 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.stl 형식만 지원합니다 (ASCII / Binary 모두 가능)</p>',
     '<p>.stl 形式対応（ASCII / Binary 両対応）</p>'),
    ('<p>.svg 형식을 지원합니다</p>',
     '<p>.svg 形式に対応</p>'),
    ('<p>.tar,.tar.gz,.tgz,.gz format · Files never sent to server</p>',
     '<p>.tar,.tar.gz,.tgz,.gz 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.tif,.tiff format · Files never sent to server</p>',
     '<p>.tif,.tiff 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.torrent format · Files never sent to server</p>',
     '<p>.torrent 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.vcf,.vcard format · Files never sent to server</p>',
     '<p>.vcf,.vcard 形式対応 · ファイルはサーバーに送信されません</p>'),
    ('<p>.xml / .svg / .rss / .atom / .kml 등 XML 기반 형식 지원</p>',
     '<p>.xml / .svg / .rss / .atom / .kml などXMLベース形式に対応</p>'),
    ('<p>Supports .yaml, .yml format</p>',
     '<p>.yaml,.yml 形式に対応</p>'),
    ('<p>Supports .zip format</p>',
     '<p>.zip 形式に対応</p>'),

    # ── breadcrumb 영어 → 일본어 ────────────────────────────────
    ('<span>CSV Viewer</span>',     '<span>CSV ビューア</span>'),
    ('<span>DOCX Viewer</span>',    '<span>DOCX ビューア</span>'),
    ('<span>DXF Viewer</span>',     '<span>DXF ビューア</span>'),
    ('<span>EML Viewer</span>',     '<span>EML ビューア</span>'),
    ('<span>EPUB Viewer</span>',    '<span>EPUB ビューア</span>'),
    ('<span>Font Viewer</span>',    '<span>フォント ビューア</span>'),
    ('<span>GCode Viewer</span>',   '<span>GCode ビューア</span>'),
    ('<span>HEIC Viewer</span>',    '<span>HEIC ビューア</span>'),
    ('<span>ICS Viewer</span>',     '<span>ICS ビューア</span>'),
    ('<span>JSON Viewer</span>',    '<span>JSON ビューア</span>'),
    ('<span>Log Viewer</span>',     '<span>Log ビューア</span>'),
    ('<span>Markdown Viewer</span>','<span>Markdown ビューア</span>'),
    ('<span>MSG Viewer</span>',     '<span>MSG ビューア</span>'),
    ('<span>ODT Viewer</span>',     '<span>ODT ビューア</span>'),
    ('<span>PPTX Viewer</span>',    '<span>PPTX ビューア</span>'),
    ('<span>PSD Viewer</span>',     '<span>PSD ビューア</span>'),
    ('<span>RTF Viewer</span>',     '<span>RTF ビューア</span>'),
    ('<span>STL Viewer</span>',     '<span>STL ビューア</span>'),
    ('<span>SVG Viewer</span>',     '<span>SVG ビューア</span>'),
    ('<span>TIFF Viewer</span>',    '<span>TIFF ビューア</span>'),
    ('<span>VCF Viewer</span>',     '<span>VCF ビューア</span>'),
    ('<span>XML Viewer</span>',     '<span>XML ビューア</span>'),
    ('<span>YAML Viewer</span>',    '<span>YAML ビューア</span>'),
    ('<span>ZIP Viewer</span>',     '<span>ZIP ビューア</span>'),
    ('<span>CBZ Viewer</span>',     '<span>CBZ ビューア</span>'),
    ('<span>HEX Viewer</span>',     '<span>HEX ビューア</span>'),
    ('<span>INI Viewer</span>',     '<span>INI ビューア</span>'),
    ('<span>M3U Viewer</span>',     '<span>M3U ビューア</span>'),
    ('<span>SRT Viewer</span>',     '<span>SRT ビューア</span>'),
    ('<span>TAR Viewer</span>',     '<span>TAR ビューア</span>'),
    ('<span>Torrent Viewer</span>', '<span>Torrent ビューア</span>'),
    ('<span>GPX Viewer</span>',     '<span>GPX ビューア</span>'),
]

ok = 0
skip = 0

for fname in sorted(os.listdir(JA_DIR)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(JA_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    if content == original:
        skip += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {fname}')
    ok += 1

print(f'\n완료: {ok}개 수정, {skip}개 변경없음')
