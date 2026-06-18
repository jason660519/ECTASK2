#!/usr/bin/env python3
"""
Convert Markdown report to A4 PDF with academic formatting.
"""
import os
import re
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup


def fix_image_paths(html_content, base_path):
    """Fix relative image paths to absolute paths."""
    soup = BeautifulSoup(html_content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.startswith('PIC/') or src.startswith('diagrams/'):
            img['src'] = str(Path(base_path) / src)
    return str(soup)


def convert_md_to_html(md_file_path):
    """Convert Markdown file to HTML with extensions."""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
    ]
    
    html_content = markdown.markdown(md_content, extensions=extensions)
    return html_content


def create_full_html(content_html, title="Assessment Task 2 Report"):
    """Wrap HTML content in full HTML document structure."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="report_style.css">
</head>
<body>
    <div class="title-page">
        <h1>Assessment Task 2: Networking Systems and Social Computing</h1>
        <div class="student-info">
            <p><strong>Student Name:</strong> Danny Yu</p>
            <p><strong>Class:</strong> 11 CMP01</p>
            <p><strong>Due Date:</strong> Friday, 19 June 2026 – Week 9, Period 2</p>
        </div>
    </div>
    <div class="content">
        {content_html}
    </div>
</body>
</html>"""


def main():
    script_dir = Path(__file__).parent
    md_file = script_dir / "full_report_for_pdf.md"
    css_file = script_dir / "report_style.css"
    output_pdf = script_dir / "assessment_task2_report_final.pdf"
    
    print(f"Converting {md_file.name} to PDF...")
    
    # Convert Markdown to HTML
    content_html = convert_md_to_html(md_file)
    
    # Fix image paths
    content_html = fix_image_paths(content_html, str(script_dir))
    
    # Create full HTML document
    full_html = create_full_html(content_html)
    
    # Save intermediate HTML for debugging
    with open(script_dir / "temp_report.html", 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    # Convert to PDF with WeasyPrint
    HTML(string=full_html, base_url=str(script_dir)).write_pdf(
        str(output_pdf),
        stylesheets=[str(css_file)]
    )
    
    print(f"Success! PDF saved to: {output_pdf}")
    print(f"Intermediate HTML saved to: temp_report.html (for debugging)")


if __name__ == "__main__":
    main()
