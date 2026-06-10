"""
WooaViewer JA 파일 Tips + FAQ 영어 → 일본어 교체 (2차: 여러 줄 형식 파일)
- gpx-maker, gpx-viewer, hex-viewer, ini-viewer, m3u-viewer, srt-viewer, tar-viewer
- cbz (마지막 FAQ 이미 수정, tips/faq1/2는 이전 스크립트에서 처리 못함)
"""
import os, re

JA_DIR = 'C:/개인/wooahouse/WooaViewer/ja'

# 각 파일의 영어 tips li 3개 → 일본어
TIPS_MAP = {
    'gpx-maker.html': {
        'tips_old': [
            'Plan hiking, cycling, or running routes by clicking on the map, then export as GPX to import directly into Garmin devices, Strava, AllTrails, or Komoot.',
            'Load an existing GPX file to make it editable — add or remove track points and waypoints, then save the updated route.',
            'Click a waypoint marker to open its popup, then press the <strong>Delete</strong> button to remove it. Click a blue track dot to remove that track point.',
        ],
        'tips_new': [
            '地図上をクリックしてハイキング・サイクリング・ランニングルートを計画し、GPXとしてエクスポートしてGarmin・Strava・AllTrails・Komootに取り込めます。',
            '既存のGPXファイルを読み込んで編集可能にし、トラックポイントやウェイポイントを追加・削除してルートを更新できます。',
            'ウェイポイントマーカーをクリックするとポップアップが開き、<strong>削除</strong>ボタンで削除できます。青いトラックドットをクリックするとトラックポイントを削除できます。',
        ],
        'faq_old': [
            ('Where can I use the GPX file I create?',
             'Almost any GPS device or app supports GPX — including Garmin devices, Strava, Komoot, AllTrails, OsmAnd, and Google Maps (via import). Use each app\'s "Import route" or "Import GPX" feature.'),
            ('Can I add elevation data to my route?',
             'Track points added by clicking the map do not include elevation. If you need elevation data, export the GPX and then use a tool like GPSBabel or GPS Visualizer to add elevation from a DEM dataset.'),
            ('Is my data uploaded to a server?',
             'No. All processing happens entirely in your browser. Your route data is never sent to any server. Only map tile images are fetched from OpenStreetMap to render the map.'),
        ],
        'faq_new': [
            ('作成したGPXファイルはどこで使えますか？',
             'GPXはGarminデバイス・Strava・Komoot・AllTrails・OsmAnd・Google Maps（インポート経由）など、ほぼすべてのGPSデバイスやアプリで対応しています。各アプリの「ルートのインポート」または「GPXのインポート」機能をご使用ください。'),
            ('ルートに標高データを追加できますか？',
             '地図上をクリックして追加したトラックポイントには標高が含まれていません。標高データが必要な場合はGPXをエクスポートし、GPSBabelやGPS VisualizerなどのツールでDEMデータセットから標高を追加してください。'),
            ('データはサーバーにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ルートデータは一切サーバーに送信されません。地図のレンダリングに必要なOpenStreetMapのマップタイル画像のみ取得されます。'),
        ],
    },
    'gpx-viewer.html': {
        'tips_old': [
            'GPX files can be exported from most GPS devices and apps — Garmin, Strava, AllTrails, and Komoot all support GPX export.',
            'The map uses OpenStreetMap. An internet connection is required for map tiles, but your GPX data is never sent to a server.',
            'Waypoints (<code>&lt;wpt&gt;</code>) in the GPX file are shown as markers on the map with their name as a popup.',
        ],
        'tips_new': [
            'GPXファイルはほとんどのGPSデバイスやアプリからエクスポートできます。Garmin・Strava・AllTrails・KomootすべてがGPXエクスポートに対応しています。',
            '地図はOpenStreetMapを使用しています。マップタイルにはインターネット接続が必要ですが、GPXデータはサーバーに送信されません。',
            'GPXファイル内のウェイポイント（<code>&lt;wpt&gt;</code>）は地図上にマーカーとして表示され、名前がポップアップで確認できます。',
        ],
        'faq_old': [
            ('What is a GPX file?',
             'GPX (GPS Exchange Format) is an XML-based file format for GPS data. It stores tracks (routes), waypoints (named locations), and routes. It is widely used for hiking, cycling, running, and other outdoor activity recording.'),
            ('Does this viewer support KML files?',
             'Currently only GPX is supported. For KML files, convert them to GPX using a tool like GPSBabel or GPS Visualizer, then upload here.'),
            ('Is my file uploaded to a server?',
             'No. The GPX data is processed entirely in your browser. Only map tile images are fetched from OpenStreetMap servers to render the map.'),
        ],
        'faq_new': [
            ('GPXファイルとは何ですか？',
             'GPX（GPS Exchange Format）はGPSデータ用のXMLベースのファイル形式です。トラック（ルート）・ウェイポイント（名前付き地点）・ルートを保存します。ハイキング・サイクリング・ランニングなどのアウトドアアクティビティの記録に広く使われています。'),
            ('KMLファイルにも対応していますか？',
             '現在はGPXのみ対応しています。KMLファイルの場合はGPSBabelやGPS Visualizerなどのツールを使ってGPXに変換してからアップロードしてください。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。GPXデータはブラウザ内のみで処理されます。地図のレンダリングに必要なOpenStreetMapのマップタイル画像のみ取得されます。'),
        ],
    },
    'hex-viewer.html': {
        'tips_old': [
            'The first few bytes of a file are its <strong>file signature (magic number)</strong>. E.g. PDF starts with <code>25 50 44 46</code>, ZIP with <code>50 4B 03 04</code>.',
            'Only the first 8,192 bytes (8 KB) are shown — sufficient for analysing file headers and structure.',
            'Dots (.) in the ASCII column represent non-printable characters. Readable text sections will appear as plain text.',
        ],
        'tips_new': [
            'ファイルの最初の数バイトは<strong>ファイルシグネチャ（マジックナンバー）</strong>です。例：PDFは<code>25 50 44 46</code>、ZIPは<code>50 4B 03 04</code>で始まります。',
            '最初の8,192バイト（8 KB）のみ表示されます。ファイルヘッダーと構造の分析には十分な量です。',
            'ASCII列のドット（.）は非印刷文字を表します。読めるテキスト部分はプレーンテキストとして表示されます。',
        ],
        'faq_old': [
            ('What is a HEX viewer used for?',
             'Hex viewers are used for file format analysis, identifying file signatures, debugging binary data, and diagnosing corrupted files. They are commonly used by developers and security researchers.'),
            ('Why is only the first 8 KB shown?',
             'Displaying entire large files would slow down the browser. The header region (first few KB) contains the most structurally important information, so 8 KB is a practical limit for analysis.'),
            ('Is my file uploaded to a server?',
             'No. All processing happens entirely in your browser. Your file is never sent to any server — it is completely private and safe.'),
        ],
        'faq_new': [
            ('HEXビューアは何に使いますか？',
             'HEXビューアはファイル形式の分析・ファイルシグネチャの確認・バイナリデータのデバッグ・破損ファイルの診断に使用されます。開発者やセキュリティ研究者が一般的に使用します。'),
            ('なぜ最初の8 KBしか表示されないのですか？',
             '大きなファイル全体を表示するとブラウザが遅くなります。ヘッダー領域（最初の数KB）に最も重要な構造情報が含まれているため、8 KBは分析の実用的な上限です。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。'),
        ],
    },
    'ini-viewer.html': {
        'tips_old': [
            'Comments starting with <code>;</code> or <code>#</code> are skipped — only active configuration entries are displayed.',
            'Key-value pairs at the top of the file with no section header are shown under <strong>(global)</strong>.',
            'UTF-8, UTF-16, and most single-byte encodings are handled. If text looks garbled, re-save the file as UTF-8.',
        ],
        'tips_new': [
            '<code>;</code>または<code>#</code>で始まるコメント行はスキップされ、有効な設定エントリのみ表示されます。',
            'セクションヘッダーのないファイル先頭のキーと値のペアは<strong>（global）</strong>として表示されます。',
            'UTF-8、UTF-16、ほとんどのシングルバイトエンコーディングに対応しています。文字化けする場合はUTF-8で保存し直してください。',
        ],
        'faq_old': [
            ('What is the INI file format?',
             'INI is a simple text-based configuration format. Groups are defined by <code>[section]</code> headers, and settings are stored as <code>key=value</code> pairs. It predates the Windows Registry and remains widely used in applications across all platforms.'),
            ('Does this viewer support .cfg, .conf, and .properties files?',
             'Yes — any file using the same key=value structure is supported regardless of extension. The parser detects the format from file content, not the filename.'),
            ('Is my file uploaded to a server?',
             'No. All processing happens entirely in your browser. Your file is never sent to any server — it is completely private and safe.'),
        ],
        'faq_new': [
            ('INIファイル形式とは何ですか？',
             'INIはシンプルなテキストベースの設定形式です。グループは<code>[セクション]</code>ヘッダーで定義され、設定は<code>キー=値</code>のペアとして保存されます。Windowsレジストリより以前から存在し、あらゆるプラットフォームのアプリケーションで広く使われています。'),
            ('.cfg、.conf、.propertiesファイルにも対応していますか？',
             'はい。拡張子に関わらず、同じキー=値の構造を使用するファイルであればすべて対応しています。パーサーはファイル名ではなくファイルの内容から形式を検出します。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。'),
        ],
    },
    'm3u-viewer.html': {
        'tips_old': [
            'Extended M3U format uses an <code>#EXTM3U</code> header and <code>#EXTINF:duration,title</code> tags before each URL.',
            'M3U8 is identical to M3U but explicitly specifies UTF-8 encoding. It is also used for Apple HLS streaming segments.',
            'IPTV playlist files are almost always in M3U format and can be opened with this viewer.',
        ],
        'tips_new': [
            '拡張M3U形式は<code>#EXTM3U</code>ヘッダーと各URLの前にある<code>#EXTINF:時間,タイトル</code>タグを使用します。',
            'M3U8はM3Uと同じ形式ですが明示的にUTF-8エンコーディングを指定し、Apple HLSストリーミングにも使用されます。',
            'IPTVプレイリストファイルはほぼ常にM3U形式で、このビューアで開けます。',
        ],
        'faq_old': [
            ('What is the difference between M3U and M3U8?',
             'M3U is a simple text playlist format. M3U8 is the same format but explicitly encoded in UTF-8, and is also used by Apple\'s HTTP Live Streaming (HLS) protocol for adaptive bitrate streaming.'),
            ('Why does some duration show as -1 or empty?',
             'A duration of -1 indicates a live stream or a track with no duration metadata. This viewer displays those as a dash (-).'),
            ('Is my file uploaded to a server?',
             'No. All processing happens entirely in your browser. Your file is never sent to any server — it is completely private and safe.'),
        ],
        'faq_new': [
            ('M3UとM3U8の違いは何ですか？',
             'M3Uはシンプルなテキストプレイリスト形式です。M3U8は同じ形式ですが明示的にUTF-8でエンコードされており、AppleのアダプティブビットレートストリーミングプロトコルであるHLSにも使用されます。'),
            ('再生時間が-1や空白で表示されるのはなぜですか？',
             '-1の再生時間はライブストリームまたは再生時間メタデータのないトラックを示します。このビューアではダッシュ（-）として表示されます。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。'),
        ],
    },
    'srt-viewer.html': {
        'tips_old': [
            'SRT subtitles follow: sequence number → timecode → text, separated by blank lines.',
            'VTT files must start with <strong>WEBVTT</strong> on the first line. They are used by YouTube and the HTML5 &lt;track&gt; element.',
            'If text looks garbled, the file is likely encoded in a non-UTF-8 charset. Re-save as UTF-8 in a text editor and re-upload.',
        ],
        'tips_new': [
            'SRT字幕の形式：シーケンス番号 → タイムコード → テキスト、空行で区切られています。',
            'VTTファイルは最初の行に<strong>WEBVTT</strong>が必要です。YouTubeやHTML5の&lt;track&gt;要素で使用されます。',
            'テキストが文字化けする場合はUTF-8以外のエンコーディングの可能性があります。テキストエディターでUTF-8として保存し直してください。',
        ],
        'faq_old': [
            ('What is the difference between SRT and VTT?',
             'SRT (SubRip Text) is the most widely-used subtitle format for movies and TV. VTT (WebVTT) is designed for web browsers and supports style tags and CSS positioning for HTML5 video and YouTube.'),
            ('The subtitle text looks garbled — how do I fix it?',
             'The file is likely encoded in Windows-1252 or EUC-KR. Open it in VSCode, change the encoding to UTF-8, save, and re-upload.'),
            ('Is my file uploaded to a server?',
             'No. All processing happens entirely in your browser. Your file is never sent to any server — it is completely private and safe.'),
        ],
        'faq_new': [
            ('SRTとVTTの違いは何ですか？',
             'SRT（SubRip Text）は映画やTVで最も広く使われる字幕形式です。VTT（WebVTT）はウェブブラウザ向けに設計されており、HTML5ビデオとYouTubeのスタイルタグとCSSポジショニングをサポートしています。'),
            ('字幕テキストが文字化けしています。どうすれば直りますか？',
             'ファイルがWindows-1252またはEUC-KRでエンコードされている可能性があります。VSCodeで開き、エンコーディングをUTF-8に変更して保存し、再アップロードしてください。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。'),
        ],
    },
    'tar-viewer.html': {
        'tips_old': [
            '.tar.gz and .tgz are the same format — a TAR archive compressed with GZIP. Both are handled automatically.',
            'File size limit is 100 MB. For larger archives, use a desktop tool like 7-Zip or tar CLI to inspect the contents.',
            'This viewer shows the file listing only — actual extraction is not supported. Use 7-Zip or a similar tool to extract files.',
        ],
        'tips_new': [
            '.tar.gzと.tgzは同じ形式です。GZIPで圧縮されたTARアーカイブで、どちらも自動的に処理されます。',
            'ファイルサイズの上限は100MBです。より大きなアーカイブには7-ZipやtarコマンドなどのデスクトップツールをCLIで使用してください。',
            'このビューアはファイル一覧のみ表示します。実際の解凍はできません。ファイルを解凍するには7-Zipなどのツールをご使用ください。',
        ],
        'faq_old': [
            ('What is the difference between TAR and ZIP?',
             'TAR bundles files into a single archive without compression. It is typically paired with GZIP (.tar.gz) or BZIP2 (.tar.bz2) for compression. ZIP combines archiving and compression in a single step and is more common on Windows.'),
            ('Can I open plain .gz files?',
             'A plain .gz file is a single compressed file with no TAR structure inside. This viewer requires a TAR structure (.tar, .tar.gz, .tgz). To decompress a plain .gz file, use the gunzip command or 7-Zip.'),
            ('Is my file uploaded to a server?',
             'No. All processing happens entirely in your browser. Your file is never sent to any server — it is completely private and safe.'),
        ],
        'faq_new': [
            ('TARとZIPの違いは何ですか？',
             'TARはファイルを圧縮なしで1つのアーカイブにまとめます。通常GZIP（.tar.gz）またはBZIP2（.tar.bz2）と組み合わせて圧縮します。ZIPはアーカイブ化と圧縮を1ステップで行い、Windows上でより一般的です。'),
            ('通常の.gzファイルを開けますか？',
             '.gzファイルはTAR構造のない単一の圧縮ファイルです。このビューアはTAR構造（.tar、.tar.gz、.tgz）が必要です。通常の.gzファイルを解凍するにはgunzipコマンドまたは7-Zipをご使用ください。'),
            ('ファイルはインターネットにアップロードされますか？',
             'いいえ。すべての処理はブラウザ内のみで行われます。ファイルは一切サーバーに送信されません。'),
        ],
    },
}

ok = 0
err = 0

for fname, d in TIPS_MAP.items():
    fpath = os.path.join(JA_DIR, fname)
    if not os.path.exists(fpath):
        print(f'  MISSING: {fname}')
        err += 1
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # ── Tips 교체 (li 단위) ─────────────────────────────────────
    for old_li, new_li in zip(d['tips_old'], d['tips_new']):
        content = content.replace(f'<li>{old_li}</li>', f'<li>{new_li}</li>', 1)

    # ── FAQ 교체 (summary + p 단위) ─────────────────────────────
    for (old_q, old_a), (new_q, new_a) in zip(d['faq_old'], d['faq_new']):
        old_block = f'<summary>{old_q}</summary><p>{old_a}</p>'
        new_block = f'<summary>{new_q}</summary><p>{new_a}</p>'
        content = content.replace(old_block, new_block, 1)

    if content == original:
        print(f'  WARN (변경없음): {fname}')
        err += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {fname}')
    ok += 1

print(f'\n완료: {ok}개 업데이트, {err}개 경고/오류')
