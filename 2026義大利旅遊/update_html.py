import markdown
import sys

def convert_md_to_html(md_file, html_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
        html = markdown.markdown(text, extensions=['tables', 'fenced_code', 'nl2br'])
        
        css = """
        <style>
            :root {
                --primary: #2d3748;
                --secondary: #4a5568;
                --accent: #3182ce;
                --bg: #f7fafc;
                --card-bg: #ffffff;
                --text: #1a202c;
                --border: #e2e8f0;
            }
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                line-height: 1.6;
                color: var(--text);
                background-color: var(--bg);
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 1000px;
                margin: 0 auto;
                padding: 2rem;
            }
            header {
                background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
                color: white;
                padding: 3rem 2rem;
                border-radius: 12px;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            h2 {
                color: var(--primary);
                border-bottom: 2px solid var(--accent);
                padding-bottom: 0.5rem;
                margin-top: 2.5rem;
            }
            h3 {
                color: var(--secondary);
                margin-top: 2rem;
            }
            a {
                color: var(--accent);
                text-decoration: none;
                font-weight: 500;
                transition: color 0.2s;
            }
            a:hover {
                color: #2b6cb0;
                text-decoration: underline;
            }
            .nav-links {
                background: var(--card-bg);
                padding: 1rem 1.5rem;
                border-radius: 8px;
                margin-bottom: 2rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                border: 1px solid var(--border);
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 1.1rem;
            }
            .nav-links a {
                display: inline-block;
                padding: 0.5rem 1rem;
                background: #ebf8ff;
                border-radius: 6px;
                border: 1px solid #bee3f8;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
                background: var(--card-bg);
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                border-radius: 8px;
                overflow: hidden;
            }
            th, td {
                padding: 12px 15px;
                text-align: left;
                border-bottom: 1px solid var(--border);
            }
            th {
                background-color: var(--primary);
                color: white;
                font-weight: 600;
            }
            tr:hover {
                background-color: #edf2f7;
            }
            blockquote {
                border-left: 4px solid var(--accent);
                background: #ebf8ff;
                margin: 1.5rem 0;
                padding: 1rem 1.5rem;
                border-radius: 0 8px 8px 0;
            }
            ul, ol {
                padding-left: 1.5rem;
            }
            li {
                margin-bottom: 0.5rem;
            }
            .content-wrapper {
                background: var(--card-bg);
                padding: 2.5rem;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            }
        </style>
        """
        
        full_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2026 德國北義之旅 - Ortisei 每日行程表</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    {css}
</head>
<body>
    <div class="container">
        <header>
            <h1>🏔️ 2026 德國北義之旅 (7/17 - 8/1)</h1>
            <p>慕尼黑 ➔ 多洛米蒂 (Ortisei) ➔ 奧地利 ➔ 國王湖</p>
        </header>
        
        <div class="nav-links">
            <span>👉 <strong>關聯文件：</strong></span>
            <a href="Wanderkarte步道解析表.html" target="_blank">🗺️ Wanderkarte 步道解析表 (含地形與難度評估)</a>
        </div>
        
        <div class="content-wrapper">
            {html}
        </div>
    </div>
</body>
</html>"""
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
    except Exception as e:
        print(f'Error: {e}')

convert_md_to_html('/Users/jasminelai/2026義大利旅遊/Ortisei每日行程表.md', '/Users/jasminelai/2026義大利旅遊/2026德國北義之旅.html')
