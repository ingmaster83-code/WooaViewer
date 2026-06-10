"""
WooaViewer KO 페이지 메타 디스크립션 CTR 최적화
- 기준: 네이버 서치어드바이저 노출 대비 CTR 개선
- 핵심: pptx 뷰어(469노출 0.9%), docx 파일 열기(498노출 0.6%), xlsx 파일 열기(483노출 0.4%)
- 전략: 키워드 선행, 구체적 기능 명시, 보일러플레이트 제거
"""
import re, os

BASE = 'C:/개인/wooahouse/WooaViewer'

PAGES = {
    'index.html': (
        'Word, Excel, PowerPoint',
        'Word·Excel·PowerPoint·PSD·CAD 등 36종 파일을 설치 없이 브라우저에서 무료로 열기. docx·xlsx·pptx 파일 열기, 회원가입 없이 바로 가능. 파일은 서버에 전송되지 않아 100% 안전 — 우아뷰어(WooaViewer)'
    ),
    # ── 노출 많고 CTR 낮은 핵심 3개 ───────────────────────────────────
    'pptx-viewer.html': (
        '파워포인트 없이 .pptx',
        'pptx 뷰어 무료 — 파워포인트 없이 .pptx 파일을 브라우저에서 바로 열기. 슬라이드별 텍스트·이미지 확인, 회원가입·설치 없이 즉시 사용. 파일은 서버에 전송되지 않아 100% 안전.'
    ),
    'docx-viewer.html': (
        'Microsoft Word 없이도 .docx',
        'docx 파일 열기 무료 — Word 없이 .docx 파일을 브라우저에서 즉시 열기. 텍스트·표·이미지 렌더링 지원, 회원가입·설치 없이 바로 가능. 파일은 서버에 전송되지 않아 100% 안전.'
    ),
    'xlsx-viewer.html': (
        'Microsoft Excel 없이도 .xlsx',
        'xlsx 파일 열기 무료 — Excel 없이 .xlsx·.xls·.csv 파일을 브라우저에서 즉시 열기. 다중 시트·셀 데이터 확인, 회원가입·설치 없이 바로 가능. 파일은 서버에 전송되지 않아 안전.'
    ),
    # ── 그 외 개선 ────────────────────────────────────────────────────
    'gpx-maker.html': (
        '지도를 클릭해 GPS 경로를 만들고',
        'GPX 파일 만들기 무료 — 지도를 클릭해 GPS 경로를 그리고 GPX 파일로 저장. 기존 GPX 수정도 가능, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'psd-viewer.html': (
        'Adobe Photoshop 없이도 .psd',
        'PSD 파일 뷰어 무료 — Photoshop 없이 .psd 파일을 브라우저에서 즉시 미리보기. 레이어 목록 확인·합성 이미지 표시, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'gpx-viewer.html': (
        '.gpx GPS 경로 파일을 업로드하면',
        'GPX 뷰어 무료 — .gpx GPS 경로 파일을 지도에 표시하고 거리·고도·포인트 분석. 설치·로그인 없이 브라우저에서 바로 사용, 파일은 서버에 전송되지 않아 안전.'
    ),
    'cbz-viewer.html': (
        '.cbz 만화책 파일을 업로드하면',
        'CBZ 뷰어 무료 — .cbz 만화책 파일을 브라우저에서 바로 열기. 이미지를 순서대로 확인, 설치·로그인 없이 즉시 사용 가능. 파일은 서버에 전송되지 않아 안전.'
    ),
    'csv-viewer.html': (
        'CSV 파일을 업로드하거나',
        'CSV 뷰어 무료 — CSV 파일을 깔끔한 테이블로 표시. 열 정렬·실시간 검색·구분자 선택 지원, 설치·로그인 없이 브라우저에서 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'diff-viewer.html': (
        '두 텍스트 파일 또는 코드를 비교',
        '파일 비교 뷰어 무료 — 두 텍스트·코드의 차이를 색상으로 즉시 확인. 추가·삭제·변경 줄 강조, 파일 업로드 또는 붙여넣기 지원. 서버 전송 없이 100% 안전.'
    ),
    'dxf-viewer.html': (
        'AutoCAD 없이도 .dxf',
        'DXF 뷰어 무료 — AutoCAD 없이 .dxf CAD 도면을 브라우저에서 즉시 열기. 확대·축소·도면 탐색 지원, 설치·로그인 없이 바로 가능. 파일은 서버에 전송되지 않아 안전.'
    ),
    'eml-viewer.html': (
        '.eml 이메일 파일을 업로드하면',
        'EML 뷰어 무료 — .eml 이메일 파일을 브라우저에서 즉시 열기. 발신자·수신자·제목·본문·첨부파일 목록 확인, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'epub-viewer.html': (
        '.epub 전자책 파일을 설치 없이',
        'EPUB 뷰어 무료 — .epub 전자책을 설치 없이 브라우저에서 바로 읽기. 페이지 넘기기·목차·챕터 이동 지원, 회원가입 없이 즉시 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'font-viewer.html': (
        'TTF, OTF, WOFF',
        '폰트 뷰어 무료 — TTF·OTF·WOFF 파일을 업로드하면 즉시 미리보기. 크기·굵기·이탤릭 조절, 한글·영문·숫자 캐릭터 확인. 설치·로그인 없이 바로 사용.'
    ),
    'gcode-viewer.html': (
        '.gcode 3D 프린터 슬라이서',
        'GCode 뷰어 무료 — 3D 프린터 .gcode 파일의 툴패스를 레이어별로 시각화. Cura·PrusaSlicer 파일 지원, 설치·로그인 없이 브라우저에서 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'heic-viewer.html': (
        '아이폰 .heic, .heif 사진을',
        'HEIC 뷰어 무료 — 아이폰 .heic·.heif 사진을 브라우저에서 바로 열기. 코덱 설치 없이 즉시 확인, PNG·JPG 변환 저장 가능. 파일은 서버에 전송되지 않아 안전.'
    ),
    'hex-viewer.html': (
        '모든 바이너리 파일을 업로드하면',
        'HEX 뷰어 무료 — 바이너리 파일을 업로드하면 16진수(HEX) 덤프를 브라우저에서 즉시 확인. 파일 시그니처·헤더 분석에 최적, 설치·로그인 없이 바로 사용.'
    ),
    'ics-viewer.html': (
        '.ics iCalendar 파일을 업로드하면',
        'ICS 뷰어 무료 — .ics iCalendar 파일을 브라우저에서 즉시 열기. 일정 제목·날짜·장소·설명 확인, Google 캘린더·Outlook 내보내기 지원. 설치·로그인 없이 바로 사용.'
    ),
    'ini-viewer.html': (
        '.ini .cfg .conf 설정 파일을',
        'INI 뷰어 무료 — .ini·.cfg·.conf 설정 파일을 섹션·키·값으로 정리해 표시. 설치·로그인 없이 브라우저에서 바로 사용, 파일은 서버에 전송되지 않아 안전.'
    ),
    'json-viewer.html': (
        'JSON 파일을 업로드하거나',
        'JSON 뷰어 무료 — JSON 파일을 트리 구조로 표시. 접기/펼치기·실시간 검색·오류 검출 지원, 설치·로그인 없이 브라우저에서 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'log-viewer.html': (
        '.log .txt 로그 파일을 업로드하면',
        '로그 뷰어 무료 — .log 파일을 업로드하면 ERROR·WARN·INFO·DEBUG 레벨별 색상 강조와 검색 기능 제공. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'm3u-viewer.html': (
        '.m3u .m3u8 재생목록 파일을',
        'M3U 뷰어 무료 — .m3u·.m3u8 재생목록 파일을 업로드하면 트랙 제목·재생 시간·URL을 표로 즉시 확인. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'markdown-viewer.html': (
        '.md 마크다운 파일을 업로드하거나',
        '마크다운 뷰어 무료 — .md 파일을 업로드하면 HTML로 즉시 렌더링. README·코드 블록 하이라이팅 지원, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'msg-viewer.html': (
        '.msg 아웃룩 이메일 파일을',
        'MSG 뷰어 무료 — Outlook 없이 .msg 이메일 파일을 브라우저에서 즉시 열기. 발신자·수신자·제목·본문 확인, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'odt-viewer.html': (
        '.odt .ods LibreOffice 문서',
        'ODT 뷰어 무료 — LibreOffice 없이 .odt·.ods 파일을 브라우저에서 즉시 열기. 문서 내용 확인, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'pdf-viewer.html': (
        'Adobe Acrobat 없이 PDF 파일을',
        'PDF 뷰어 무료 — Acrobat 없이 PDF 파일을 브라우저에서 즉시 열기. 페이지 이동·확대·축소 지원, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 100% 안전.'
    ),
    'rtf-viewer.html': (
        '.rtf 파일을 업로드하면',
        'RTF 뷰어 무료 — Word 없이 .rtf 파일을 브라우저에서 즉시 열기. 서버 전송 없이 100% 안전, 설치·로그인 없이 바로 사용.'
    ),
    'srt-viewer.html': (
        '.srt .vtt 자막 파일을',
        '자막 뷰어 무료 — .srt·.vtt 자막 파일을 업로드하면 번호·시간 코드·텍스트를 표로 즉시 확인. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'stl-viewer.html': (
        '.stl 3D 프린팅 모델 파일을',
        'STL 뷰어 무료 — .stl 3D 프린팅 모델을 브라우저에서 회전·확대·축소해 확인. 마우스로 360도 3D 뷰, 설치·로그인 없이 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'svg-viewer.html': (
        'SVG 파일을 업로드하거나 코드를',
        'SVG 뷰어 무료 — SVG 파일을 즉시 미리보기. 확대/축소·PNG 변환·소스 코드 확인 지원, 아이콘·벡터 이미지 확인에 최적. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'tar-viewer.html': (
        '.tar .tar.gz .tgz 아카이브',
        'TAR 뷰어 무료 — .tar·.tar.gz·.tgz 파일을 업로드하면 내부 파일 목록·크기를 즉시 확인. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'tiff-viewer.html': (
        '.tif .tiff 이미지 파일을',
        'TIFF 뷰어 무료 — .tif·.tiff 이미지를 브라우저에서 즉시 열기. 다중 페이지 TIFF 지원, 의료·스캔 이미지 확인에 최적. 설치·로그인 없이 바로 사용.'
    ),
    'torrent-viewer.html': (
        '.torrent 파일을 업로드하면',
        '토렌트 뷰어 무료 — .torrent 파일을 업로드하면 파일 목록·크기·트래커 정보를 즉시 확인. 실제 다운로드 없이 내용 미리보기, 설치·로그인 없이 바로 사용.'
    ),
    'vcf-viewer.html': (
        '.vcf vCard 연락처 파일을',
        'VCF 연락처 뷰어 무료 — .vcf vCard 파일을 업로드하면 이름·전화번호·이메일·주소·사진을 브라우저에서 즉시 확인. 설치·로그인 없이 바로 사용.'
    ),
    'xml-viewer.html': (
        '.xml 파일을 브라우저에서 무료로 트리',
        'XML 뷰어 무료 — .xml 파일을 트리 구조로 즉시 열기. 접기/펼치기·문법 강조 지원, RSS·SVG·HTML 등 XML 형식 모두 지원. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'yaml-viewer.html': (
        'YAML 파일을 업로드하거나',
        'YAML 뷰어 무료 — YAML 파일을 트리 구조로 표시. 오류 검출·접기/펼치기 지원, 설치·로그인 없이 브라우저에서 바로 사용. 파일은 서버에 전송되지 않아 안전.'
    ),
    'zip-viewer.html': (
        'ZIP 파일을 업로드하면 내부 파일 목록을',
        'ZIP 뷰어 무료 — ZIP 파일을 업로드하면 내부 파일 목록을 트리 구조로 표시. 텍스트·이미지 미리보기, 압축 해제 없이 내용 확인. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
}

ok_count = 0
fail_count = 0

for fname, (match_prefix, new_desc) in PAGES.items():
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f'  SKIP (없음): {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<meta name="description" content=")[^"]*(")'

    def replacer(m):
        current = m.group(0)
        if match_prefix in current:
            return m.group(1) + new_desc + m.group(2)
        return current

    new_content = re.sub(pattern, replacer, content)

    if new_content == content:
        print(f'  MISS: {fname} — "{match_prefix[:30]}"')
        fail_count += 1
        continue

    # og:description / twitter:description 동기화
    new_content = re.sub(
        r'(<meta property="og:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2),
        new_content
    )
    new_content = re.sub(
        r'(<meta name="twitter:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2),
        new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  OK: {fname}')
    ok_count += 1

print(f'\n완료: {ok_count}개 교체, {fail_count}개 실패')
