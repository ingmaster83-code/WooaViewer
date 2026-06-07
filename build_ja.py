"""
WooaViewer JA(日本語) 버전 빌드 스크립트
- EN 파일을 기반으로 ja/ 디렉토리에 일본어 파일 생성
- JS 파일도 함께 준비
"""
import os, re, shutil

BASE = 'C:/개인/wooahouse/WooaViewer'
EN_DIR = os.path.join(BASE, 'en')
JA_DIR = os.path.join(BASE, 'ja')
JS_DIR = os.path.join(BASE, 'js')
SHARED_JS = 'C:/개인/wooahouse/shared-js'

# ── 파일별 메타 정보 딕셔너리 ─────────────────────────────────────────────
PAGE_META = {
    'index.html': {
        'title': 'インストール不要の無料オンラインファイルビューア — DOCX XLSX DXF PSD HEICなど36形式 | WooaViewer',
        'desc': 'Word、Excel、CAD、Photoshop、HEIC、GCode、字幕、GPX、HEXなどをブラウザで無料で開く — インストール不要。36ファイル形式対応、ファイルはサーバーに送信されません。',
        'kw': 'ファイルビューア, DOCXビューア, XLSXビューア, DXFビューア, PSDビューア, STLビューア, HEICビューア, GCodeビューア, XMLビューア, Markdownビューア, JSONビューア, CSVビューア, ZIPビューア, SVGビューア, 無料ファイルビューア, オンラインファイルビューア, WooaViewer',
        'h1': 'インストール不要 — あらゆるファイルを開く',
    },
    'docx-viewer.html': {
        'title': 'DOCX ビューア 無料オンライン インストール不要 — Microsoft Wordなしでワード文書を開く | WooaViewer',
        'desc': 'Microsoft Wordなしでブラウザで.docxファイルを無料で開く。テキスト、表、画像を表示。ファイルはサーバーに送信されません — 100%プライベート、インストール不要。',
        'kw': 'DOCXビューア, Wordビューア, docxを開く, Wordファイルを開く, 無料DOCXビューア, オンラインWordビューア',
        'h1': 'DOCX ビューア — Wordファイルを無料でオンラインで開く',
        'tool_desc': '.docxファイルをアップロードして、Microsoft Wordなしで開いて読む。テキスト、表、画像を表示します。すべての処理はブラウザ内で行われます。',
    },
    'xlsx-viewer.html': {
        'title': 'XLSX ビューア 無料オンライン インストール不要 — Microsoft Excelなしでエクセルを開く | WooaViewer',
        'desc': 'Microsoft Excelなしでブラウザで.xlsx、.xlsファイルを無料で開く。複数シートタブとセルデータの表示に対応。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'XLSXビューア, Excelビューア, スプレッドシートビューア, xlsxを開く, XLSビューア, 無料Excelビューア',
        'h1': 'XLSX ビューア — Excelファイルを無料でオンラインで開く',
        'tool_desc': '.xlsx、.xlsファイルをアップロードして、Microsoft Excelなしで開く。複数シートタブとセルデータの表示に対応。',
    },
    'markdown-viewer.html': {
        'title': 'Markdown ビューア 無料オンライン インストール不要 — .mdファイルをレンダリング・プレビュー | WooaViewer',
        'desc': 'Markdown（.md）ファイルをアップロードまたは貼り付けてHTMLとして即座にレンダリング。README.mdプレビューとコードブロックのシンタックスハイライトに対応。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'Markdownビューア, mdファイルビューア, Markdownプレビュー, READMEビューア',
        'h1': 'Markdown ビューア — .mdファイルを無料でレンダリング',
        'tool_desc': 'Markdown（.md）ファイルをアップロードまたは貼り付けてHTMLとして即座にレンダリング。README.mdプレビューとコードブロックのシンタックスハイライトに対応。',
    },
    'epub-viewer.html': {
        'title': 'EPUB ビューア 無料オンライン インストール不要 — ブラウザで電子書籍を読む | WooaViewer',
        'desc': 'アプリなしでブラウザで.epub電子書籍ファイルを無料で読む。ページめくり、目次ナビゲーション、章ジャンプに対応。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'EPUBビューア, 電子書籍ビューア, epubを開く, ブラウザで電子書籍',
        'h1': 'EPUB ビューア — 電子書籍を無料でオンラインで読む',
        'tool_desc': '.epub電子書籍ファイルをアップロードしてブラウザで読む。ページめくり、目次ナビゲーション、章ジャンプに対応。',
    },
    'pptx-viewer.html': {
        'title': 'PPTX ビューア 無料オンライン インストール不要 — PowerPointなしでスライドを開く | WooaViewer',
        'desc': 'Microsoft PowerPointなしでブラウザで.pptxファイルを無料で開く。スライドのタイトル、本文テキストを表示し、スライドをナビゲート。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'PPTXビューア, PowerPointビューア, pptxを開く, スライドビューア',
        'h1': 'PPTX ビューア — PowerPointファイルを無料でオンラインで開く',
        'tool_desc': '.pptxファイルをアップロードして、Microsoft PowerPointなしで開く。スライドのタイトルと本文テキストを表示。',
    },
    'eml-viewer.html': {
        'title': 'EML ビューア 無料オンライン インストール不要 — メールファイルを開く | WooaViewer',
        'desc': 'ブラウザで.emlメールファイルを無料で開く。送信者、受信者、件名、日付、メール本文（HTMLとテキスト）を表示。添付ファイルリストも表示。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'EMLビューア, メールファイルビューア, emlを開く, メールビューア',
        'h1': 'EML ビューア — メールファイルを無料でオンラインで開く',
        'tool_desc': '.emlメールファイルをアップロードして、送信者、受信者、件名、本文、添付ファイルを表示。',
    },
    'pdf-viewer.html': {
        'title': 'PDF ビューア — Adobeなしでオンラインで無料でPDFファイルを開く | WooaViewer',
        'desc': 'Adobe AcrobatなしでブラウザでPDFファイルを開く。ページナビゲーションとズームイン・アウト対応。ファイルはブラウザから外に出ません — 100%プライベート、無料、インストール不要。',
        'kw': 'PDFビューア, PDFを開く, オンラインPDFビューア, 無料PDFビューア',
        'h1': 'PDF ビューア',
        'tool_desc': 'PDFファイルをアップロードしてブラウザで開く。Adobe Acrobatは不要。ページナビゲーションとズーム対応。',
    },
    'rtf-viewer.html': {
        'title': 'RTF ビューア 無料オンライン インストール不要 — リッチテキスト形式ファイルを開く | WooaViewer',
        'desc': 'ブラウザで.rtfリッチテキスト形式ファイルを無料で開く。Wordは不要、サーバーアップロードなし。RTFドキュメントの内容を即座に表示、インストール不要。',
        'kw': 'RTFビューア, リッチテキストビューア, rtfを開く',
        'h1': 'RTF ビューア — リッチテキスト形式ファイルを無料でオンラインで開く',
        'tool_desc': '.rtfリッチテキスト形式ファイルをアップロードしてブラウザで開く。Wordは不要。',
    },
    'vcf-viewer.html': {
        'title': 'VCF ビューア 無料オンライン インストール不要 — vCard連絡先ファイルを開く | WooaViewer',
        'desc': 'ブラウザで.vcf vCard連絡先ファイルを開く。名前、電話番号、メール、住所、写真を表示。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'VCFビューア, vCardビューア, 連絡先ファイルビューア, vcfを開く',
        'h1': 'VCF ビューア — vCard連絡先ファイルを無料でオンラインで開く',
        'tool_desc': '.vcf vCard連絡先ファイルをアップロードして、名前、電話番号、メール、住所、写真を表示。',
    },
    'ics-viewer.html': {
        'title': 'ICS ビューア 無料オンライン インストール不要 — iCalendarファイルを開く | WooaViewer',
        'desc': 'ブラウザで.ics iCalendarファイルを開く。イベントタイトル、日時、場所、説明を表示。GoogleカレンダーとOutlookのエクスポートファイルをサポート。無料、インストール不要。',
        'kw': 'ICSビューア, iCalendarビューア, カレンダーファイルビューア, icsを開く',
        'h1': 'ICS ビューア — iCalendarファイルを無料でオンラインで開く',
        'tool_desc': '.ics iCalendarファイルをアップロードして、イベントタイトル、日時、場所、説明を表示。',
    },
    'msg-viewer.html': {
        'title': 'MSG ビューア 無料オンライン インストール不要 — Outlookメールファイルを開く | WooaViewer',
        'desc': 'ブラウザで.msg Outlookメールファイルを開く。送信者、受信者、件名、本文、添付ファイルを表示。Outlookは不要。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'MSGビューア, Outlookメールビューア, msgを開く',
        'h1': 'MSG ビューア — Outlookメールファイルを無料でオンラインで開く',
        'tool_desc': '.msg Outlookメールファイルをアップロードして、送信者、受信者、件名、本文、添付ファイルを表示。Outlookは不要。',
    },
    'odt-viewer.html': {
        'title': 'ODT ビューア 無料オンライン インストール不要 — LibreOfficeドキュメントを開く | WooaViewer',
        'desc': 'ブラウザで.odtおよび.ods LibreOffice / OpenDocumentファイルを開く。LibreOfficeもOpenOfficeも不要。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'ODTビューア, LibreOfficeビューア, odtを開く, OpenDocumentビューア',
        'h1': 'ODT ビューア — LibreOfficeドキュメントを無料でオンラインで開く',
        'tool_desc': '.odtおよび.odsファイルをアップロードしてブラウザで開く。LibreOfficeは不要。',
    },
    'dxf-viewer.html': {
        'title': 'DXF ビューア 無料オンライン インストール不要 — AutoCADなしでCAD図面ファイルを開く | WooaViewer',
        'desc': 'AutoCADなしでブラウザで.dxf CAD図面ファイルを無料で開く。ズームとパンで図面を操作可能。ファイルはサーバーに送信されません — 100%プライベート、インストール不要。',
        'kw': 'DXFビューア, CADビューア, AutoCADビューア, dxfを開く',
        'h1': 'DXF ビューア — CAD図面を無料でオンラインで開く',
        'tool_desc': '.dxf CAD図面ファイルをアップロードして、AutoCADなしでブラウザで開く。ズームとパン操作に対応。',
    },
    'psd-viewer.html': {
        'title': 'PSD ビューア 無料オンライン インストール不要 — Photoshopなしでレイヤーリスト表示 | WooaViewer',
        'desc': 'Adobe Photoshopなしでブラウザで.psdファイルを無料でプレビュー。レイヤーリストと合成画像のプレビューを表示。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'PSDビューア, Photoshopビューア, psdを開く, レイヤービューア',
        'h1': 'PSD ビューア — Photoshopファイルを無料でオンラインで開く',
        'tool_desc': '.psdファイルをアップロードして、Adobe Photoshopなしでプレビュー。レイヤーリストと合成画像を表示。',
    },
    'heic-viewer.html': {
        'title': 'HEIC ビューア 無料オンライン インストール不要 — iPhoneの写真をコーデックなしで開く | WooaViewer',
        'desc': 'コーデックのインストールなしでブラウザでiPhoneの.heicおよび.heif写真を無料で開く。PNGまたはJPGとして変換・保存可能。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'HEICビューア, iPhoneフォトビューア, heicを開く, HEIFビューア',
        'h1': 'HEIC ビューア — iPhoneの写真を無料でオンラインで開く',
        'tool_desc': '.heicおよび.heifファイルをアップロードして、コーデックなしでブラウザで開く。PNGまたはJPGとして保存可能。',
    },
    'tiff-viewer.html': {
        'title': 'TIFF ビューア 無料オンライン インストール不要 — TIF/TIFFイメージファイルを開く | WooaViewer',
        'desc': 'ブラウザで.tifおよび.tiffイメージファイルを無料で開く。マルチページTIFF、医療用スキャン、プロフェッショナル画像を表示。ソフトウェア不要、インストール不要。',
        'kw': 'TIFFビューア, TIFビューア, tiffを開く, マルチページTIFF',
        'h1': 'TIFF ビューア — TIF/TIFFイメージファイルを無料でオンラインで開く',
        'tool_desc': '.tifおよび.tiffファイルをアップロードしてブラウザで開く。マルチページTIFFにも対応。',
    },
    'svg-viewer.html': {
        'title': 'SVG ビューア 無料オンライン インストール不要 — SVGファイルをプレビュー・ソース表示・PNG変換 | WooaViewer',
        'desc': 'SVGコードをアップロードまたは貼り付けて即座にプレビュー。ズーム/パン、PNG変換ダウンロード、SVGソースコード表示に対応。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'SVGビューア, SVGプレビュー, svgを開く, SVGをPNGに変換',
        'h1': 'SVG ビューア — SVGを無料でプレビュー・変換',
        'tool_desc': 'SVGファイルをアップロードまたはコードを貼り付けて即座にプレビュー。ズーム/パン、PNG変換、ソースコード表示に対応。',
    },
    'font-viewer.html': {
        'title': 'フォントビューア 無料オンライン インストール不要 — TTF OTF WOFFフォントファイルをプレビュー | WooaViewer',
        'desc': 'TTF、OTF、WOFF、WOFF2フォントファイルをアップロードして即座にプレビュー。フォントサイズ、ウェイト、イタリック体を調整。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'フォントビューア, TTFビューア, OTFビューア, WOFFビューア, フォントプレビュー',
        'h1': 'フォントビューア — フォントファイルを無料でプレビュー',
        'tool_desc': 'TTF、OTF、WOFF、WOFF2フォントファイルをアップロードして即座にプレビュー。フォントサイズ、ウェイト、イタリック体を調整可能。',
    },
    'json-viewer.html': {
        'title': 'JSON ビューア 無料オンライン インストール不要 — ツリー構造で表示・検索 | WooaViewer',
        'desc': 'JSONファイルをアップロードまたは貼り付けてインタラクティブなツリー構造で表示。キーの折りたたみ・展開、リアルタイム検索、構文エラー検出。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'JSONビューア, JSONツリービュー, jsonを開く, JSONフォーマッター',
        'h1': 'JSON ビューア — 無料オンラインツリービュー',
        'tool_desc': 'JSONファイルをアップロードまたは貼り付けてインタラクティブなツリー構造で表示。折りたたみ・展開、リアルタイム検索に対応。',
    },
    'xml-viewer.html': {
        'title': 'XML ビューア 無料オンライン インストール不要 — ツリー構造で表示・折りたたみ | WooaViewer',
        'desc': 'ブラウザで.xmlファイルを無料でインタラクティブなツリー構造として開く。要素の折りたたみ・展開、シンタックスハイライトに対応。RSS、SVG、HTMLすべてのXML形式をサポート。インストール不要。',
        'kw': 'XMLビューア, XMLツリービュー, xmlを開く, RSSビューア',
        'h1': 'XML ビューア — 無料オンラインツリービュー',
        'tool_desc': '.xmlファイルをアップロードまたは貼り付けてインタラクティブなツリー構造で表示。折りたたみ・展開に対応。',
    },
    'csv-viewer.html': {
        'title': 'CSV ビューア 無料オンライン インストール不要 — CSVファイルをテーブルとして表示 | WooaViewer',
        'desc': 'CSVファイルをアップロードまたは貼り付けてテーブルとして表示。列の並び替え、リアルタイム検索、区切り文字の選択に対応。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'CSVビューア, CSVテーブル, csvを開く, CSVファイルビューア',
        'h1': 'CSV ビューア — 無料オンライン',
        'tool_desc': 'CSVファイルをアップロードまたは貼り付けてテーブルとして表示。列の並び替えとリアルタイム検索に対応。',
    },
    'yaml-viewer.html': {
        'title': 'YAML ビューア 無料オンライン インストール不要 — YAMLファイルをツリー構造で表示 | WooaViewer',
        'desc': 'YAML（.yaml/.yml）ファイルをアップロードまたは貼り付けてインタラクティブなツリー構造として表示。ノードの折りたたみ・展開、設定ファイルとCI/CDパイプラインをサポート。インストール不要。',
        'kw': 'YAMLビューア, YAMLツリービュー, yamlを開く, ymlビューア',
        'h1': 'YAML ビューア — 無料オンラインツリービュー',
        'tool_desc': 'YAML（.yaml/.yml）ファイルをアップロードまたは貼り付けてインタラクティブなツリーとして表示。',
    },
    'ini-viewer.html': {
        'title': 'INI CFG 設定ファイルビューア 無料オンライン | WooaViewer',
        'desc': '.ini、.cfg、.confの設定ファイルをアップロードして、セクション、キー、値をきれいなレイアウトで表示。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'INIビューア, CFGビューア, 設定ファイルビューア, iniを開く',
        'h1': 'INI / CFG 設定ファイルビューア — 設定ファイルを無料でオンラインで開く',
        'tool_desc': '.ini、.cfg、.confの設定ファイルをアップロードして、セクション、キー、値を表示。',
    },
    'hex-viewer.html': {
        'title': 'HEX ビューア 無料オンライン — バイナリファイルを16進ダンプとして表示 | WooaViewer',
        'desc': '任意のバイナリファイルをアップロードして、オフセット、16進値、ASCII表現で16進ダンプとして表示。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'HEXビューア, 16進ダンプ, バイナリビューア, hexを開く',
        'h1': 'HEX ビューア — バイナリファイルを16進ダンプとして表示',
        'tool_desc': 'バイナリファイルをアップロードして、オフセット、16進値、ASCII表現で16進ダンプとして表示。',
    },
    'diff-viewer.html': {
        'title': 'Diff ビューア 無料オンライン インストール不要 — 2つのテキストファイルを比較 | WooaViewer',
        'desc': '2つのテキストファイルを貼り付けるかアップロードして比較し、追加・削除・変更された行をハイライト表示。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'Diffビューア, テキスト比較, ファイル差分, diffを開く',
        'h1': 'Diff ビューア — テキストファイルを無料で比較',
        'tool_desc': '2つのテキストファイルを貼り付けるかアップロードして比較。追加・削除・変更された行をハイライト表示。',
    },
    'log-viewer.html': {
        'title': 'LOG ビューア 無料オンライン インストール不要 — ログファイルをシンタックスハイライトで表示 | WooaViewer',
        'desc': 'ブラウザで.logおよび.txtログファイルを開く。ERROR、WARN、INFO、DEBUGレベルのカラーハイライト、キーワード検索・フィルタリング。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'LOGビューア, ログファイルビューア, logを開く, シンタックスハイライト',
        'h1': 'LOG ビューア — ログファイルをシンタックスハイライトで無料で開く',
        'tool_desc': '.logおよび.txtログファイルをアップロードして開く。ERROR、WARN、INFO、DEBUGレベルのカラーハイライトとキーワード検索に対応。',
    },
    'zip-viewer.html': {
        'title': 'ZIP ビューア 無料オンライン インストール不要 — ZIPファイルの内容を表示 | WooaViewer',
        'desc': 'ZIPファイルをアップロードしてツリー構造で内容を表示。内部のテキストファイルと画像ファイルをクリックしてプレビュー。解凍せずにZIPの内容を確認。インストール不要。',
        'kw': 'ZIPビューア, ZIPファイルビューア, zipを開く, アーカイブビューア',
        'h1': 'ZIP ビューア — ZIPの内容を無料でオンラインで表示',
        'tool_desc': 'ZIPファイルをアップロードしてツリー構造で内容を表示。テキストと画像ファイルのプレビューに対応。',
    },
    'tar-viewer.html': {
        'title': 'TAR GZ TGZ アーカイブビューア 無料オンライン | WooaViewer',
        'desc': '.tar、.tar.gz、.tgzアーカイブファイルをアップロードして、ブラウザでファイルリストとサイズを表示。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'TARビューア, GZビューア, TGZビューア, アーカイブビューア',
        'h1': 'TAR / GZ / TGZ アーカイブビューア — TARファイルを無料でオンラインで開く',
        'tool_desc': '.tar、.tar.gz、.tgzアーカイブファイルをアップロードして、ファイルリストとサイズを表示。',
    },
    'torrent-viewer.html': {
        'title': 'トレントビューア 無料オンライン インストール不要 — .torrentファイルの内容を表示 | WooaViewer',
        'desc': '.torrentファイルをアップロードして、ファイルリスト、名前、サイズ、トラッカー情報を表示。ダウンロードせずにトレントの内容をプレビュー。無料、サーバーアップロードなし、インストール不要。',
        'kw': 'トレントビューア, torrentビューア, torrentを開く',
        'h1': 'トレントビューア — .torrentファイルの内容を無料でオンラインで表示',
        'tool_desc': '.torrentファイルをアップロードして、ファイルリスト、名前、サイズ、トラッカー情報を表示。',
    },
    'cbz-viewer.html': {
        'title': 'CBZ コミックビューア 無料オンライン | WooaViewer',
        'desc': '.cbzコミックファイルをブラウザで開く。ページを画像として直接表示。無料、インストール不要、サーバーアップロードなし。最大50ページ表示。',
        'kw': 'CBZビューア, コミックビューア, cbzを開く, 漫画ビューア',
        'h1': 'CBZ コミックビューア — CBZファイルを無料でオンラインで開く',
        'tool_desc': '.cbzコミックファイルをアップロードして、ページを画像として表示。最大50ページ対応。',
    },
    'srt-viewer.html': {
        'title': 'SRT VTT 字幕ビューア 無料オンライン — 字幕ファイルを開く | WooaViewer',
        'desc': 'ブラウザで.srtおよび.vtt字幕ファイルを開く。タイムコードとテキストをきれいなテーブルで表示。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'SRTビューア, VTTビューア, 字幕ビューア, srtを開く',
        'h1': 'SRT / VTT 字幕ビューア — 字幕ファイルを無料でオンラインで開く',
        'tool_desc': '.srtおよび.vtt字幕ファイルをアップロードして、タイムコードとテキストをテーブルで表示。',
    },
    'm3u-viewer.html': {
        'title': 'M3U M3U8 プレイリストビューア 無料オンライン | WooaViewer',
        'desc': '.m3uまたは.m3u8プレイリストファイルをアップロードして、トラックタイトル、再生時間、URLをきれいなテーブルで表示。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'M3Uビューア, M3U8ビューア, プレイリストビューア, m3uを開く',
        'h1': 'M3U / M3U8 プレイリストビューア — プレイリストファイルを無料でオンラインで開く',
        'tool_desc': '.m3uまたは.m3u8プレイリストファイルをアップロードして、トラックタイトル、再生時間、URLを表示。',
    },
    'stl-viewer.html': {
        'title': 'STL ビューア 無料オンライン インストール不要 — 3Dプリントモデルファイルを表示 | WooaViewer',
        'desc': 'ブラウザで.stl 3Dプリントモデルファイルを無料で表示。360° 3Dビューでモデルを回転、ズーム、検査。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'STLビューア, 3Dモデルビューア, stlを開く, 3Dプリントビューア',
        'h1': 'STL ビューア — 3Dモデルを無料でオンラインで表示',
        'tool_desc': '.stl 3Dプリントモデルファイルをアップロードして、360°で回転・ズーム・検査。',
    },
    'gcode-viewer.html': {
        'title': 'GCode ビューア 無料オンライン インストール不要 — 3Dプリンタの工具経路をレイヤーごとに可視化 | WooaViewer',
        'desc': 'ブラウザで.gcode 3Dプリンタスライサーファイルの工具経路をレイヤーごとに無料で可視化。CuraおよびPrusaSlicerのGCodeに対応。ファイルはサーバーに送信されません、インストール不要。',
        'kw': 'GCodeビューア, 3Dプリンタビューア, gcodeを開く, スライサービューア',
        'h1': 'GCode ビューア — 3Dプリンタファイルを無料で可視化',
        'tool_desc': '.gcodeファイルをアップロードして、3Dプリンタの工具経路をレイヤーごとに可視化。',
    },
    'gpx-viewer.html': {
        'title': 'GPX ビューア 無料オンライン — 地図上にGPSルートを表示 | WooaViewer',
        'desc': '.gpx GPSルートファイルをアップロードして地図上に表示し、距離、標高、トラックポイントを分析。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'GPXビューア, GPSビューア, gpxを開く, ルートビューア',
        'h1': 'GPX ビューア — GPSルートを地図上に無料で表示',
        'tool_desc': '.gpx GPSルートファイルをアップロードして地図上に表示。距離、標高、トラックポイントを分析。',
    },
    'gpx-maker.html': {
        'title': 'GPX メーカー — GPSルートを無料でオンラインで作成・編集 | WooaViewer',
        'desc': '地図上をクリックしてGPSルートを描き、GPXファイルとして保存。既存のGPXファイルを読み込んで編集・更新も可能。無料、インストール不要、サーバーアップロードなし。',
        'kw': 'GPXメーカー, GPSルート作成, gpxを作成, ルートエディタ',
        'h1': 'GPX メーカー',
        'tool_desc': '地図上をクリックしてGPSルートを描き、GPXファイルとして保存。既存のGPXファイルの編集も可能。',
    },
}

