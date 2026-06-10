"""
WooaViewer JA 파일 - 잔존 한국어 텍스트 일본어 교체
1. related-tools 카드 라벨
2. LD+JSON description
3. JS 에러/UI 메시지
"""
import os

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

# ─────────────────────────────────────────────
# 공통 교체 (여러 파일에서 반복됨)
# ─────────────────────────────────────────────
COMMON = [
    # related-tools 카드 한국어
    ('<span>TAR/GZ 뷰어</span>',       '<span>TAR/GZ ビューア</span>'),
    ('<span>SRT/VTT 자막 뷰어</span>', '<span>SRT/VTT ビューア</span>'),
    ('<span>M3U/M3U8 뷰어</span>',     '<span>M3U/M3U8 ビューア</span>'),
    ('<span>INI/CFG 뷰어</span>',      '<span>INI/CFG ビューア</span>'),
    # 공통 파싱 오류 패턴
    ("'파싱 오류: '",                  "'解析エラー: '"),
    ("'파일 파싱 오류: '",             "'ファイル解析エラー: '"),
]

# ─────────────────────────────────────────────
# 파일별 교체 목록
# ─────────────────────────────────────────────
FILE_SPECIFIC = {

    'cbz-viewer.html': [
        # LD+JSON description은 이미 영어로 OK
        # JS 에러
        ("'라이브러리 로딩 실패. 새로고침 후 재시도하세요.'",
         "'ライブラリの読み込みに失敗しました。ページを再読み込みしてください。'"),
        ("'이미지를 찾을 수 없습니다. 올바른 CBZ 파일인지 확인하세요.'",
         "'画像が見つかりません。正しいCBZファイルか確認してください。'"),
        # stats 텍스트
        ("+'페이지'",  "+'ページ'"),
        ("' (최대 50페이지 표시)'", "' (最大50ページ表示)'"),
        ("'파싱 오류: '+e.message", "'解析エラー: '+e.message"),
    ],

    'csv-viewer.html': [
        # LD+JSON description
        ('"CSV 파일을 테이블로 보여주는 온라인 뷰어. 열 정렬, 실시간 검색, 구분자 선택 지원."',
         '"CSVファイルをテーブル表示するオンラインビューア。列ソート・リアルタイム検索・区切り文字選択に対応。"'),
    ],

    'diff-viewer.html': [
        # LD+JSON description
        ('"두 텍스트 파일을 비교하여 차이점을 보여주는 온라인 뷰어."',
         '"2つのテキストファイルを比較して差分を表示するオンラインビューア。"'),
        # 파일 버튼 라벨
        ('>📂 파일<input', '>📂 ファイル<input'),
    ],

    'dxf-viewer.html': [
        # LD+JSON description
        ('"AutoCAD 없이 .dxf 도면 파일을 브라우저에서 무료로 열어보는 온라인 CAD 뷰어"',
         '"AutoCADなしで.dxf図面ファイルをブラウザで無料で開くオンラインCADビューア"'),
        # DWG 안내 notice
        ('💡 <span><strong>DWG 파일</strong>은 Autodesk 독점 포맷으로 브라우저 지원이 불가합니다. AutoCAD에서 <strong>다른 이름으로 저장 → DXF</strong>로 변환 후 사용해주세요.</span>',
         '💡 <span><strong>DWGファイル</strong>はAutodeskの専用フォーマットのためブラウザ対応不可です。AutoCADで<strong>名前を付けて保存 → DXF</strong>に変換してからご使用ください。</span>'),
        # JS 에러
        ("'도형을 찾을 수 없습니다. 올바른 DXF 파일인지 확인해주세요.'",
         "'図形が見つかりません。正しいDXFファイルか確認してください。'"),
    ],

    'eml-viewer.html': [
        # LD+JSON description
        ('".eml 이메일 파일을 브라우저에서 열어 본문과 첨부파일을 확인하는 온라인 뷰어."',
         '".emlメールファイルをブラウザで開き、本文と添付ファイルを確認するオンラインビューア。"'),
        # JS 에러
        ("'EML 파일을 파싱할 수 없습니다. 올바른 .eml 파일인지 확인해주세요.'",
         "'EMLファイルを解析できません。正しい.emlファイルか確認してください。'"),
        # 첨부파일 fallback
        ("'첨부파일'", "'添付ファイル'"),
    ],

    'epub-viewer.html': [
        # LD+JSON description
        ('".epub 전자책 파일을 브라우저에서 무료로 읽어보는 온라인 뷰어. 목차 탐색, 페이지 넘기기 지원."',
         '".epub電子書籍ファイルをブラウザで無料で読むオンラインビューア。目次ナビ・ページ送りに対応。"'),
        # JS 에러
        ("'.epub 파일만 지원합니다.'", "'.epubファイルのみ対応しています。'"),
    ],

    'font-viewer.html': [
        # LD+JSON description
        ('"TTF·OTF·WOFF·WOFF2 폰트 파일 미리보기 온라인 뷰어. 크기·굵기·이탤릭 조절, 한글·영문·숫자 캐릭터 세트 확인 지원."',
         '"TTF·OTF·WOFF·WOFF2フォントファイルプレビューオンラインビューア。サイズ·太さ·イタリック調整、文字セット確認に対応。"'),
        # JS 에러
        ("'.ttf, .otf, .woff, .woff2 파일만 지원합니다.'",
         "'.ttf, .otf, .woff, .woff2ファイルのみ対応しています。'"),
    ],

    'gcode-viewer.html': [
        # LD+JSON description
        ('".gcode 3D 프린터 파일을 브라우저에서 무료로 툴패스를 레이어별 시각화하는 온라인 뷰어"',
         '".gcode 3Dプリンターファイルをブラウザでレイヤー別にツールパスを可視化するオンラインビューア"'),
    ],

    'gpx-viewer.html': [
        # JS 에러
        ("'GPX 파일 파싱 오류입니다.'", "'GPXファイルの解析エラーです。'"),
    ],

    'heic-viewer.html': [
        # LD+JSON description
        ('"아이폰 .heic 사진을 코덱 설치 없이 브라우저에서 열어보고 PNG/JPG로 저장하는 온라인 뷰어"',
         '"iPhoneの.heic写真をコーデックインストールなしでブラウザで開きPNG/JPGで保存するオンラインビューア"'),
        # 로딩 메시지 (HTML)
        ('>HEIC 파일 변환 중... (파일 크기에 따라 수초 소요)<',
         '>HEICファイル変換中...（ファイルサイズにより数秒かかります）<'),
        # JS 텍스트 (template literal)
        ('개의 이미지가 포함되어 있습니다. 첫 번째 이미지를 표시합니다.',
         '枚の画像が含まれています。最初の画像を表示します。'),
        ('이 HEIC 파일에는 ${result.length}',
         'このHEICファイルには${result.length}'),
        ("'HEIC 파일을 변환하는 중 오류가 발생했습니다: '",
         "'HEICファイルの変換中にエラーが発生しました: '"),
    ],

    'ics-viewer.html': [
        # JS 에러
        ("'이벤트를 찾을 수 없습니다. 올바른 .ics 파일인지 확인하세요.'",
         "'イベントが見つかりません。正しい.icsファイルか確認してください。'"),
    ],

    'json-viewer.html': [
        # LD+JSON description
        ('"JSON 파일을 트리 구조로 보여주는 온라인 뷰어. 접기/펼치기, 실시간 검색 지원."',
         '"JSONファイルをツリー構造で表示するオンラインビューア。折りたたみ・展開・リアルタイム検索に対応。"'),
        # JS 에러
        ("'JSON 파싱 오류: '", "'JSON解析エラー: '"),
    ],

    'm3u-viewer.html': [
        # JS 에러
        ("'재생목록 항목을 찾을 수 없습니다.'", "'再生リストの項目が見つかりません。'"),
    ],

    'markdown-viewer.html': [
        # LD+JSON description
        ('".md 마크다운 파일을 HTML로 렌더링해서 미리보는 온라인 뷰어"',
         '".mdマークダウンファイルをHTMLでレンダリングしてプレビューするオンラインビューア"'),
    ],

    'msg-viewer.html': [
        # JS 에러
        ("'MSG 파일을 파싱할 수 없습니다.'", "'MSGファイルを解析できません。'"),
        ("'첨부파일'", "'添付ファイル'"),
        ("'파싱 오류: ' + e.message", "'解析エラー: ' + e.message"),
    ],

    'odt-viewer.html': [
        # JS 에러
        ("'content.xml을 찾을 수 없습니다. 올바른 ODT/ODS 파일인지 확인하세요.'",
         "'content.xmlが見つかりません。正しいODT/ODSファイルか確認してください。'"),
        ("'파싱 오류: ' + e.message", "'解析エラー: ' + e.message"),
    ],

    'pptx-viewer.html': [
        # LD+JSON description
        ('"파워포인트 없이 .pptx 파일을 브라우저에서 열어보는 무료 온라인 뷰어."',
         '"PowerPointなしで.pptxファイルをブラウザで開く無料オンラインビューア。"'),
        # JS 에러
        ("'.pptx 파일만 지원합니다.'", "'.pptxファイルのみ対応しています。'"),
        ("'Slides를 찾을 수 없습니다.'", "'スライドが見つかりません。'"),
        ("'파일 파싱 오류: ' + e.message", "'ファイル解析エラー: ' + e.message"),
        # HTML alt 속성
        ('alt="Slides 이미지"', 'alt="スライド画像"'),
    ],

    'psd-viewer.html': [
        # LD+JSON description
        ('"Photoshop 없이 .psd 파일을 브라우저에서 무료로 열어보는 온라인 뷰어. 레이어 목록 확인 지원."',
         '"Photoshopなしで.psdファイルをブラウザで無料で開くオンラインビューア。レイヤー一覧確認に対応。"'),
        # 로딩 메시지 (HTML)
        ('>PSD 파일 분석 중...<', '>PSDファイル解析中...<'),
        # JS 에러
        ("'합성 이미지를 추출할 수 없습니다.'", "'合成画像を抽出できません。'"),
    ],

    'rtf-viewer.html': [
        # JS 에러
        ("'올바른 RTF 파일이 아닙니다.'", "'正しいRTFファイルではありません。'"),
    ],

    'srt-viewer.html': [
        # JS 에러
        ("'자막 항목을 찾을 수 없습니다. 올바른 SRT/VTT 파일인지 확인하세요.'",
         "'字幕項目が見つかりません。正しいSRT/VTTファイルか確認してください。'"),
        # stats 텍스트 (JS 문자열)
        ("+'개 자막 · '", "+'件の字幕 · '"),
        ("'올바른 VTT 파일이 아닙니다.'", "'正しいVTTファイルではありません。'"),
    ],

    'stl-viewer.html': [
        # LD+JSON description
        ('".stl 3D 프린팅 파일을 브라우저에서 무료로 회전·확대해서 확인하는 온라인 3D 뷰어"',
         '".stl 3Dプリントファイルをブラウザで無料で回転·拡大確認するオンライン3Dビューア"'),
    ],

    'svg-viewer.html': [
        # LD+JSON description
        ('"SVG 파일 미리보기, 소스 확인, PNG 변환 다운로드를 제공하는 온라인 뷰어"',
         '"SVGファイルのプレビュー、ソース確認、PNG変換ダウンロードを提供するオンラインビューア"'),
    ],

    'tar-viewer.html': [
        # JS 에러
        ("'파일 크기가 100MB를 초과합니다.'", "'ファイルサイズが100MBを超えています。'"),
        ("'파싱 오류: '+e2.message", "'解析エラー: '+e2.message"),
        ("'TAR 구조를 파싱할 수 없습니다. 올바른 TAR/TAR.GZ 파일인지 확인하세요.'",
         "'TAR構造を解析できません。正しいTAR/TAR.GZファイルか確認してください。'"),
        # 통계 행 라벨
        ("['파일 수',fileCount+'개'],['폴더 수',dirs+'개'],['전체 크기',formatBytes(totalSize)]",
         "['ファイル数',fileCount+'件'],['フォルダ数',dirs+'件'],['合計サイズ',formatBytes(totalSize)]"),
        # 파일 목록 타이틀 (template literal)
        ("`📂 파일 목록 (${files.length}개)`", "`📂 ファイル一覧 (${files.length}件)`"),
    ],

    'tiff-viewer.html': [
        # JS 에러
        ("'TIFF 파일을 읽을 수 없습니다.'", "'TIFFファイルを読み込めません。'"),
        ("'파싱 오류: ' + e.message", "'解析エラー: ' + e.message"),
    ],

    'torrent-viewer.html': [
        # JS 에러
        ("'올바른 torrent 파일이 아닙니다.'", "'正しいTorrentファイルではありません。'"),
        # 통계 행
        ("['파일 수', files.length + '개']", "['ファイル数', files.length + '件']"),
        ("'📂 파일 목록 (' + files.length + '개)'",
         "'📂 ファイル一覧 (' + files.length + '件)'"),
        ("'파싱 오류: ' + e.message", "'解析エラー: ' + e.message"),
    ],

    'vcf-viewer.html': [
        # JS 에러
        ("'VCF 파일을 파싱할 수 없습니다.'", "'VCFファイルを解析できません。'"),
        ("'연락처 정보를 찾을 수 없습니다.'", "'連絡先情報が見つかりません。'"),
    ],

    'xml-viewer.html': [
        # 탭 버튼
        ('>파일 업로드<', '>ファイルをアップロード<'),
        # JS 에러
        ("'파일을 읽을 수 없습니다: ' + e.message", "'ファイルを読み込めません: ' + e.message"),
        ("'XML 파싱 오류: '", "'XML解析エラー: '"),
    ],

    'yaml-viewer.html': [
        # JS 에러
        ("'YAML 파싱 오류: '", "'YAML解析エラー: '"),
    ],

    'zip-viewer.html': [
        # HTML span
        ('>파일 0개<', '>ファイル 0件<'),
        # JS 텍스트
        ("'파일 ' + fileCount + '개'", "'ファイル ' + fileCount + '件'"),
        ("'ZIP 파일을 읽을 수 없습니다: ' + err.message",
         "'ZIPファイルを読み込めません: ' + err.message"),
    ],
}

# ─────────────────────────────────────────────
# 실행
# ─────────────────────────────────────────────
ok = 0
skip = 0

for fname in sorted(os.listdir(JA_DIR)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(JA_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 공통 교체
    for old, new in COMMON:
        content = content.replace(old, new)

    # 파일별 교체
    if fname in FILE_SPECIFIC:
        for old, new in FILE_SPECIFIC[fname]:
            content = content.replace(old, new)

    if content == original:
        skip += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {fname}')
    ok += 1

print(f'\n완료: {ok}개 수정, {skip}개 변경없음')
