#!/usr/bin/env python3
import os
import re
import requests
from urllib.parse import urljoin, urlparse

BASE_URL = "http://localhost:8000"
PROJECT_DIR = "/Users/jasonmacbbookpro/Project/ECTASK2"

# Links in sidebar
SIDEBAR_LINKS = [
    "/",
    "/readme.md",
    "/assessment_task2_report_final.md",
    "/network_diagrams.md",
    "/report_final.md",
    "/report_draft.md",
    "/project_guidelines.md",
]

# All .md files
MD_FILES = glob.glob(os.path.join(PROJECT_DIR, "**", "*.md"), recursive=True)

def check_url(url):
    """Check if URL returns 404"""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 404, response.status_code
    except Exception as e:
        return True, f"Error: {str(e)}"

def find_links_in_file(file_path):
    """Find all links in Markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find Markdown links [text](url)
    md_links = re.findall(r'\[.*?\]\((.*?)\)', content)
    
    # Find image links ![]()
    img_links = re.findall(r'!\[.*?\]\((.*?)\)', content)
    
    return md_links + img_links

def main():
    print("=" * 80)
    print("ECTASK2 Project Link Check Report")
    print("=" * 80)
    print()
    
    # Check sidebar links
    print("1. Checking sidebar links:")
    print("-" * 40)
    sidebar_404 = []
    for path in SIDEBAR_LINKS:
        url = urljoin(BASE_URL, path)
        is_404, status = check_url(url)
        if is_404:
            print(f"❌ 404: {url} (Status: {status})")
            sidebar_404.append((path, url, status))
        else:
            print(f"✅ OK: {url} (Status: {status})")
    print()
    
    # Check all project files existence
    print("2. Checking all project files:")
    print("-" * 40)
    
    # Check .md files
    print("Markdown files:")
    for md_file in sorted(MD_FILES):
        rel_path = os.path.relpath(md_file, PROJECT_DIR)
        print(f"✅ Exists: {rel_path}")
    
    # Check PIC directory
    print("\nImage files (PIC/):")
    pic_dir = os.path.join(PROJECT_DIR, "PIC")
    if os.path.exists(pic_dir):
        for pic_file in sorted(os.listdir(pic_dir)):
            print(f"✅ Exists: PIC/{pic_file}")
    
    # Check sheets_md directory
    print("\nOther files (sheets_md/):")
    sheets_dir = os.path.join(PROJECT_DIR, "sheets_md")
    if os.path.exists(sheets_dir):
        for sheet_file in sorted(os.listdir(sheets_dir)):
            print(f"✅ Exists: sheets_md/{sheet_file}")
    
    print()
    print("=" * 80)
    print("Check complete!")
    print("=" * 80)
    
    # Summary
    if sidebar_404:
        print(f"\nFound {len(sidebar_404)} 404 errors:")
        for path, url, status in sidebar_404:
            print(f"  - {path}")
    else:
        print("\n✅ No 404 errors found!")

if __name__ == "__main__":
    import glob
    main()