# ── index.html 특수 교체 (카테고리, 카드 설명, features 등) ────────────────
INDEX_REPLACES = [
    # hero
    ('Open Word, Excel, CAD, Photoshop files — <strong style="color:#FFD700;">100% Free</strong><br>No signup. Files never stored on a server.',
     'Word、Excel、CAD、Photoshopファイルを開く — <strong style="color:#FFD700;">100%無料</strong><br>会員登録不要。ファイルはサーバーに保存されません。'),
    ('📌 Add to Home Screen', '📌 ホーム画面に追加'),
    ('Need to work with PDF files?', 'PDFファイルが必要ですか？'),
    ('WooaPDF Free PDF Tools →', 'WooaPDF 無料PDFツール →'),
    # categories
    ('<span class="category-title">Document Viewer</span>', '<span class="category-title">ドキュメントビューア</span>'),
    ('<p class="category-desc">Open Office files like Word and Excel without installation</p>', '<p class="category-desc">WordやExcelなどのOfficeファイルをインストールなしで開く</p>'),
    ('<span class="category-title">Image &amp; Graphics</span>', '<span class="category-title">画像・グラフィックス</span>'),
    ('<p class="category-desc">Open CAD drawings, design files, and image formats without installation</p>', '<p class="category-desc">CAD図面・デザインファイル・画像形式をインストールなしで開く</p>'),
    ('<span class="category-title">Dev &amp; Data</span>', '<span class="category-title">開発・データ</span>'),
    ('<p class="category-desc">View code, config, and data files in a structured way</p>', '<p class="category-desc">コード・設定・データファイルを構造的に表示</p>'),
    ('<span class="category-title">Archive &amp; Media</span>', '<span class="category-title">アーカイブ・メディア</span>'),
    ('<p class="category-desc">Inspect archive files and media playlists</p>', '<p class="category-desc">アーカイブファイルとメディアプレイリストを検査</p>'),
    ('<span class="category-title">3D &amp; GPS</span>', '<span class="category-title">3D・GPS</span>'),
    ('<p class="category-desc">Visualize 3D model files and GPS route data</p>', '<p class="category-desc">3Dモデルファイルとグルートデータを可視化</p>'),
    # tool cards - desc
    ('<div class="tool-desc">Open .docx documents without Word</div>', '<div class="tool-desc">Wordなしで.docxを開く</div>'),
    ('<div class="tool-desc">Open .xlsx spreadsheets without Excel</div>', '<div class="tool-desc">Excelなしで.xlsxを開く</div>'),
    ('<div class="tool-desc">View .md files rendered as HTML</div>', '<div class="tool-desc">.mdファイルをHTMLとして表示</div>'),
    ('<div class="tool-desc">Read .epub eBook files in your browser</div>', '<div class="tool-desc">ブラウザで.epubの電子書籍を読む</div>'),
    ('<div class="tool-desc">Open .pptx slides without PowerPoint</div>', '<div class="tool-desc">PowerPointなしで.pptxを開く</div>'),
    ('<div class="tool-desc">View .eml email sender, body &amp; attachments</div>', '<div class="tool-desc">.emlメールの送信者・本文・添付ファイルを表示</div>'),
    ('<div class="tool-desc">Open .pdf files in your browser without Adobe Acrobat</div>', '<div class="tool-desc">Acrobatなしで.pdfをブラウザで開く</div>'),
    ('<div class="tool-desc">Open .rtf Rich Text Format files without Word</div>', '<div class="tool-desc">Wordなしで.rtfを開く</div>'),
    ('<div class="tool-desc">View .vcf vCard contact files — name, phone, email</div>', '<div class="tool-desc">.vcf連絡先ファイルを表示</div>'),
    ('<div class="tool-desc">View .ics calendar events — date, location, details</div>', '<div class="tool-desc">.icsカレンダーイベントを表示</div>'),
    ('<div class="tool-desc">Open .msg Outlook email files without Outlook</div>', '<div class="tool-desc">Outlookなしで.msgを開く</div>'),
    ('<div class="tool-desc">Open .odt/.ods LibreOffice documents without LibreOffice</div>', '<div class="tool-desc">LibreOfficeなしで.odtを開く</div>'),
    ('<div class="tool-desc">Open .dxf CAD drawings without AutoCAD</div>', '<div class="tool-desc">AutoCADなしで.dxfを開く</div>'),
    ('<div class="tool-desc">Preview .psd files without Photoshop</div>', '<div class="tool-desc">Photoshopなしで.psdをプレビュー</div>'),
    ('<div class="tool-desc">Open .heic iPhone photos — save as PNG/JPG</div>', '<div class="tool-desc">iPhoneの.heic写真を開く — PNG/JPGで保存</div>'),
    ('<div class="tool-desc">Open .tif/.tiff multi-page images in your browser</div>', '<div class="tool-desc">マルチページの.tif/.tiffを開く</div>'),
    ('<div class="tool-desc">Preview SVG, view source, convert to PNG</div>', '<div class="tool-desc">SVGをプレビュー・ソース表示・PNGに変換</div>'),
    ('<div class="tool-desc">Preview TTF/OTF/WOFF font files, adjust size &amp; weight</div>', '<div class="tool-desc">TTF/OTF/WOFFフォントをプレビュー</div>'),
    ('<div class="tool-desc">View JSON files as an interactive tree</div>', '<div class="tool-desc">JSONをインタラクティブなツリーで表示</div>'),
    ('<div class="tool-desc">View XML files as a collapsible tree</div>', '<div class="tool-desc">XMLを折りたたみ可能なツリーで表示</div>'),
    ('<div class="tool-desc">View CSV files as a table, with sort &amp; search</div>', '<div class="tool-desc">CSVをテーブルとして表示（並べ替え・検索付き）</div>'),
    ('<div class="tool-desc">View .yaml / .yml files as an interactive tree</div>', '<div class="tool-desc">.yaml/.ymlファイルをツリーで表示</div>'),
    ('<div class="tool-desc">Parse .ini .cfg .conf config files into sections and keys</div>', '<div class="tool-desc">.ini/.cfg設定ファイルをセクション・キーに解析</div>'),
    ('<div class="tool-desc">View binary files as hex dump with ASCII column</div>', '<div class="tool-desc">バイナリファイルを16進ダンプで表示</div>'),
    ('<div class="tool-desc">Compare two text files and highlight differences</div>', '<div class="tool-desc">2つのテキストファイルを比較して差分をハイライト</div>'),
    ('<div class="tool-desc">View log files with ERROR/WARN/INFO color highlighting</div>', '<div class="tool-desc">ログファイルをカラーハイライトで表示</div>'),
    ('<div class="tool-desc">View ZIP contents list and preview files inside</div>', '<div class="tool-desc">ZIPの内容リストを表示・内部ファイルをプレビュー</div>'),
    ('<div class="tool-desc">View .tar .tar.gz .tgz archive file listings</div>', '<div class="tool-desc">.tar/.tar.gz/.tgzのファイルリストを表示</div>'),
    ('<div class="tool-desc">View .torrent file list, sizes and trackers — no downloading</div>', '<div class="tool-desc">.torrentのファイルリスト・トラッカーを表示</div>'),
    ('<div class="tool-desc">Read .cbz comic book page images in your browser</div>', '<div class="tool-desc">ブラウザで.cbzコミックを読む</div>'),
    ('<div class="tool-desc">View .srt .vtt subtitle timecodes and text</div>', '<div class="tool-desc">.srt/.vttの字幕タイムコードとテキストを表示</div>'),
    ('<div class="tool-desc">View .m3u .m3u8 playlist tracks, duration &amp; URLs</div>', '<div class="tool-desc">.m3u/.m3u8プレイリストのトラック・時間・URLを表示</div>'),
    ('<div class="tool-desc">Rotate and inspect .stl 3D printing files</div>', '<div class="tool-desc">.stl 3Dプリントファイルを回転・検査</div>'),
    ('<div class="tool-desc">Visualize .gcode toolpath layer by layer</div>', '<div class="tool-desc">.gcodeの工具経路をレイヤーごとに可視化</div>'),
    ('<div class="tool-desc">Display GPS routes on map with distance &amp; elevation</div>', '<div class="tool-desc">地図にGPSルートを表示（距離・標高付き）</div>'),
    ('<div class="tool-desc">Draw GPS routes on map, edit existing GPX &amp; save</div>', '<div class="tool-desc">地図上でGPSルートを描画・編集してGPXを保存</div>'),
    # features
    ('<div class="feature-title">100% Safe</div>', '<div class="feature-title">100%安全</div>'),
    ('<div class="feature-desc">Files are never sent to a server. All processing happens inside your browser.</div>', '<div class="feature-desc">ファイルはサーバーに送信されません。すべての処理はブラウザ内で行われます。</div>'),
    ('<div class="feature-title">Fast Loading</div>', '<div class="feature-title">高速読み込み</div>'),
    ('<div class="feature-desc">Processed instantly on your device — no upload wait.</div>', '<div class="feature-desc">デバイス上で即座に処理 — アップロード待機なし。</div>'),
    ('<div class="feature-title">Completely Free</div>', '<div class="feature-title">完全無料</div>'),
    ('<div class="feature-desc">All viewers are free — no signup required.</div>', '<div class="feature-desc">すべてのビューアは無料 — 会員登録不要。</div>'),
    ('<div class="feature-title">All Devices</div>', '<div class="feature-title">全デバイス対応</div>'),
    ('<div class="feature-desc">Responsive design works on PC, tablet, and smartphone.</div>', '<div class="feature-desc">レスポンシブデザインでPC、タブレット、スマートフォンで動作。</div>'),
    # header nav
    ('<a href="index.html">All Tools ›</a>', '<a href="index.html">すべてのツール ›</a>'),
    # badges
    ('<span class="free-badge">Free</span>', '<span class="free-badge">無料</span>'),
]

