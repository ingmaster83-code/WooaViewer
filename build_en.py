"""
WooaViewer 영어 버전 자동 생성 스크립트
실행: python build_en.py
결과: en/ 폴더에 영어 버전 HTML 파일 생성
"""

import os, re, sys, io, json as _json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE, 'en')
os.makedirs(EN_DIR, exist_ok=True)

# ── 1. 페이지별 메타 번역 ─────────────────────────────────────────────────────
PAGE_META = {
    'index.html': {
        'title': 'Free Online File Viewer – Open DOCX XLSX DXF PSD HEIC CSV ZIP SVG Without Installing | WooaViewer',
        'desc':  'Open Word, Excel, CAD, Photoshop, iPhone photos, CSV, ZIP, SVG and font files for free in your browser — no installation needed. 15+ file formats, files never sent to a server.',
        'kw':    'file viewer, DOCX viewer, XLSX viewer, DXF viewer, PSD viewer, STL viewer, HEIC viewer, GCode viewer, XML viewer, Markdown viewer, JSON viewer, CSV viewer, ZIP viewer, SVG viewer, font viewer, free file viewer, online file viewer, WooaViewer',
        'og_title': 'Free Online File Viewer – Open DOCX XLSX DXF PSD HEIC CSV ZIP SVG | WooaViewer',
        'og_desc':  'Open Word, Excel, CAD, Photoshop, iPhone photos, CSV, ZIP, SVG and more — all free in your browser. No installation, no server upload.',
        'app_name': 'WooaViewer',
        'faq': [
            ('Are all the file viewers really free?',
             'Yes. All WooaViewer tools are completely free with no signup required and no usage limits.'),
            ('Are my files uploaded to a server?',
             'No. All file processing happens locally in your browser. Your files never leave your device.'),
            ('Which file formats are supported?',
             'DOCX, XLSX, DXF, PSD, STL, Markdown, JSON, EPUB, HEIC, GCode, XML, CSV, ZIP, SVG, and font files (TTF/OTF/WOFF) are all supported.'),
        ],
        'h1': 'Open Any File — No Installation Needed',
        'tool_desc': 'Open Word, Excel, CAD, Photoshop files 100% free. No signup, files never stored on a server.',
        'breadcrumb': 'Home',
        'cross_banner_text': 'Need to work with PDF files too?',
        'cross_banner_link_text': '📄 WooaPDF – Free PDF Tools →',
        'cross_banner_href': 'https://pdfkit.wooahouse.com/',
    },
    'csv-viewer.html': {
        'title': 'CSV Viewer Free Online – Open CSV File as Table, Sort & Search | WooaViewer',
        'desc':  'Upload or paste a CSV file to view it as a clean, sortable table. Supports column sorting, real-time search, and comma/tab/semicolon delimiter selection. Free, no server upload.',
        'kw':    'CSV viewer, open CSV file, CSV table viewer, online CSV viewer, free CSV viewer, CSV sort, CSV search, CSV data viewer, TSV viewer, CSV parser, data file viewer',
        'og_title': 'CSV Viewer Free Online – Table View, Sort & Search | WooaViewer',
        'og_desc':  'View CSV files as a table with column sorting and real-time search. Free, no server upload.',
        'app_name': 'CSV Viewer',
        'faq': [
            ('What delimiters are supported?',
             'Comma (,), tab (\\t), and semicolon (;) delimiters are all supported.'),
            ('Can I search within the CSV data?',
             'Yes. Use the real-time search box to filter rows instantly as you type.'),
            ('Is my CSV file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'CSV Viewer – Free Online',
        'tool_desc': 'Upload or paste a CSV file to display it as a sortable, searchable table. Choose your delimiter. Everything runs in your browser.',
        'breadcrumb': 'CSV Viewer',
        'cross_banner_text': 'Need to view Excel or JSON data too?',
        'cross_banner_link_text': '📊 XLSX Viewer →',
        'cross_banner_href': '../xlsx-viewer.html',
    },
    'docx-viewer.html': {
        'title': 'DOCX Viewer Free Online – Open Word Documents Without Microsoft Word | WooaViewer',
        'desc':  'Open .docx Word files for free in your browser without Microsoft Word. Text, tables, and images are rendered. Files are never sent to a server — 100% private.',
        'kw':    'DOCX viewer, Word viewer, open docx, open Word file, free DOCX viewer, online Word viewer, Word file viewer, open Word without Word, docx online viewer, document viewer',
        'og_title': 'DOCX Viewer Free Online – Open Word Without Microsoft Word | WooaViewer',
        'og_desc':  'Open .docx Word files in your browser for free. No Word needed. Files never sent to a server.',
        'app_name': 'DOCX Viewer',
        'faq': [
            ('Do I need Microsoft Word installed?',
             'No. You can open .docx files directly in your browser without any software installed.'),
            ('Are tables and images supported?',
             'Yes. Text, tables, and embedded images are all rendered in the viewer.'),
            ('Is my file uploaded to a server?',
             'No. All processing is done locally in your browser. Your document is never sent anywhere.'),
        ],
        'h1': 'DOCX Viewer – Open Word Files Free Online',
        'tool_desc': 'Upload a .docx file to open and read it without Microsoft Word. Text, tables, and images are displayed. All processing happens in your browser.',
        'breadcrumb': 'DOCX Viewer',
        'cross_banner_text': 'Need to view Excel spreadsheets too?',
        'cross_banner_link_text': '📊 XLSX Viewer →',
        'cross_banner_href': '../xlsx-viewer.html',
    },
    'dxf-viewer.html': {
        'title': 'DXF Viewer Free Online – Open CAD Drawing Files Without AutoCAD | WooaViewer',
        'desc':  'Open .dxf CAD drawing files for free in your browser without AutoCAD. Supports zoom and pan for drawing navigation. Files never sent to a server — 100% private.',
        'kw':    'DXF viewer, CAD viewer, drawing viewer, open DXF, AutoCAD viewer, free CAD viewer, online DXF viewer, CAD drawing viewer, DXF online viewer, free drawing viewer',
        'og_title': 'DXF Viewer Free Online – Open CAD Drawings Without AutoCAD | WooaViewer',
        'og_desc':  'Open .dxf CAD drawing files in your browser for free. Zoom and pan supported. Files never sent to a server.',
        'app_name': 'DXF Viewer',
        'faq': [
            ('Do I need AutoCAD installed?',
             'No. You can open .dxf CAD files directly in your browser without any CAD software.'),
            ('Can I zoom and pan the drawing?',
             'Yes. Use the mouse wheel to zoom and drag to pan around the drawing.'),
            ('Is my file uploaded to a server?',
             'No. All rendering happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'DXF Viewer – Open CAD Drawings Free Online',
        'tool_desc': 'Upload a .dxf file to view CAD drawings without AutoCAD. Zoom and pan to explore the drawing. All processing happens in your browser.',
        'breadcrumb': 'DXF Viewer',
        'cross_banner_text': 'Need to view 3D model files too?',
        'cross_banner_link_text': '🖨️ STL Viewer →',
        'cross_banner_href': '../stl-viewer.html',
    },
    'epub-viewer.html': {
        'title': 'EPUB Viewer Free Online – Read eBook Files in Browser, Table of Contents & Pages | WooaViewer',
        'desc':  'Read .epub eBook files for free in your browser without any app. Supports page turning, table of contents navigation, and chapter jumping. Files never sent to a server.',
        'kw':    'EPUB viewer, eBook viewer, open EPUB, online EPUB viewer, free eBook viewer, ebook reader, EPUB reader, read epub online, EPUB preview, free epub reader',
        'og_title': 'EPUB Viewer Free Online – Read eBooks in Browser | WooaViewer',
        'og_desc':  'Read .epub eBook files in your browser for free. Table of contents, page turning supported. Files never sent to a server.',
        'app_name': 'EPUB Viewer',
        'faq': [
            ('Do I need an eBook reader app installed?',
             'No. You can read .epub files directly in your browser without any additional app.'),
            ('Can I navigate by table of contents?',
             'Yes. The table of contents is displayed and you can jump to any chapter directly.'),
            ('Is my eBook file uploaded to a server?',
             'No. All processing is done locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'EPUB Viewer – Read eBooks Free Online',
        'tool_desc': 'Upload an .epub file to read it in your browser. Navigate chapters via table of contents and turn pages. All processing runs in your browser.',
        'breadcrumb': 'EPUB Viewer',
        'cross_banner_text': 'Need to view Word documents too?',
        'cross_banner_link_text': '📝 DOCX Viewer →',
        'cross_banner_href': '../docx-viewer.html',
    },
    'font-viewer.html': {
        'title': 'Font Viewer Free Online – Preview TTF OTF WOFF Font Files, Size & Weight | WooaViewer',
        'desc':  'Upload TTF, OTF, WOFF, or WOFF2 font files to instantly preview them. Adjust font size, weight, and italic style. Check Latin, Hangul, and numeric character sets. Free, no server upload.',
        'kw':    'font viewer, TTF viewer, OTF viewer, WOFF viewer, font preview, online font viewer, free font viewer, open font file, WOFF2 viewer, font checker, font preview tool',
        'og_title': 'Font Viewer Free Online – Preview TTF OTF WOFF Font Files | WooaViewer',
        'og_desc':  'Upload font files to preview them. Adjust size, weight, and italic. Free, no server upload.',
        'app_name': 'Font Viewer',
        'faq': [
            ('Which font formats are supported?',
             'TTF, OTF, WOFF, and WOFF2 font files are all supported.'),
            ('Can I adjust the preview size and style?',
             'Yes. You can adjust font size, weight (bold), italic, and preview different character sets.'),
            ('Is my font file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'Font Viewer – Preview Font Files Free Online',
        'tool_desc': 'Upload a TTF, OTF, or WOFF font file to preview it instantly. Adjust size, weight, and italic. Check character sets. All runs in your browser.',
        'breadcrumb': 'Font Viewer',
        'cross_banner_text': 'Need to view SVG or image files?',
        'cross_banner_link_text': '🔷 SVG Viewer →',
        'cross_banner_href': '../svg-viewer.html',
    },
    'gcode-viewer.html': {
        'title': 'GCode Viewer Free Online – Visualize 3D Printer Slicer Toolpath Layer by Layer | WooaViewer',
        'desc':  'Visualize .gcode 3D printer slicer file toolpaths layer by layer in your browser for free. Supports Cura and PrusaSlicer GCode. Files never sent to a server.',
        'kw':    'GCode viewer, gcode open, 3D printer viewer, slicer viewer, free GCode viewer, online GCode viewer, toolpath viewer, 3D printer file viewer, gcode visualizer, gcode layer viewer, Cura gcode viewer',
        'og_title': 'GCode Viewer Free Online – 3D Printer Toolpath Visualization | WooaViewer',
        'og_desc':  'Visualize .gcode toolpaths layer by layer in your browser. Free, no server upload.',
        'app_name': 'GCode Viewer',
        'faq': [
            ('Which slicer GCode formats are supported?',
             'GCode files from Cura, PrusaSlicer, and most standard 3D printer slicers are supported.'),
            ('Can I view individual layers?',
             'Yes. You can step through layers individually to inspect the toolpath at each level.'),
            ('Is my GCode file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'GCode Viewer – Visualize 3D Printer Files Free Online',
        'tool_desc': 'Upload a .gcode file to visualize the toolpath layer by layer. Inspect your 3D print before printing. All processing runs in your browser.',
        'breadcrumb': 'GCode Viewer',
        'cross_banner_text': 'Need to view 3D STL model files?',
        'cross_banner_link_text': '🖨️ STL Viewer →',
        'cross_banner_href': '../stl-viewer.html',
    },
    'heic-viewer.html': {
        'title': 'HEIC Viewer Free Online – Open iPhone Photos Without Codec, Save as PNG JPG | WooaViewer',
        'desc':  'Open iPhone .heic and .heif photos in your browser for free without any codec installation. Convert and save as PNG or JPG. Files never sent to a server — 100% private.',
        'kw':    'HEIC viewer, open HEIC, iPhone photo viewer, HEIF viewer, free HEIC viewer, online HEIC viewer, HEIC converter, open iPhone photos on PC, HEIC to PNG, HEIC to JPG, iPhone photo viewer',
        'og_title': 'HEIC Viewer Free Online – Open iPhone Photos, Save as PNG JPG | WooaViewer',
        'og_desc':  'Open iPhone .heic photos without codec. Save as PNG or JPG. Free, no server upload.',
        'app_name': 'HEIC Viewer',
        'faq': [
            ('Do I need to install a codec to view HEIC files?',
             'No. You can open .heic and .heif files directly in your browser without any codec or plugin.'),
            ('Can I save HEIC photos as JPG or PNG?',
             'Yes. After opening, you can download the image as a PNG or JPG file.'),
            ('Is my photo uploaded to a server?',
             'No. All processing is done locally in your browser. Your photo is never sent anywhere.'),
        ],
        'h1': 'HEIC Viewer – Open iPhone Photos Free Online',
        'tool_desc': 'Upload an iPhone .heic or .heif photo to view it without a codec. Download as PNG or JPG. All processing happens in your browser.',
        'breadcrumb': 'HEIC Viewer',
        'cross_banner_text': 'Need to compress or edit the saved images?',
        'cross_banner_link_text': '🖼️ WooaImage – Image Tools →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
    'json-viewer.html': {
        'title': 'JSON Viewer Free Online – View JSON in Tree Structure, Collapse & Search | WooaViewer',
        'desc':  'Upload or paste a JSON file to view it in an interactive tree structure. Collapse/expand keys, real-time search, and syntax error detection. Free, no server upload.',
        'kw':    'JSON viewer, open JSON file, JSON tree viewer, JSON formatter, online JSON viewer, free JSON viewer, JSON search, JSON parser, JSON visualizer, JSON explorer',
        'og_title': 'JSON Viewer Free Online – Tree View, Collapse & Search | WooaViewer',
        'og_desc':  'View JSON files in tree structure. Collapse/expand nodes, real-time search, syntax error detection. Free, no server upload.',
        'app_name': 'JSON Viewer',
        'faq': [
            ('Can I search within the JSON data?',
             'Yes. Use the real-time search to filter keys and values instantly.'),
            ('Can I collapse and expand nodes?',
             'Yes. Click any node to collapse or expand it for easier navigation.'),
            ('Is my JSON file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'JSON Viewer – Free Online Tree View',
        'tool_desc': 'Upload or paste JSON to display it in an interactive tree. Collapse/expand nodes and search through the data. Everything runs in your browser.',
        'breadcrumb': 'JSON Viewer',
        'cross_banner_text': 'Need to view XML or CSV files too?',
        'cross_banner_link_text': '📄 XML Viewer →',
        'cross_banner_href': '../xml-viewer.html',
    },
    'markdown-viewer.html': {
        'title': 'Markdown Viewer Free Online – Render & Preview .md Files | WooaViewer',
        'desc':  'Upload or paste a Markdown (.md) file to render it as HTML instantly. README.md preview and code block syntax highlighting supported. Files never sent to a server.',
        'kw':    'Markdown viewer, Markdown renderer, md file open, README viewer, Markdown render, free Markdown viewer, md renderer, Markdown preview, online Markdown viewer, Markdown to HTML',
        'og_title': 'Markdown Viewer Free Online – Render & Preview .md Files | WooaViewer',
        'og_desc':  'Upload or paste Markdown to render it instantly. README preview, code highlighting. Free, no server upload.',
        'app_name': 'Markdown Viewer',
        'faq': [
            ('What Markdown syntax is supported?',
             'CommonMark-compatible Markdown is supported, including headings, lists, tables, code blocks, and links.'),
            ('Can I preview README.md files?',
             'Yes. Just upload your README.md file and it will be rendered exactly as it appears on GitHub.'),
            ('Is my file uploaded to a server?',
             'No. All rendering happens locally in your browser using marked.js. Your file is never sent anywhere.'),
        ],
        'h1': 'Markdown Viewer – Render .md Files Free Online',
        'tool_desc': 'Upload or paste Markdown text to render it as formatted HTML. Supports headings, tables, code blocks, and more. All runs in your browser.',
        'breadcrumb': 'Markdown Viewer',
        'cross_banner_text': 'Need to view JSON or XML data files?',
        'cross_banner_link_text': '🗂️ JSON Viewer →',
        'cross_banner_href': '../json-viewer.html',
    },
    'psd-viewer.html': {
        'title': 'PSD Viewer Free Online – Open Photoshop Files Without Photoshop, Layer List | WooaViewer',
        'desc':  'Preview .psd Photoshop files for free in your browser without Adobe Photoshop. View layer list and composite image preview. Files never sent to a server — 100% private.',
        'kw':    'PSD viewer, Photoshop viewer, open PSD, Photoshop file viewer, free PSD viewer, online PSD viewer, open Photoshop without Photoshop, PSD preview, psd online viewer, layer viewer',
        'og_title': 'PSD Viewer Free Online – Open Photoshop Files Without Photoshop | WooaViewer',
        'og_desc':  'Preview .psd files in your browser for free. View layer list. Files never sent to a server.',
        'app_name': 'PSD Viewer',
        'faq': [
            ('Do I need Adobe Photoshop installed?',
             'No. You can open and preview .psd files directly in your browser without any software installed.'),
            ('Can I see the layer list?',
             'Yes. The layer names and composite preview image are both displayed.'),
            ('Is my PSD file uploaded to a server?',
             'No. All processing is done locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'PSD Viewer – Open Photoshop Files Free Online',
        'tool_desc': 'Upload a .psd file to preview it without Photoshop. View the layer list and composite image. All processing happens in your browser.',
        'breadcrumb': 'PSD Viewer',
        'cross_banner_text': 'Need to compress or convert the preview image?',
        'cross_banner_link_text': '🖼️ WooaImage – Image Tools →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
    'stl-viewer.html': {
        'title': 'STL Viewer Free Online – View 3D Printing Model Files, Rotate & Zoom | WooaViewer',
        'desc':  'View .stl 3D printing model files for free in your browser. Rotate, zoom, and inspect your model with 360° 3D view. Files never sent to a server — 100% private.',
        'kw':    'STL viewer, 3D viewer, open STL, 3D printing viewer, free STL viewer, online 3D viewer, 3D model viewer, STL file viewer, stl online viewer, 3D printer file viewer',
        'og_title': 'STL Viewer Free Online – View 3D Printing Model Files | WooaViewer',
        'og_desc':  'View .stl 3D files in your browser. Rotate and zoom with 360° view. Free, no server upload.',
        'app_name': 'STL Viewer',
        'faq': [
            ('Can I rotate and zoom the 3D model?',
             'Yes. Use mouse drag to rotate and scroll wheel to zoom in/out for a full 360° view.'),
            ('What STL formats are supported?',
             'Both ASCII and binary STL files are supported.'),
            ('Is my STL file uploaded to a server?',
             'No. All 3D rendering happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'STL Viewer – View 3D Models Free Online',
        'tool_desc': 'Upload a .stl file to view your 3D model. Rotate and zoom for a 360° view. Mouse controls for easy navigation. All runs in your browser.',
        'breadcrumb': 'STL Viewer',
        'cross_banner_text': 'Need to view GCode toolpath files?',
        'cross_banner_link_text': '⚙️ GCode Viewer →',
        'cross_banner_href': '../gcode-viewer.html',
    },
    'svg-viewer.html': {
        'title': 'SVG Viewer Free Online – Preview SVG Files, View Source & Convert to PNG | WooaViewer',
        'desc':  'Upload or paste SVG code to preview it instantly. Supports zoom/pan, PNG conversion download, and SVG source code viewing. Perfect for icons and vector images. Free, no server upload.',
        'kw':    'SVG viewer, open SVG file, SVG preview, SVG to PNG, online SVG viewer, free SVG viewer, SVG source viewer, SVG renderer, SVG icon viewer, SVG vector viewer',
        'og_title': 'SVG Viewer Free Online – Preview SVG, View Source & Convert to PNG | WooaViewer',
        'og_desc':  'Preview SVG files, view source code, convert to PNG and download. Zoom/pan supported. Free, no server upload.',
        'app_name': 'SVG Viewer',
        'faq': [
            ('Can I convert SVG to PNG?',
             'Yes. After loading an SVG file, you can download it as a PNG image with one click.'),
            ('Can I view the SVG source code?',
             'Yes. The raw SVG source code is displayed so you can inspect or copy it.'),
            ('Is my SVG file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'SVG Viewer – Preview & Convert SVG Free Online',
        'tool_desc': 'Upload or paste an SVG file to preview it. Zoom and pan, view source code, and download as PNG. Everything runs in your browser.',
        'breadcrumb': 'SVG Viewer',
        'cross_banner_text': 'Need to compress or edit images?',
        'cross_banner_link_text': '🖼️ WooaImage – Image Tools →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
    'xlsx-viewer.html': {
        'title': 'XLSX Viewer Free Online – Open Excel Spreadsheets Without Microsoft Excel | WooaViewer',
        'desc':  'Open .xlsx, .xls spreadsheet files for free in your browser without Microsoft Excel. Multiple sheet tabs and cell data viewing supported. Files never sent to a server.',
        'kw':    'XLSX viewer, Excel viewer, spreadsheet viewer, open XLSX, XLS viewer, free Excel viewer, online Excel viewer, open Excel without Excel, xlsx online viewer, Excel file viewer',
        'og_title': 'XLSX Viewer Free Online – Open Excel Without Microsoft Excel | WooaViewer',
        'og_desc':  'Open .xlsx, .xls spreadsheets in your browser for free. Multiple sheets supported. Files never sent to a server.',
        'app_name': 'XLSX Viewer',
        'faq': [
            ('Do I need Microsoft Excel installed?',
             'No. You can open .xlsx and .xls files directly in your browser without any software.'),
            ('Are multiple sheets supported?',
             'Yes. All sheets are shown as tabs and you can switch between them.'),
            ('Is my file uploaded to a server?',
             'No. All processing is done locally in your browser. Your spreadsheet is never sent anywhere.'),
        ],
        'h1': 'XLSX Viewer – Open Excel Files Free Online',
        'tool_desc': 'Upload an .xlsx or .xls file to view your spreadsheet without Excel. Switch between multiple sheets. All processing happens in your browser.',
        'breadcrumb': 'XLSX Viewer',
        'cross_banner_text': 'Need to view CSV data files too?',
        'cross_banner_link_text': '📊 CSV Viewer →',
        'cross_banner_href': '../csv-viewer.html',
    },
    'xml-viewer.html': {
        'title': 'XML Viewer Free Online – View XML in Tree Structure, Collapse & Expand | WooaViewer',
        'desc':  'Open .xml files for free in your browser as an interactive tree structure. Collapse/expand elements, syntax highlighting supported. RSS, SVG, HTML and all XML formats supported. Files never sent to a server.',
        'kw':    'XML viewer, open XML, XML tree viewer, free XML viewer, online XML viewer, XML parser, XML explorer, RSS viewer, XML syntax highlight, XML file viewer',
        'og_title': 'XML Viewer Free Online – Tree View, Collapse & Expand | WooaViewer',
        'og_desc':  'Open .xml files as an interactive tree. Collapse/expand elements, syntax highlighting. Free, no server upload.',
        'app_name': 'XML Viewer',
        'faq': [
            ('What XML-based formats are supported?',
             'Any .xml file is supported, including RSS feeds, SVG, HTML, and custom XML formats.'),
            ('Can I collapse and expand elements?',
             'Yes. Click any element to collapse or expand its children for easier navigation.'),
            ('Is my file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'XML Viewer – Free Online Tree View',
        'tool_desc': 'Upload an .xml file to display it in an interactive tree. Collapse/expand elements and browse the structure. All runs in your browser.',
        'breadcrumb': 'XML Viewer',
        'cross_banner_text': 'Need to view JSON files too?',
        'cross_banner_link_text': '🗂️ JSON Viewer →',
        'cross_banner_href': '../json-viewer.html',
    },
    'zip-viewer.html': {
        'title': 'ZIP Viewer Free Online – View ZIP File Contents, Preview Text & Images | WooaViewer',
        'desc':  'Upload a ZIP file to see its contents as a tree structure. Click to preview text and image files inside. View ZIP contents without extracting. Free, no server upload.',
        'kw':    'ZIP viewer, open ZIP file, ZIP contents viewer, online ZIP viewer, free ZIP viewer, archive file viewer, ZIP list checker, ZIP preview, open compressed file, ZIP file explorer',
        'og_title': 'ZIP Viewer Free Online – View ZIP Contents, Preview Files | WooaViewer',
        'og_desc':  'View ZIP file contents as a tree. Preview text and images inside. Free, no extraction needed, no server upload.',
        'app_name': 'ZIP Viewer',
        'faq': [
            ('Do I need to extract the ZIP to view its contents?',
             'No. The file list is shown as a tree structure without extracting. Click files to preview them.'),
            ('Can I preview files inside the ZIP?',
             'Yes. Text and image files can be previewed by clicking on them in the file tree.'),
            ('Is my ZIP file uploaded to a server?',
             'No. All processing happens locally in your browser. Your file is never sent anywhere.'),
        ],
        'h1': 'ZIP Viewer – View ZIP Contents Free Online',
        'tool_desc': 'Upload a ZIP file to see all its contents. Preview text and image files without extracting. All processing runs in your browser.',
        'breadcrumb': 'ZIP Viewer',
        'cross_banner_text': 'Need to compress or edit files and images?',
        'cross_banner_link_text': '🖼️ WooaImage – Image Tools →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
}

# ── 2. 공통 문자열 치환 ──────────────────────────────────────────────────────
COMMON = [
    # lang
    ('<html lang="ko">', '<html lang="en">'),
    # locale
    ('ko_KR', 'en_US'),
    # inLanguage
    ('"inLanguage": "ko"', '"inLanguage": "en"'),
    # priceCurrency
    ('"priceCurrency": "KRW"', '"priceCurrency": "USD"'),
    ('"priceCurrency":"KRW"', '"priceCurrency":"USD"'),
    # paths: CSS, JS, manifest
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('href="/manifest.json"', 'href="../manifest.json"'),
    ('src="js/', 'src="../js/'),
    ('href="js/', 'href="../js/'),

    # header nav
    ('>전체 도구 ›<', '>All Tools ›<'),
    ('>홈<', '>Home<'),

    # header-right 소개 링크
    ('>소개<', '>About<'),

    # hero section (index)
    ('어떤 파일이든 설치 없이 바로 열기', 'Open Any File — No Installation Needed'),
    ('Word, Excel, CAD, Photoshop 파일을 <strong style="color:#FFD700;">100% 무료</strong>로<br>회원가입 없이, 파일은 서버에 저장되지 않아요',
     'Open Word, Excel, CAD, Photoshop files — <strong style="color:#FFD700;">100% Free</strong><br>No signup. Files never stored on a server.'),
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),

    # hero-related (index)
    ('PDF 작업이 필요하다면?', 'Need to work with PDF files?'),
    ('WooaPDF 무료 PDF 도구 보기 →', 'WooaPDF Free PDF Tools →'),

    # index category titles & descs
    ('<span class="category-title">문서 뷰어</span>', '<span class="category-title">Document Viewer</span>'),
    ('<p class="category-desc">Word, Excel 등 오피스 파일을 설치 없이 열어보기</p>',
     '<p class="category-desc">Open Office files like Word and Excel without installation</p>'),
    ('<span class="category-title">설계 · 디자인 뷰어</span>', '<span class="category-title">Design & CAD Viewer</span>'),
    ('<p class="category-desc">CAD 도면과 디자인 파일을 무료로 열어보기</p>',
     '<p class="category-desc">Open CAD drawings and design files for free</p>'),
    ('<span class="category-title">3D · 개발자 도구</span>', '<span class="category-title">3D & Developer Tools</span>'),
    ('<p class="category-desc">3D 모델 파일과 데이터 구조 파일 보기</p>',
     '<p class="category-desc">View 3D model files and structured data files</p>'),

    # tool card names (index)
    ('<div class="tool-name">DOCX 뷰어</div>', '<div class="tool-name">DOCX Viewer</div>'),
    ('<div class="tool-name">XLSX 뷰어</div>', '<div class="tool-name">XLSX Viewer</div>'),
    ('<div class="tool-name">Markdown 뷰어</div>', '<div class="tool-name">Markdown Viewer</div>'),
    ('<div class="tool-name">EPUB 뷰어</div>', '<div class="tool-name">EPUB Viewer</div>'),
    ('<div class="tool-name">DXF 뷰어</div>', '<div class="tool-name">DXF Viewer</div>'),
    ('<div class="tool-name">PSD 뷰어</div>', '<div class="tool-name">PSD Viewer</div>'),
    ('<div class="tool-name">HEIC 뷰어</div>', '<div class="tool-name">HEIC Viewer</div>'),
    ('<div class="tool-name">STL 뷰어</div>', '<div class="tool-name">STL Viewer</div>'),
    ('<div class="tool-name">GCode 뷰어</div>', '<div class="tool-name">GCode Viewer</div>'),
    ('<div class="tool-name">JSON 뷰어</div>', '<div class="tool-name">JSON Viewer</div>'),
    ('<div class="tool-name">XML 뷰어</div>', '<div class="tool-name">XML Viewer</div>'),
    ('<div class="tool-name">CSV 뷰어</div>', '<div class="tool-name">CSV Viewer</div>'),
    ('<div class="tool-name">ZIP 내용물 뷰어</div>', '<div class="tool-name">ZIP Contents Viewer</div>'),
    ('<div class="tool-name">SVG 뷰어</div>', '<div class="tool-name">SVG Viewer</div>'),
    ('<div class="tool-name">폰트 뷰어</div>', '<div class="tool-name">Font Viewer</div>'),

    # tool card descs (index)
    ('<div class="tool-desc">Word 없이 .docx 문서 열어보기</div>',
     '<div class="tool-desc">Open .docx documents without Word</div>'),
    ('<div class="tool-desc">Excel 없이 .xlsx 스프레드시트 열어보기</div>',
     '<div class="tool-desc">Open .xlsx spreadsheets without Excel</div>'),
    ('<div class="tool-desc">.md 파일을 렌더링된 형태로 보기</div>',
     '<div class="tool-desc">View .md files rendered as HTML</div>'),
    ('<div class="tool-desc">전자책 .epub 파일 브라우저에서 읽기</div>',
     '<div class="tool-desc">Read .epub eBook files in your browser</div>'),
    ('<div class="tool-desc">AutoCAD 없이 .dxf 도면 열어보기</div>',
     '<div class="tool-desc">Open .dxf CAD drawings without AutoCAD</div>'),
    ('<div class="tool-desc">Photoshop 없이 .psd 파일 미리보기</div>',
     '<div class="tool-desc">Preview .psd files without Photoshop</div>'),
    ('<div class="tool-desc">아이폰 .heic 사진 코덱 없이 열기 · PNG/JPG 저장</div>',
     '<div class="tool-desc">Open .heic iPhone photos — save as PNG/JPG</div>'),
    ('<div class="tool-desc">3D 프린팅 .stl 파일 브라우저에서 회전·확인</div>',
     '<div class="tool-desc">Rotate and inspect .stl 3D printing files</div>'),
    ('<div class="tool-desc">3D 프린터 .gcode 슬라이서 파일 툴패스 시각화</div>',
     '<div class="tool-desc">Visualize .gcode toolpath layer by layer</div>'),
    ('<div class="tool-desc">JSON 파일을 트리 구조로 보기</div>',
     '<div class="tool-desc">View JSON files as an interactive tree</div>'),
    ('<div class="tool-desc">XML 파일을 접기/펼치기 트리 구조로 보기</div>',
     '<div class="tool-desc">View XML files as a collapsible tree</div>'),
    ('<div class="tool-desc">CSV 파일을 테이블로 보기, 정렬·검색 지원</div>',
     '<div class="tool-desc">View CSV files as a table, with sort & search</div>'),
    ('<div class="tool-desc">ZIP 압축 파일 내부 목록 확인, 텍스트·이미지 미리보기</div>',
     '<div class="tool-desc">View ZIP contents list and preview files inside</div>'),
    ('<div class="tool-desc">SVG 파일 미리보기·소스 확인·PNG 변환 다운로드</div>',
     '<div class="tool-desc">Preview SVG, view source, convert to PNG</div>'),
    ('<div class="tool-desc">TTF·OTF·WOFF 폰트 파일 미리보기, 크기·굵기 조절</div>',
     '<div class="tool-desc">Preview TTF/OTF/WOFF font files, adjust size & weight</div>'),

    # free/new badges
    ('>무료<', '>Free<'),

    # features section (index)
    ('<div class="feature-title">100% 안전</div>', '<div class="feature-title">100% Safe</div>'),
    ('<div class="feature-desc">파일이 서버로 전송되지 않습니다. 모든 처리가 브라우저 안에서 이루어집니다.</div>',
     '<div class="feature-desc">Files are never sent to a server. All processing happens inside your browser.</div>'),
    ('<div class="feature-title">빠른 로딩</div>', '<div class="feature-title">Fast Loading</div>'),
    ('<div class="feature-desc">업로드 대기 없이 로컬에서 즉시 처리합니다.</div>',
     '<div class="feature-desc">Processed instantly on your device — no upload wait.</div>'),
    ('<div class="feature-title">완전 무료</div>', '<div class="feature-title">Completely Free</div>'),
    ('<div class="feature-desc">회원가입 없이 모든 뷰어를 무료로 사용할 수 있습니다.</div>',
     '<div class="feature-desc">All viewers are free — no signup required.</div>'),
    ('<div class="feature-title">모든 기기 지원</div>', '<div class="feature-title">All Devices</div>'),
    ('<div class="feature-desc">PC, 태블릿, 스마트폰 어디서나 사용 가능한 반응형 디자인.</div>',
     '<div class="feature-desc">Responsive design works on PC, tablet, and smartphone.</div>'),

    # footer brand desc (index)
    ('<p>DOCX, XLSX, DXF, PSD 등 다양한 파일을 설치 없이 브라우저에서 안전하게 열어보세요.</p>',
     '<p>Open DOCX, XLSX, DXF, PSD and more safely in your browser — no installation needed.</p>'),

    # footer brand desc (tool pages)
    ('<p>다양한 파일을 설치 없이 브라우저에서 안전하게 열어보세요.</p>',
     '<p>Open various file types safely in your browser — no installation needed.</p>'),

    # footer link section headings
    ('<h4>문서 뷰어</h4>', '<h4>Document Viewer</h4>'),
    ('<h4>데이터 · 개발</h4>', '<h4>Data & Dev Tools</h4>'),
    ('<h4>설계 · 3D · 개발</h4>', '<h4>Design & 3D & Dev</h4>'),
    ('<h4>WooaHouse 서비스</h4>', '<h4>WooaHouse Services</h4>'),

    # footer link texts (index)
    ('>DOCX 뷰어<', '>DOCX Viewer<'),
    ('>XLSX 뷰어<', '>XLSX Viewer<'),
    ('>Markdown 뷰어<', '>Markdown Viewer<'),
    ('>EPUB 뷰어<', '>EPUB Viewer<'),
    ('>DXF 뷰어<', '>DXF Viewer<'),
    ('>PSD 뷰어<', '>PSD Viewer<'),
    ('>HEIC 뷰어<', '>HEIC Viewer<'),
    ('>STL 뷰어<', '>STL Viewer<'),
    ('>GCode 뷰어<', '>GCode Viewer<'),
    ('>JSON 뷰어<', '>JSON Viewer<'),
    ('>XML 뷰어<', '>XML Viewer<'),
    ('>CSV 뷰어<', '>CSV Viewer<'),
    ('>ZIP 뷰어<', '>ZIP Viewer<'),
    ('>SVG 뷰어<', '>SVG Viewer<'),
    ('>폰트 뷰어<', '>Font Viewer<'),

    # breadcrumb spans (tool pages)
    ('<span>CSV 뷰어</span>', '<span>CSV Viewer</span>'),
    ('<span>DOCX 뷰어</span>', '<span>DOCX Viewer</span>'),
    ('<span>DXF 뷰어</span>', '<span>DXF Viewer</span>'),
    ('<span>EPUB 뷰어</span>', '<span>EPUB Viewer</span>'),
    ('<span>폰트 뷰어</span>', '<span>Font Viewer</span>'),
    ('<span>GCode 뷰어</span>', '<span>GCode Viewer</span>'),
    ('<span>HEIC 뷰어</span>', '<span>HEIC Viewer</span>'),
    ('<span>JSON 뷰어</span>', '<span>JSON Viewer</span>'),
    ('<span>Markdown 뷰어</span>', '<span>Markdown Viewer</span>'),
    ('<span>PSD 뷰어</span>', '<span>PSD Viewer</span>'),
    ('<span>STL 뷰어</span>', '<span>STL Viewer</span>'),
    ('<span>SVG 뷰어</span>', '<span>SVG Viewer</span>'),
    ('<span>XLSX 뷰어</span>', '<span>XLSX Viewer</span>'),
    ('<span>XML 뷰어</span>', '<span>XML Viewer</span>'),
    ('<span>ZIP 내용물 뷰어</span>', '<span>ZIP Viewer</span>'),

    # drop zone texts (generic)
    ('파일을 여기에 끌어다 놓으세요', 'Drop your file here'),
    ('파일 선택', 'Select File'),

    # CSV viewer specifics
    ('CSV 파일을 여기에 끌어다 놓으세요', 'Drop your CSV file here'),
    ('.csv 형식을 지원합니다', 'Supports .csv format'),
    ('<label>구분자:</label>', '<label>Delimiter:</label>'),
    ('<label for="delimSelect">구분자:</label>', '<label for="delimSelect">Delimiter:</label>'),
    ('<option value=",">쉼표 (,)</option>', '<option value=",">Comma (,)</option>'),
    ('<option value="&#9;">탭 (\\t)</option>', '<option value="&#9;">Tab (\\t)</option>'),
    ('<option value=";">세미콜론 (;)</option>', '<option value=";">Semicolon (;)</option>'),
    ('<button class="mode-tab active" id="tabUpload" onclick="switchMode(\'upload\')">파일 업로드</button>',
     '<button class="mode-tab active" id="tabUpload" onclick="switchMode(\'upload\')">Upload File</button>'),
    ('<button class="mode-tab" id="tabPaste" onclick="switchMode(\'paste\')">직접 입력</button>',
     '<button class="mode-tab" id="tabPaste" onclick="switchMode(\'paste\')">Paste Text</button>'),
    ('<button class="parse-btn" onclick="parseFromInput()">파싱</button>',
     '<button class="parse-btn" onclick="parseFromInput()">Parse</button>'),
    ('placeholder="검색..."', 'placeholder="Search..."'),
    ('<button class="fullscreen-btn" onclick="toggleFullscreen()">전체화면</button>',
     '<button class="fullscreen-btn" onclick="toggleFullscreen()">Fullscreen</button>'),
    ("btn.textContent = csvWrap.classList.contains('fullscreen') ? '전체화면 닫기' : '전체화면';",
     "btn.textContent = csvWrap.classList.contains('fullscreen') ? 'Exit Fullscreen' : 'Fullscreen';"),
    ("'CSV 파싱 오류: '", "'CSV parse error: '"),
    ("'데이터가 없습니다.'", "'No data found.'"),
    ("parseCSV(text, '입력', new Blob([text]).size);", "parseCSV(text, 'input', new Blob([text]).size);"),

    # DOCX viewer specifics
    ('파일을 여기에 끌어다 놓거나 버튼을 클릭하세요', 'Drop your file here or click the button'),
    ('.docx 형식을 지원합니다', 'Supports .docx format'),

    # XLSX viewer specifics
    ('.xlsx, .xls 형식을 지원합니다', 'Supports .xlsx, .xls format'),

    # font viewer specifics
    ('폰트 파일을 여기에 끌어다 놓으세요', 'Drop your font file here'),
    ('TTF, OTF, WOFF, WOFF2 형식 지원', 'Supports TTF, OTF, WOFF, WOFF2'),

    # HEIC viewer specifics
    ('.heic, .heif 형식을 지원합니다', 'Supports .heic, .heif format'),

    # SVG viewer specifics
    ('SVG 파일을 여기에 끌어다 놓거나 코드를 붙여넣으세요', 'Drop your SVG file here or paste the code'),

    # ZIP viewer specifics
    ('ZIP 파일을 여기에 끌어다 놓으세요', 'Drop your ZIP file here'),
    ('.zip 형식을 지원합니다', 'Supports .zip format'),

    # Markdown viewer specifics
    ('Markdown 파일을 여기에 끌어다 놓거나 텍스트를 붙여넣으세요', 'Drop your Markdown file here or paste text'),
    ('.md, .markdown 형식을 지원합니다', 'Supports .md, .markdown format'),

    # JSON viewer specifics
    ('JSON 파일을 여기에 끌어다 놓거나 텍스트를 붙여넣으세요', 'Drop your JSON file here or paste text'),
    ('.json 형식을 지원합니다', 'Supports .json format'),

    # XML viewer specifics
    ('XML 파일을 여기에 끌어다 놓거나 텍스트를 붙여넣으세요', 'Drop your XML file here or paste text'),
    ('.xml 형식을 지원합니다', 'Supports .xml format'),

    # DXF viewer specifics
    ('DXF 파일을 여기에 끌어다 놓으세요', 'Drop your DXF file here'),
    ('.dxf 형식을 지원합니다', 'Supports .dxf format'),

    # STL viewer specifics
    ('STL 파일을 여기에 끌어다 놓으세요', 'Drop your STL file here'),
    ('.stl 형식을 지원합니다', 'Supports .stl format'),

    # GCode viewer specifics
    ('GCode 파일을 여기에 끌어다 놓으세요', 'Drop your GCode file here'),
    ('.gcode 형식을 지원합니다', 'Supports .gcode format'),

    # PSD viewer specifics
    ('PSD 파일을 여기에 끌어다 놓으세요', 'Drop your PSD file here'),
    ('.psd 형식을 지원합니다', 'Supports .psd format'),

    # EPUB viewer specifics
    ('EPUB 파일을 여기에 끌어다 놓으세요', 'Drop your EPUB file here'),
    ('.epub 형식을 지원합니다', 'Supports .epub format'),

    # common download buttons
    ('>⬇️ 다운로드<', '>⬇️ Download<'),
    ('⬇️ 다운로드', '⬇️ Download'),
    ('>⬇️ PNG 다운로드<', '>⬇️ Download PNG<'),
    ('>⬇️ JPG 다운로드<', '>⬇️ Download JPG<'),

    # common UI texts
    ('>다시 열기<', '>Open Again<'),
    ('>다시 시작<', '>Start Over<'),
    ('>복사<', '>Copy<'),
    ('>전체 선택<', '>Select All<'),
    ('처리 중...', 'Processing...'),
    ('로딩 중...', 'Loading...'),
    ('렌더링 중...', 'Rendering...'),

    # error messages (JS)
    ("'파일을 선택해주세요.'", "'Please select a file.'"),
    ("'지원하지 않는 파일 형식입니다.'", "'Unsupported file format.'"),
    ("'파일을 읽을 수 없습니다.'", "'Cannot read file.'"),
    ("'파일을 불러오는 중 오류가 발생했습니다.'", "'Failed to load file.'"),

    # footer
    ('모든 권리 보유.', 'All rights reserved.'),
    ('>개인정보처리방침<', '>Privacy Policy<'),
    ('href="privacy.html"', 'href="../privacy.html"'),
    ('href="about.html"', 'href="../about.html"'),

    # FAQ heading
    ('>자주 묻는 질문<', '>Frequently Asked Questions<'),

    # pwa install button
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),

    # our-sites-bar active link → en/
    ('href="https://wooaviewer.wooahouse.com/" target="_blank" rel="noopener" class="active"',
     'href="https://wooaviewer.wooahouse.com/en/" target="_blank" rel="noopener" class="active"'),
]

# ── 3. 언어 선택기 CSS ────────────────────────────────────────────────────────
LANG_SWITCHER_CSS = """    .lang-switcher { display:flex; align-items:center; gap:4px; }
    .lang-switcher a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:0.8rem; font-weight:600; padding:3px 8px; border-radius:12px; transition:background 0.15s; }
    .lang-switcher a.active { color:white; background:rgba(255,255,255,0.25); }
    .lang-switcher a:hover { color:white; background:rgba(255,255,255,0.18); }
    .lang-switcher span { color:rgba(255,255,255,0.3); font-size:0.75rem; }
"""

SITE_URL = 'https://wooaviewer.wooahouse.com'
THEME_COLOR = '#0284C7'


def build_page(filename, meta):
    ko_path = os.path.join(BASE, filename)
    en_path = os.path.join(EN_DIR, filename)

    with open(ko_path, encoding='utf-8') as f:
        html = f.read()

    # ── 메타 태그 교체 ──
    html = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{meta["desc"]}"', html)
    html = re.sub(r'<meta name="keywords" content="[^"]*"',
                  f'<meta name="keywords" content="{meta["kw"]}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"',
                  f'<meta property="og:title" content="{meta["og_title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"',
                  f'<meta property="og:description" content="{meta["og_desc"]}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"',
                  f'<meta property="og:url" content="{SITE_URL}/en/{filename}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"',
                  f'<link rel="canonical" href="{SITE_URL}/en/{filename}"', html)

    # ── hreflang 추가 (canonical 바로 뒤) ──
    hreflang = (
        f'\n  <link rel="alternate" hreflang="ko" href="{SITE_URL}/{filename}">'
        f'\n  <link rel="alternate" hreflang="en" href="{SITE_URL}/en/{filename}">'
        f'\n  <link rel="alternate" hreflang="x-default" href="{SITE_URL}/en/{filename}">'
    )
    html = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1' + hreflang, html)

    # ── ld+json 업데이트 ──
    # Replace Korean name fields
    html = re.sub(r'"name": "([^"]*[가-힣][^"]*)"', f'"name": "{meta["app_name"]}"', html)
    # Replace Korean description fields
    html = re.sub(r'"description": "([^"]*[가-힣][^"]*)"', f'"description": "{meta["desc"]}"', html)
    # Replace URL in ld+json for tool pages
    html = re.sub(
        r'"url": "' + re.escape(SITE_URL) + r'/' + re.escape(filename) + '"',
        f'"url": "{SITE_URL}/en/{filename}"',
        html
    )
    # Fix index.html WebSite url
    if filename == 'index.html':
        html = re.sub(
            r'"url": "' + re.escape(SITE_URL) + r'/"',
            f'"url": "{SITE_URL}/en/"',
            html
        )
        # Fix ItemList urls (keep as ko pages for cross-reference)
        # Update inLanguage in ItemList/WebSite to "en"
    # Also fix compact JSON (no spaces after colon)
    html = re.sub(
        r'"url":"' + re.escape(SITE_URL) + r'/' + re.escape(filename) + '"',
        f'"url":"{SITE_URL}/en/{filename}"',
        html
    )

    # ── Tool header (h1, tool_desc, breadcrumb) ──
    if meta.get('h1'):
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>',
                          f'<h1 id="toolTitle">{meta["h1"]}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', f'<h1>{meta["h1"]}</h1>', html, count=1)
        html = replaced

    if meta.get('tool_desc'):
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>',
                          f'<p id="toolDesc">{meta["tool_desc"]}</p>', html)
        if replaced == html:
            replaced = re.sub(
                r'(<div class="tool-header">.*?<h1>[^<]*</h1>\s*)<p>[^<]*</p>',
                r'\g<1>' + f'<p>{meta["tool_desc"]}</p>',
                html, count=1, flags=re.DOTALL
            )
        html = replaced

    if meta.get('breadcrumb') and meta['breadcrumb'] != 'Home':
        html = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>',
                      f'<span id="breadcrumbTitle">{meta["breadcrumb"]}</span>', html)
        html = re.sub(
            r'(<div class="breadcrumb">.*?<span>›</span>\s*)<span>([^<]+)</span>',
            r'\g<1><span>' + meta['breadcrumb'] + r'</span>',
            html, count=1, flags=re.DOTALL
        )

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
        if 'lang-switcher' not in html:
            html = html.replace('</style>', LANG_SWITCHER_CSS + '</style>', 1)

    # ── 헤더에 언어 선택기 삽입 ──
    # WooaViewer has header-right with 소개 link on some pages; insert lang-switcher
    # Replace existing header-right 소개 link or insert before </div></header>
    if 'header-right' in html:
        html = re.sub(
            r'<div class="header-right">[^<]*<a href="about\.html"[^>]*>[^<]*</a>[^<]*</div>',
            f'<div class="header-right">\n'
            f'      <div class="lang-switcher">\n'
            f'        <a href="../{filename}">KO</a>\n'
            f'        <span>|</span>\n'
            f'        <a href="{filename}" class="active">EN</a>\n'
            f'      </div>\n'
            f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
            f'    </div>',
            html, count=1, flags=re.DOTALL
        )
    else:
        html = re.sub(
            r'(\s*</div>\s*</header>)',
            f'\n    <div class="header-right">\n'
            f'      <div class="lang-switcher">\n'
            f'        <a href="../{filename}">KO</a>\n'
            f'        <span>|</span>\n'
            f'        <a href="{filename}" class="active">EN</a>\n'
            f'      </div>\n'
            f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</header>',
            html, count=1
        )

    # ── 쿠팡 광고 제거 ──
    html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
    html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
    html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)

    # ── og:locale 교체 (COMMON에서 처리 안 된 경우 대비) ──
    html = html.replace('content="ko_KR"', 'content="en_US"')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  ✅ en/{filename}')


# ── 4. 실행 ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Building WooaViewer English pages...')
    for filename, meta in PAGE_META.items():
        ko_path = os.path.join(BASE, filename)
        if os.path.exists(ko_path):
            build_page(filename, meta)
        else:
            print(f'  ⚠️  {filename} not found, skipping')
    print(f'\nDone! {len(PAGE_META)} files generated in en/')
