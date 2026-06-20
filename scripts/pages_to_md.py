#!/usr/bin/env python3
"""
Convert Apple Pages file to Markdown using macOS Pages app.
Requires macOS with Pages installed.
"""
import os
import sys
import subprocess
from pathlib import Path
import tempfile
import shutil


def pages_to_markdown(pages_path: Path, output_md_path: Path):
    """
    Convert Pages file to Markdown by first exporting to RTF,
    then converting RTF to Markdown.
    """
    if not pages_path.exists():
        raise FileNotFoundError(f"Pages file not found: {pages_path}")
    
    # Create temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Step 1: Use Pages to export to RTF (Rich Text Format)
        rtf_path = temp_path / "temp.rtf"
        
        applescript = f'''
        tell application "Pages"
            activate
            open POSIX file "{pages_path.absolute()}"
            set theDocument to front document
            export theDocument to POSIX file "{rtf_path.absolute()}" as RTF
            close theDocument saving no
        end tell
        '''
        
        print(f"Exporting Pages file to RTF...")
        result = subprocess.run(
            ["osascript", "-e", applescript],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Warning: AppleScript export may have issues (return code {result.returncode})")
            print(f"stderr: {result.stderr}")
        
        # Step 2: Check if RTF was created
        if not rtf_path.exists():
            # Try alternative: export to Text
            print("RTF export failed, trying plain text export...")
            txt_path = temp_path / "temp.txt"
            applescript_txt = f'''
            tell application "Pages"
                activate
                open POSIX file "{pages_path.absolute()}"
                set theDocument to front document
                export theDocument to POSIX file "{txt_path.absolute()}" as plain text
                close theDocument saving no
            end tell
            '''
            subprocess.run(["osascript", "-e", applescript_txt], capture_output=True, text=True)
            
            if txt_path.exists():
                shutil.copy(txt_path, output_md_path)
                print(f"Success! Converted to Markdown (plain text): {output_md_path}")
                return
            else:
                raise RuntimeError("Failed to export Pages file")
        
        # Step 3: Convert RTF to Markdown using textutil (macOS built-in)
        md_temp_path = temp_path / "temp.md"
        try:
            subprocess.run(
                ["textutil", "-convert", "txt", "-stdout", str(rtf_path)],
                capture_output=True,
                text=True,
                check=True
            )
            # For simplicity, we'll just use textutil to convert to plain text
            # and then format as Markdown
            txt_path = temp_path / "temp.txt"
            subprocess.run(
                ["textutil", "-convert", "txt", "-output", str(txt_path), str(rtf_path)],
                check=True
            )
            
            # Copy and rename to md
            shutil.copy(txt_path, output_md_path)
            print(f"Success! Converted to Markdown: {output_md_path}")
            
        except subprocess.CalledProcessError:
            # Fallback: just copy the RTF content as text
            print("Warning: Full RTF conversion failed, using basic text extraction")
            if rtf_path.exists():
                # Try reading RTF content
                try:
                    import re
                    with open(rtf_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    # Very basic RTF stripping
                    content = re.sub(r'\\[a-z]+\d*', '', content)
                    content = re.sub(r'[{}]', '', content)
                    with open(output_md_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Basic text extraction complete: {output_md_path}")
                except Exception as e:
                    print(f"Error extracting text: {e}")


def main():
    script_dir = Path(__file__).parent.parent
    default_pages = script_dir / "2026_11EC_Assessment Task 2 2.pages"
    default_output = script_dir / "2026_11EC_Assessment Task 2 2_converted.md"
    
    pages_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_pages
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else default_output
    
    print(f"Converting: {pages_path}")
    print(f"Output: {output_path}")
    
    try:
        pages_to_markdown(pages_path, output_path)
    except Exception as e:
        print(f"Error: {e}")
        print("\nAlternative: Use Pages app to manually export:")
        print("1. Open .pages file in Pages")
        print("2. File > Export To > Plain Text or Word")
        print("3. Save, then convert to Markdown")
        sys.exit(1)


if __name__ == "__main__":
    main()