# ── 공통 교체 패턴 (도구 페이지 포함) ─────────────────────────────────────
COMMON_REPLACES = [
    # header nav
    ('<a href="index.html">All Tools ›</a>', '<a href="index.html">すべてのツール ›</a>'),
    # badges
    ('<span class="free-badge">Free</span>', '<span class="free-badge">無料</span>'),
    # Tips/FAQ headers
    ('<h2>Related Tools</h2>', '<h2>関連ツール</h2>'),
    ('<h2>Frequently Asked Questions</h2>', '<h2>よくある質問</h2>'),
    ('<h3>💡 Tips</h3>', '<h3>💡 ヒント</h3>'),
    # common FAQ
    ('<summary>Are my files uploaded to the internet?</summary>', '<summary>ファイルはインターネットにアップロードされますか？</summary>'),
    ('<p>No. All processing happens entirely in your browser. Files are never sent to any server.</p>', '<p>いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。</p>'),
    # wooa-originals texts in JS (not applicable in HTML, but keep for future use)
    # Select File button
    ('>Select File<', '>ファイルを選択<'),
    # breadcrumb
    ('<a href="index.html">WooaViewer</a>', '<a href="index.html">WooaViewer</a>'),
    # about link
    ('>About</a>', '>About</a>'),
]


def build_lang_switcher_ja(fname):
    """lang-switcher를 KO|EN|JA 형식으로 업데이트"""
    stem = fname  # 파일명 그대로
    ko_href = f'../{stem}'
    en_href = f'../en/{stem}'
    ja_href = stem
    return (
        '<div class="lang-switcher">\n'
        f'        <a href="{ko_href}">KO</a>\n'
        '        <span>|</span>\n'
        f'        <a href="{en_href}">EN</a>\n'
        '        <span>|</span>\n'
        f'        <a href="{ja_href}" class="active">JA</a>\n'
        '      </div>'
    )


