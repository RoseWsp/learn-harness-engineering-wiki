import re
from collections import defaultdict
import os
import sys

def extract_wikilinks(file_path):
    """Extract wikilinks from a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return set()
    
    # Pattern to match [[wikilinks]] including [[page|display]] format
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    
    links = set()
    for match in matches:
        # Extract the page name before the pipe if exists
        page_name = match.split('|')[0].strip()
        links.add(page_name)
    
    return links

def main():
    wiki_dir = 'wiki'
    
    if not os.path.exists(wiki_dir):
        print(f"Error: Directory {wiki_dir} not found", file=sys.stderr)
        return 1
    
    # Get all markdown files recursively
    file_links = defaultdict(set)
    
    for root, _, files in os.walk(wiki_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                links = extract_wikilinks(file_path)
                if links:
                    file_links[file] = links
    
    # Print results
    print("Wikilinks by file:")
    print("=" * 50)
    
    for filename in sorted(file_links.keys()):
        print(f"\nFile: {filename}")
        print("-" * 30)
        for link in sorted(file_links[filename]):
            print(f"- [[{link}]]")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
