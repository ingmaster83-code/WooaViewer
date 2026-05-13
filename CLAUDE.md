# WooaViewer 프로젝트 지침

## 개요
- **브랜드:** WooaViewer
- **URL:** https://wooaviewer.wooahouse.com
- **테마 컬러:** `#0284C7` (스카이 블루)
- **GitHub:** https://github.com/ingmaster83-code/WooaViewer
- **배포:** GitHub Pages (main 브랜치 → root)
- **참고 기준:** PDFKIT 레이아웃을 그대로 따름 (공통 지침 참조)

---

## 서비스 목적
설치가 필요한 프로그램(Word, Excel, AutoCAD, Photoshop 등) 없이
브라우저에서 다양한 파일 형식을 무료로 열어볼 수 있는 뷰어 모음.
파일은 서버에 전송되지 않아 안전.

---

## 현재 파일 구조
```
WooaViewer/
├── index.html          ← 메인 (도구 목록)
├── docx-viewer.html    ← DOCX 뷰어 (mammoth.js)
├── xlsx-viewer.html    ← XLSX 뷰어 (SheetJS)
├── dxf-viewer.html     ← DXF 뷰어 (dxf-viewer)
├── psd-viewer.html     ← PSD 뷰어 (ag-psd)
├── stl-viewer.html     ← STL 뷰어 (Three.js)
├── markdown-viewer.html ← Markdown 뷰어 (marked.js)
├── json-viewer.html    ← JSON 뷰어 (vanilla JS)
├── epub-viewer.html    ← EPUB 뷰어 (epub.js)
├── css/style.css
├── js/pwa-install.js
├── manifest.json
├── sw.js
├── robots.txt
├── sitemap.xml
└── CNAME               ← wooaviewer.wooahouse.com
```

---

## 도구별 라이브러리

| 도구 | 파일 | 라이브러리 | CDN |
|------|------|-----------|-----|
| DOCX 뷰어 | docx-viewer.html | mammoth.js | https://cdn.jsdelivr.net/npm/mammoth/mammoth.browser.min.js |
| XLSX 뷰어 | xlsx-viewer.html | SheetJS | https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js |
| DXF 뷰어 | dxf-viewer.html | dxf-viewer | ESM: https://cdn.jsdelivr.net/npm/dxf-viewer/dist/dxf-viewer.es.js |
| PSD 뷰어 | psd-viewer.html | ag-psd | ESM: https://cdn.jsdelivr.net/npm/ag-psd/dist/bundle-umd.js |
| STL 뷰어 | stl-viewer.html | Three.js + STLLoader | https://cdn.jsdelivr.net/npm/three |
| Markdown 뷰어 | markdown-viewer.html | marked.js | https://cdn.jsdelivr.net/npm/marked/marked.min.js |
| JSON 뷰어 | json-viewer.html | vanilla JS | 없음 |
| EPUB 뷰어 | epub-viewer.html | epub.js | https://cdn.jsdelivr.net/npm/epubjs/dist/epub.min.js |

---

## 도구 현황

| 도구 | 파일 | 상태 |
|------|------|------|
| DOCX 뷰어 | docx-viewer.html | 🔨 준비중 |
| XLSX 뷰어 | xlsx-viewer.html | 🔨 준비중 |
| DXF 뷰어 | dxf-viewer.html | 🔨 준비중 |
| PSD 뷰어 | psd-viewer.html | 🔨 준비중 |
| STL 뷰어 | stl-viewer.html | 🔨 준비중 |
| Markdown 뷰어 | markdown-viewer.html | 🔨 준비중 |
| JSON 뷰어 | json-viewer.html | 🔨 준비중 |
| EPUB 뷰어 | epub-viewer.html | 🔨 준비중 |

---

## ld+json 패턴
- index.html: `"@type": "WebSite"` + `"@type": "ItemList"`
- 도구 페이지: `"@type": "WebApplication"`, `applicationCategory: "UtilitiesApplication"`
