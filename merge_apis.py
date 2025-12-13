import urllib.request
import re
from collections import  OrderedDict
from typing import Dict, List, Set

SOURCES = [
    "https://raw.githubusercontent.com/jaegeral/security-apis/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/smew-tech/public-apis/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/markodenic/public-apis/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/ngongcm/public-api-list/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/trntv/apis-list/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/public-apis/public-apis/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/n0shake/Public-APIs/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/marcelscruz/public-apis/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/public-api-lists/public-api-lists/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/APIs-guru/graphql-apis/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/yybmion/public-apis-4Kr/refs/heads/main/GLOBAL_PUBLIC_APIS_KR.md",
    "https://raw.githubusercontent.com/llf007/public-apis-cn/refs/heads/main/README.md"
]

# Data structure: Categories -> List of APIs
# API: {name, link, description, auth, https, cors}
database: Dict[str, List[Dict]] = OrderedDict()
seen_links: Set[str] = set()

def fetch_url(url):
    try:
        print(f"Fetching {url}...")
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def clean_text(text):
    if not text: return ""
    return text.strip().replace('\n', ' ').replace('|', '/')

def extract_link(md_link):
    # Matches [Name](Link) or just Link
    match = re.search(r'\[(.*?)\]\((.*?)\)', md_link)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return md_link.strip(), md_link.strip()

def normalize_auth(auth):
    auth = auth.lower().strip()
    if 'key' in auth: return 'apiKey'
    if 'oauth' in auth: return 'OAuth'
    if auth in ['no', 'none', 'null', '']: return 'No'
    return auth

def parse_markdown(content):
    current_category = "Miscellaneous"
    
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Category detection (Headers)
        if line.startswith('##') and not line.startswith('###'): # Assume level 2 headers are categories
            current_category = line.lstrip('#').strip()
            # Clean up category name (remove links, emojis usually)
            current_category = re.sub(r'\[.*?\]\(.*?\)', '', current_category).strip()
            
        # Table detection
        if line.startswith('|'):
            # Check if it's a header line
            if '---' in lines[i+1]:
                headers = [h.strip().lower() for h in line.strip('|').split('|')]
                # Map headers to indices
                idx_map = {}
                for idx, h in enumerate(headers):
                    if 'api' in h or 'name' in h: idx_map['name'] = idx
                    elif 'desc' in h: idx_map['desc'] = idx
                    elif 'auth' in h: idx_map['auth'] = idx
                    elif 'http' in h: idx_map['https'] = idx
                    elif 'cors' in h: idx_map['cors'] = idx
                    elif 'link' in h : idx_map['link'] = idx

                # Process table rows
                i += 2
                while i < len(lines) and lines[i].strip().startswith('|'):
                    row = [c.strip() for c in lines[i].strip('|').split('|')]
                    # Handle cases where row might be missing tail pipes or whatever
                    if len(row) < len(headers): 
                         # Try to fill missing cols
                         row += [''] * (len(headers) - len(row))
                    
                    entry = {}
                    
                    # Extract Name and Link
                    raw_name = row[idx_map.get('name', 0)] if 'name' in idx_map else "Unknown"
                    raw_link_col = row[idx_map.get('link', -1)] if 'link' in idx_map else ""
                    
                    name_text, link_url = extract_link(raw_name)
                    
                    # If explicit link column exists and extracted link from name is effectively empty or same as name
                    if raw_link_col:
                        _, link_url_col = extract_link(raw_link_col)
                        if link_url_col and not link_url.startswith('http'):
                             link_url = link_url_col
                    
                    # Basic Validation
                    if not link_url.startswith('http'):
                        i+=1
                        continue

                    # Deduplication
                    normalized_link = link_url.rstrip('/').lower()
                    if normalized_link in seen_links:
                        i+=1
                        continue
                    seen_links.add(normalized_link)
                    
                    entry['name'] = name_text
                    entry['link'] = link_url
                    entry['description'] = row[idx_map.get('desc', 1)] if 'desc' in idx_map else ""
                    entry['auth'] = normalize_auth(row[idx_map.get('auth', 2)]) if 'auth' in idx_map else "Unknown"
                    entry['https'] = row[idx_map.get('https', 3)] if 'https' in idx_map else "Unknown"
                    entry['cors'] = row[idx_map.get('cors', 4)] if 'cors' in idx_map else "Unknown"
                    
                    if current_category not in database:
                        database[current_category] = []
                    database[current_category].append(entry)
                    
                    i += 1
                continue
        i += 1

def generate_readme():
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("# Ultimate Free APIs Collection\n\n")
        f.write("A massive, curated, and community-driven collection of free and public APIs. Aggregated from over 10 different awesome-lists to be the most complete resource on the internet.\n\n")
        
        # Index
        f.write("## Index\n\n")
        sorted_categories = sorted(database.keys())
        for cat in sorted_categories:
            if not cat or cat.lower() == "index" or len(database[cat]) == 0: continue
            anchor = cat.lower().replace(' ', '-').replace('&', '').replace('.', '')
            f.write(f"- [{cat}](#{anchor})\n")
        f.write("\n---\n\n")
        
        # Content
        for cat in sorted_categories:
            if not cat or cat.lower() == "index" or len(database[cat]) == 0: continue
            
            f.write(f"## {cat}\n\n")
            f.write("| API | Description | Auth | HTTPS | CORS |\n")
            f.write("|---|---|---|---|---|\n")
            
            # Sort entries by name
            entries = sorted(database[cat], key=lambda x: x['name'].lower())
            
            for entry in entries:
                desc = clean_text(entry['description'])
                auth = clean_text(entry['auth'])
                https = clean_text(entry['https'])
                cors = clean_text(entry['cors'])
                
                # Truncate desc if too long? No, let it wrap.
                
                f.write(f"| [{entry['name']}]({entry['link']}) | {desc} | {auth} | {https} | {cors} |\n")
            
            f.write("\n**[⬆ Back to Index](#index)**\n\n")

def main():
    for source in SOURCES:
        content = fetch_url(source)
        parse_markdown(content)
    
    print(f"Total unique APIs found: {len(seen_links)}")
    generate_readme()

if __name__ == "__main__":
    main()