def convert_en_to_ja(content, fname):
    meta = PAGE_META.get(fname, {})

    # 1. lang="en" → lang="ja"
    content = content.replace('<html lang="en">', '<html lang="ja">')

    # 2. title 교체
    if 'title' in meta:
        content = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', content)

    # 3. description 교체 (meta + og + twitter)
    if 'desc' in meta:
        d = meta['desc']
        content = re.sub(r'(<meta name="description" content=")[^"]*(")', rf'\g<1>{d}\2', content)
        content = re.sub(r'(<meta property="og:description" content=")[^"]*(")', rf'\g<1>{d}\2', content)
        content = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', rf'\g<1>{d}\2', content)

    # 4. keywords 교체
    if 'kw' in meta:
        content = re.sub(r'(<meta name="keywords" content=")[^"]*(")', rf'\g<1>{meta["kw"]}\2', content)

    # 5. og:title, twitter:title 교체 (title과 동일)
    if 'title' in meta:
        t = meta['title']
        content = re.sub(r'(<meta property="og:title" content=")[^"]*(")', rf'\g<1>{t}\2', content)
        content = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', rf'\g<1>{t}\2', content)

    # 6. canonical만 /en/ → /ja/
    content = re.sub(
        r'(<link rel="canonical" href="https://wooaviewer\.wooahouse\.com)/en/([^"]*)"',
        r'\1/ja/\2"', content
    )
    # og:url만 /en/ → /ja/
    content = re.sub(
        r'(<meta property="og:url" content="https://wooaviewer\.wooahouse\.com)/en/([^"]*)"',
        r'\1/ja/\2"', content
    )

    # 7. og:locale: en_US → ja_JP
    content = content.replace(
        '<meta property="og:locale" content="en_US">',
        '<meta property="og:locale" content="ja_JP">'
    )

    # 8. hreflang: ja 추가 (x-default 앞에 삽입)
    # 기존 en hreflang 찾아서 ja 추가
    ja_url = f'https://wooaviewer.wooahouse.com/ja/{fname}'
    ja_hreflang = f'  <link rel="alternate" hreflang="ja" href="{ja_url}">\n'
    # x-default 앞에 삽입
    content = re.sub(
        r'(<link rel="alternate" hreflang="x-default")',
        ja_hreflang + r'\1',
        content
    )
    # x-default URL도 EN으로 유지 (EN이 기본)

    # 9. LD+JSON inLanguage: "en" → "ja"
    content = content.replace('"inLanguage":"en"', '"inLanguage":"ja"')
    content = content.replace('"inLanguage": "en"', '"inLanguage": "ja"')
    # LD+JSON URL /en/ → /ja/
    content = re.sub(
        r'("url":"https://wooaviewer\.wooahouse\.com)/en/',
        r'\1/ja/', content
    )

    # 10. lang-switcher 교체
    # 현재 KO|EN 패턴 찾아서 KO|EN|JA로 교체
    new_switcher = build_lang_switcher_ja(fname)
    content = re.sub(
        r'<div class="lang-switcher">.*?</div>',
        new_switcher,
        content,
        flags=re.DOTALL
    )

    # 11. h1 교체 (도구 페이지)
    if 'h1' in meta:
        content = re.sub(
            r'<h1>[^<]+</h1>',
            f'<h1>{meta["h1"]}</h1>',
            content,
            count=1
        )

    # 12. tool_desc 교체 (tool-header p)
    if 'tool_desc' in meta:
        content = re.sub(
            r'(<div class="tool-header">.*?<h1>[^<]+</h1>\s*<p>)[^<]*(</p>)',
            rf'\g<1>{meta["tool_desc"]}\2',
            content,
            flags=re.DOTALL,
            count=1
        )

    # 13. JS 파일 경로 교체
    content = content.replace(
        'src="../js/wooahouse-originals-en.js"',
        'src="../js/wooahouse-originals-ja.js"'
    )
    content = content.replace(
        'src="../js/wooahouse-originals-tool-en.js"',
        'src="../js/wooahouse-originals-tool-ja.js"'
    )
    content = content.replace(
        'src="../js/wooa-sidebar-en.js"',
        'src="../js/wooa-sidebar-ja.js"'
    )
    content = content.replace(
        'src="../js/wooa-footer-en.js"',
        'src="../js/wooa-footer-ja.js"'
    )

    # 14. index.html 특수 교체
    if fname == 'index.html':
        for old, new in INDEX_REPLACES:
            content = content.replace(old, new)

    # 15. 공통 교체 (모든 파일)
    for old, new in COMMON_REPLACES:
        content = content.replace(old, new)

    return content


