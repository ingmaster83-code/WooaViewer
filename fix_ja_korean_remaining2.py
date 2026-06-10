"""
WooaViewer JA - 잔존 한국어 2차 일본어 교체
UI 라벨, 버튼, stats 텍스트, placeholder 등
"""
import os, sys

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

FILE_SPECIFIC = {

    # ────────────── cbz-viewer ──────────────
    'cbz-viewer.html': [
        # template literal 페이지 카운터
        ('}페이지${', '}ページ${'),
    ],

    # ────────────── csv-viewer ──────────────
    'csv-viewer.html': [
        ('>탭 (\\t)</option>', '>タブ (\\t)</option>'),
        # placeholder 예시 데이터
        ('placeholder="이름,나이,도시&#10;홍길동,30,서울&#10;김철수,25,부산"',
         'placeholder="名前,年齢,都市&#10;山田太郎,30,東京&#10;田中花子,25,大阪"'),
        # stats
        ("${headers.length}열 · ${filtered}행", "${headers.length}列 · ${filtered}行"),
        # no-data row
        ('>검색 결과가 없습니다.</td>',   '>検索結果がありません。</td>'),
    ],

    # ────────────── diff-viewer ──────────────
    'diff-viewer.html': [
        # UI 라벨
        ('        원본 (A)',     '        元のテキスト (A)'),
        ('        변경본 (B)',   '        変更後 (B)'),
        ('placeholder="원본 텍스트 또는 코드를 붙여넣으세요..."',
         'placeholder="元のテキストまたはコードを貼り付けてください..."'),
        ('placeholder="변경된 텍스트 또는 코드를 붙여넣으세요..."',
         'placeholder="変更後のテキストまたはコードを貼り付けてください..."'),
        ('>🔍 비교하기<', '>🔍 比較<'),
        # JS 에러
        ("'원본(A)과 변경본(B) 중 하나 이상을 입력하세요.'",
         "'元のテキスト(A)か変更後(B)のどちらかを入力してください。'"),
        # stats
        ('+${adds} 추가</span>', '+${adds} 追加</span>'),
        ('-${dels} 삭제</span>', '-${dels} 削除</span>'),
        ('${sames} 동일</span>', '${sames} 同一</span>'),
        # hunk 생략 텍스트
        ('줄 생략) ...</div>`', '行省略) ...</div>`'),
        # 차이없음
        ('>차이점이 없습니다.</div>',  '>差分がありません。</div>'),
    ],

    # ────────────── docx-viewer ──────────────
    'docx-viewer.html': [
        ("'ファイルの読み込み中にエラーが発生しました. 올바른 .docx 파일인지 확인해주세요.'",
         "'ファイルの読み込み中にエラーが発生しました。正しい.docxファイルか確認してください。'"),
    ],

    # ────────────── dxf-viewer ──────────────
    'dxf-viewer.html': [
        ('>전체 보기<', '>全体表示<'),
        ('>확대 +<',   '>拡大 +<'),
        ('>축소 -<',   '>縮小 -<'),
        ("'표시할 도형이 없습니다'", "'表示する図形がありません'"),
        ('도형 ${entities.length}개', '図形 ${entities.length}件'),
    ],

    # ────────────── eml-viewer ──────────────
    'eml-viewer.html': [
        ("'(제목 없음)'", "'(件名なし)'"),
        ("['발신자', from]", "['送信者', from]"),
        ("['수신자', to]",  "['受信者', to]"),
        ("['참조', cc]",    "['CC', cc]"),
        ("['날짜', date]",  "['日付', date]"),
        ("['제목', subject]", "['件名', subject]"),
        ("=== '제목'",      "=== '件名'"),
        ("btn.textContent = '텍스트'", "btn.textContent = 'テキスト'"),
    ],

    # ────────────── epub-viewer ──────────────
    'epub-viewer.html': [
        ('>← 이전<', '>← 前へ<'),
        ('>다음 →<', '>次へ →<'),
        ('>목차<',   '>目次<'),
        ("'읽을 수 있는 챕터가 없습니다.'",
         "'読めるチャプターがありません。'"),
        ("'ファイルの読み込み中にエラーが発生しました. 올바른 .epub 파일인지 확인해주세요.'",
         "'ファイルの読み込み中にエラーが発生しました。正しい.epubファイルか確認してください。'"),
    ],

    # ────────────── font-viewer ──────────────
    'font-viewer.html': [
        # UI 라벨
        ('>미리보기 텍스트<', '>プレビューテキスト<'),
        ('>크기<',            '>サイズ<'),
        ('>굵기<',            '>太さ<'),
        ('>이탤릭<',          '>イタリック<'),
        ('>배경<',            '>背景<'),
        ('title="흰색"', 'title="白"'),
        ('title="검정"', 'title="黒"'),
        ('title="회색"', 'title="グレー"'),
        # 프리뷰 기본 텍스트
        ('>안녕하세요 Hello World 가나다라 ABCDEFGHIJ 0123456789<',
         '>こんにちは Hello World あいうえお ABCDEFGHIJ 0123456789<'),
        ('placeholder="안녕하세요 Hello World 가나다라 ABCDEFGHIJ 0123456789"',
         'placeholder="こんにちは Hello World あいうえお ABCDEFGHIJ 0123456789"'),
        # 문자 세트 섹션
        ('>영문 대문자<', '>大文字<'),
        ('>영문 소문자<', '>小文字<'),
        ('>숫자 · 특수문자<', '>数字 · 記号<'),
        ('>한글 가나다<',     '>かなカナ<'),
        # 한글 문자 블록 → 일본 문자
        ('가나다라마바사아자차카타파하 각난달람밥삿앗잖찬칸탄판한 각갈감강개객갱거건걸검겁것게겨격견결겸경',
         'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめも'),
        # stats
        ("형식: ${ext.toUpperCase()}", "形式: ${ext.toUpperCase()}"),
        # JS 에러
        ("'폰트 로드 실패: ' + err.message", "'フォントの読み込みに失敗しました: ' + err.message"),
    ],

    # ────────────── gcode-viewer ──────────────
    'gcode-viewer.html': [
        # 통계 라벨
        ('>총 이동<',      '>総移動<'),
        ('>절삭 이동<',    '>切削移動<'),
        ('>레이어(Z)<',    '>レイヤー(Z)<'),
        ('>크기(X×Y)<',   '>サイズ(X×Y)<'),
        # 버튼
        ('>급이동 표시<',  '>急速移動を表示<'),
        ('>초기화<',       '>リセット<'),
        # 범례
        ('>절삭 이동 (G1)<', '>切削移動 (G1)<'),
        # hint text (다른 파일에도 있음)
        ('>마우스 드래그: 이동 · 휠: 확대/축소<',
         '>マウスドラッグ: 移動 · ホイール: 拡大/縮小<'),
        # related card
        ('>GPX 만들기<', '>GPXを作成<'),
        # JS 에러
        ("'이동 명령(G0/G1)을 찾을 수 없습니다.'",
         "'移動コマンド(G0/G1)が見つかりません。'"),
        # stats 숫자 + 개
        (".toLocaleString() + '개'", ".toLocaleString() + '件'"),
        # 버튼 토글 텍스트
        ("'급이동 숨기기'", "'急速移動を非表示'"),
        ("'급이동 표시'",   "'急速移動を表示'"),
    ],

    # ────────────── gpx-viewer ──────────────
    'gpx-viewer.html': [
        ('>GPX 만들기<', '>GPXを作成<'),
        ("'트랙 포인트 또는 웨이포인트를 찾을 수 없습니다.'",
         "'トラックポイントまたはウェイポイントが見つかりません。'"),
        (">트랙 포인트<", ">トラックポイント<"),
        (">총 거리<",     ">総距離<"),
        (">웨이포인트<",  ">ウェイポイント<"),
        (">고도 범위<",   ">標高範囲<"),
    ],

    # ────────────── heic-viewer ──────────────
    'heic-viewer.html': [
        ('alt="HEIC 미리보기"', 'alt="HEICプレビュー"'),
        ('>PNG로 저장<', '>PNGで保存<'),
        ('>JPG로 저장<', '>JPGで保存<'),
    ],

    # ────────────── hex-viewer ──────────────
    'hex-viewer.html': [
        ('표시: ${bytes.length}바이트 (전체: ${formatBytes(fsize)})',
         '表示: ${bytes.length}バイト (合計: ${formatBytes(fsize)})'),
    ],

    # ────────────── ics-viewer ──────────────
    'ics-viewer.html': [
        ("'(제목 없음)'", "'(タイトルなし)'"),
        ("irow('시작', ",   "irow('開始', "),
        ("irow('종료', ",   "irow('終了', "),
        ("irow('장소', ",   "irow('場所', "),
        ("irow('주최자', ", "irow('主催者', "),
        ("irow('상태', ",   "irow('状態', "),
        ("irow('설명', ",   "irow('説明', "),
        ("${events.length}개 이벤트", "${events.length}件のイベント"),
    ],

    # ────────────── ini-viewer ──────────────
    'ini-viewer.html': [
        ("'(전역)'", "'(グローバル)'"),
        ("'INI/CFG 항목을 찾을 수 없습니다.'",
         "'INI/CFGの項目が見つかりません。'"),
        ("${sections.length}개 섹션 · ${total}개 항목",
         "${sections.length}個のセクション · ${total}個の項目"),
    ],

    # ────────────── json-viewer ──────────────
    'json-viewer.html': [
        ('>전체 펼치기<', '>すべて展開<'),
        ('>전체 접기<',   '>すべて折りたたむ<'),
        ("renderJSON(document.getElementById('jsonInput').value.trim(), '입력')",
         "renderJSON(document.getElementById('jsonInput').value.trim(), '入力')"),
        ("키 ${keys}개", "キー ${keys}件"),
        # array/object 개수
        ("${val.length}개</span>", "${val.length}件</span>"),
        ("${keys.length}개</span>", "${keys.length}件</span>"),
    ],

    # ────────────── log-viewer ──────────────
    'log-viewer.html': [
        ("${lines.length}줄</span>", "${lines.length}行</span>"),
    ],

    # ────────────── m3u-viewer ──────────────
    'm3u-viewer.html': [
        ("'(제목 없음)'", "'(タイトルなし)'"),
        ("${tracks.length}개 트랙", "${tracks.length}曲"),
        ("' · 총 '+fmtDur(td)", "' · 合計 '+fmtDur(td)"),
    ],

    # ────────────── markdown-viewer ──────────────
    'markdown-viewer.html': [
        ('placeholder="여기에 Markdown 텍스트를 붙여넣으세요..."',
         'placeholder="ここにMarkdownテキストを貼り付けてください..."'),
        ('>렌더링<', '>レンダリング<'),
        ("alert('내용을 입력해주세요.')",
         "alert('内容を入力してください。')"),
    ],

    # ────────────── msg-viewer ──────────────
    'msg-viewer.html': [
        ("'라이브러리 로딩에 실패했습니다. 새로고침 후 다시 시도하세요.'",
         "'ライブラリの読み込みに失敗しました。ページを再読み込みしてください。'"),
        ("['발신자', ", "['送信者', "),
        ("['수신자', ", "['受信者', "),
        ("['날짜', ",   "['日付', "),
        ("['제목', ",   "['件名', "),
        ("=== '제목'",  "=== '件名'"),
        ("'(제목 없음)'", "'(件名なし)'"),
        ("'(본문 없음)'", "'(本文なし)'"),
    ],

    # ────────────── odt-viewer ──────────────
    'odt-viewer.html': [
        ("'라이브러리 로딩에 실패했습니다.'",
         "'ライブラリの読み込みに失敗しました。'"),
    ],

    # ────────────── pptx-viewer ──────────────
    'pptx-viewer.html': [
        ('>⊞ 그리드<', '>⊞ グリッド<'),
        ('>≡ 목록<',   '>≡ リスト<'),
        ('>🔄 다시 열기<', '>🔄 再度開く<'),
        ("Slides ${slides.length}장",  "スライド ${slides.length}枚"),
        ('>내용 없음<', '>内容なし<'),
    ],

    # ────────────── psd-viewer ──────────────
    'psd-viewer.html': [
        ('alt="PSD 미리보기"', 'alt="PSDプレビュー"'),
        ('>레이어 목록<', '>レイヤー一覧<'),
        ('레이어 ${layers.length}개', 'レイヤー ${layers.length}件'),
        ("'그룹'",   "'グループ'"),
        ("'텍스트'", "'テキスト'"),
        ("'레이어'", "'レイヤー'"),
    ],

    # ────────────── stl-viewer ──────────────
    'stl-viewer.html': [
        ('>와이어프레임<', '>ワイヤーフレーム<'),
        ('>초기화<',       '>リセット<'),
        ('>마우스 드래그: 회전 · 휠: 확대/축소 · 우클릭 드래그: 이동<',
         '>マウスドラッグ: 回転 · ホイール: 拡大/縮小 · 右クリックドラッグ: 移動<'),
        ('>GPX 만들기<', '>GPXを作成<'),
        ("'솔리드'",       "'ソリッド'"),
        ("'와이어프레임'", "'ワイヤーフレーム'"),
    ],

    # ────────────── svg-viewer ──────────────
    'svg-viewer.html': [
        ('>코드 입력<',       '>コード入力<'),
        ('>미리보기<',        '>プレビュー<'),
        ('>확대:<',           '>拡大:<'),
        ('>소스 보기<',       '>ソースを表示<'),
        ('>PNG 다운로드<',    '>PNGダウンロード<'),
        ('>SVG 다운로드<',    '>SVGダウンロード<'),
        ('>배경:<',           '>背景:<'),
        ('title="흰색"', 'title="白"'),
        ('title="검정"', 'title="黒"'),
        ('title="회색"', 'title="グレー"'),
        ('alt="SVG 미리보기"', 'alt="SVGプレビュー"'),
        ("'SVG 형식이 아닙니다. <svg ...> 태그가 필요합니다.'",
         "'SVG形式ではありません。<svg ...>タグが必要です。'"),
        ("'소스 닫기'",  "'ソースを閉じる'"),
        ("'소스 보기'",  "'ソースを表示'"),
    ],

    # ────────────── tar-viewer ──────────────
    'tar-viewer.html': [
        (">... 외 ${files.length-500}개</div>`",
         ">... 他 ${files.length-500}件</div>`"),
    ],

    # ────────────── tiff-viewer ──────────────
    'tiff-viewer.html': [
        ("'라이브러리 로딩에 실패했습니다.'",
         "'ライブラリの読み込みに失敗しました。'"),
        ("tiffPages.length + '페이지'", "tiffPages.length + 'ページ'"),
    ],

    # ────────────── torrent-viewer ──────────────
    'torrent-viewer.html': [
        ("['이름', name]",               "['ファイル名', name]"),
        ("['전체 크기', formatBytes(totalSize)]",
         "['合計サイズ', formatBytes(totalSize)]"),
        ("['트래커', announce]",         "['トラッカー', announce]"),
        ("['설명', comment]",            "['説明', comment]"),
        ("['생성일', creationDate]",     "['作成日', creationDate]"),
        ("['생성 앱', createdBy]",       "['作成ツール', createdBy]"),
        (">... 외 ${files.length-500}개</div>`",
         ">... 他 ${files.length-500}件</div>`"),
    ],

    # ────────────── vcf-viewer ──────────────
    'vcf-viewer.html': [
        # 전화번호 타입
        ("?'휴대폰':params.includes('work')?'직장':params.includes('home')?'집':'전화'",
         "?'携帯':params.includes('work')?'会社':params.includes('home')?'自宅':'電話'"),
        ("row('조직', c.org)",       "row('会社', c.org)"),
        ("row('직책', c.title)",     "row('役職', c.title)"),
        ("row('이메일', e)",         "row('メール', e)"),
        ("row('주소', a)",           "row('住所', a)"),
        ("row('생년월일', c.bday)",  "row('生年月日', c.bday)"),
        ("row('웹사이트', c.url)",   "row('ウェブサイト', c.url)"),
        ("row('메모', c.note",       "row('メモ', c.note"),
        ("${contacts.length}개 연락처", "${contacts.length}件の連絡先"),
    ],

    # ────────────── xml-viewer ──────────────
    'xml-viewer.html': [
        (">붙여넣기<",     ">貼り付け<"),
        ('placeholder="XML을 여기에 붙여넣으세요..."',
         'placeholder="ここにXMLを貼り付けてください..."'),
        (">트리로 보기<",  ">ツリーで表示<"),
        (">모두 펼치기<",  ">すべて展開<"),
        (">모두 접기<",    ">すべて折りたたむ<"),
        ("'XML을 입력해주세요.'", "'XMLを入力してください。'"),
        ("parseAndRender(text, '붙여넣기')", "parseAndRender(text, '貼り付け')"),
        ("' · 요소 ' + nodeCount.toLocaleString() + '개'",
         "' · 要素 ' + nodeCount.toLocaleString() + '件'"),
    ],

    # ────────────── yaml-viewer ──────────────
    'yaml-viewer.html': [
        (">전체 펼치기<", ">すべて展開<"),
        (">전체 접기<",   ">すべて折りたたむ<"),
        ("renderYAML(text, '입력'", "renderYAML(text, '入力'"),
        ("키 ${keys}개",           "キー ${keys}件"),
        # array/object 개수
        ("${val.length}개</span>",   "${val.length}件</span>"),
        ("${keys.length}개</span>",  "${keys.length}件</span>"),
    ],

    # ────────────── zip-viewer ──────────────
    'zip-viewer.html': [
        # LD+JSON name
        ('"name":"ZIP 내용물 뷰어"', '"name":"ZIP ビューア"'),
        ('>폴더 0개<',  '>フォルダ 0件<'),
        ('>총 0 KB<',   '>合計 0 KB<'),
        ('>닫기<',      '>閉じる<'),
        ("'폴더 ' + folderCount + '개'", "'フォルダ ' + folderCount + '件'"),
        ("'총 ' + fmtSize(totalSize)", "'合計 ' + fmtSize(totalSize)"),
    ],
}

# ─────────────────────────────────────────────
ok = 0; skip = 0

for fname in sorted(os.listdir(JA_DIR)):
    if not fname.endswith('.html'):
        continue
    if fname not in FILE_SPECIFIC:
        skip += 1
        continue

    fpath = os.path.join(JA_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in FILE_SPECIFIC[fname]:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f'  MISS [{fname}]: {repr(old[:60])}')

    if content == original:
        skip += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {fname}')
    ok += 1

print(f'\n완료: {ok}개 수정, {skip}개 변경없음')