def create_ja_js_files():
    """JA용 JS 파일 생성"""
    print('\n── JS 파일 준비 ──────────────────────────────────')

    # 1. shared-js에서 wooa-sidebar-ja.js, wooa-footer-ja.js 복사
    for fname in ['wooa-sidebar-ja.js', 'wooa-footer-ja.js']:
        src = os.path.join(SHARED_JS, fname)
        dst = os.path.join(JS_DIR, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f'  COPY: {fname}')
        else:
            print(f'  MISS (shared-js): {fname}')

    # 2. wooahouse-originals-ja.js 생성 (EN 버전 기반)
    en_orig = os.path.join(JS_DIR, 'wooahouse-originals-en.js')
    ja_orig = os.path.join(JS_DIR, 'wooahouse-originals-ja.js')
    if os.path.exists(en_orig):
        with open(en_orig, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace("'👀 Looking for something else?'", "'👀 他にお探しですか？'")
        content = content.replace("'More free tools from WooaHouse'", "'WooaHouseの他の無料ツール'")
        content = content.replace("'Visit →'", "'見る →'")
        with open(ja_orig, 'w', encoding='utf-8') as f:
            f.write(content)
        print('  CREATE: wooahouse-originals-ja.js')
    else:
        print('  MISS: wooahouse-originals-en.js (원본 없음)')

    # 3. wooahouse-originals-tool-ja.js 생성 (EN 버전 기반)
    en_tool = os.path.join(JS_DIR, 'wooahouse-originals-tool-en.js')
    ja_tool = os.path.join(JS_DIR, 'wooahouse-originals-tool-ja.js')
    if os.path.exists(en_tool):
        with open(en_tool, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace("'🛠️ More tools to try'", "'🛠️ 他のツールを試す'")
        with open(ja_tool, 'w', encoding='utf-8') as f:
            f.write(content)
        print('  CREATE: wooahouse-originals-tool-ja.js')
    else:
        print('  MISS: wooahouse-originals-tool-en.js (원본 없음)')


def build_ja_pages():
    """ja/ 디렉토리에 JA HTML 파일 생성"""
    os.makedirs(JA_DIR, exist_ok=True)
    print('\n── JA HTML 파일 생성 ────────────────────────────')

    en_files = sorted([f for f in os.listdir(EN_DIR) if f.endswith('.html')])
    ok = 0
    miss = 0

    for fname in en_files:
        en_path = os.path.join(EN_DIR, fname)
        ja_path = os.path.join(JA_DIR, fname)

        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        ja_content = convert_en_to_ja(content, fname)

        with open(ja_path, 'w', encoding='utf-8') as f:
            f.write(ja_content)

        if fname in PAGE_META:
            print(f'  OK: {fname}')
            ok += 1
        else:
            print(f'  OK (메타없음): {fname}')
            ok += 1

    print(f'\n완료: {ok}개 생성, {miss}개 실패')


if __name__ == '__main__':
    create_ja_js_files()
    build_ja_pages()
    print('\n✅ JA 빌드 완료. ja/ 디렉토리를 확인하세요.')
