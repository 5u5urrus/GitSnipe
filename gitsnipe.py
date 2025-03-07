#!/usr/bin/env python3
# GitSnipe: Search GitHub for secrets like a sniper 
# Don't forget to include your github api key (it's free)
# Author: Vahe Demirkhanyan
import sys
import requests
GITHUB_TOKEN = "<enter your github api key here>"

def search_github_code(query, max_pages=1):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    results = []
    base_url = "https://api.github.com/search/code"
    per_page = 30
    for page in range(1, max_pages + 1):
        params = {
            "q": query,
            "per_page": per_page,
            "page": page
        }
        resp = requests.get(base_url, headers=headers, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print(f"[*] Total results available: {data.get('total_count', 0)}")
            items = data.get("items", [])
            results.extend(items)
            if len(items) < per_page:
                break
        else:
            print(f"Error: HTTP {resp.status_code} - {resp.text}")
            break
    return results

def show_help():
    print("\nGitSnipe: A GitHub code scanner that mimics GitHub's search bar")
    print("=============================================================\n")
    print("USAGE:")
    print(f"  python {sys.argv[0]} \"<search_query>\" [--exact] [--help]\n")
    
    print("SEARCH SYNTAX GUIDE:")
    print("  1. Basic Search:")
    print("     python gitsnipe.py \"password\"")
    print("     - Finds code containing the word 'password'\n")
    
    print("  2. Multiple Terms (AND logic):")
    print("     python gitsnipe.py \"api key\"")
    print("     - Finds code containing both 'api' AND 'key'\n")
    
    print("  3. OR Logic:")
    print("     python gitsnipe.py \"password OR apikey\"")
    print("     - Finds code containing either 'password' OR 'apikey'\n")
    
    print("  4. Exact Phrase Matching:")
    print("     python gitsnipe.py \"api key\" --exact")
    print("     - Finds code containing the exact phrase 'api key'\n")
    
    print("GITHUB QUALIFIERS:")
    print("  These can be combined with any search to narrow results\n")
    
    print("  File Extensions:")
    print("     extension:js         - JavaScript files")
    print("     extension:py         - Python files")
    print("     extension:java       - Java files")
    print("     extension:php        - PHP files")
    print("     extension:env        - Environment files (.env)")
    print("     extension:yaml,yml   - YAML files\n")
    
    print("  Languages:")
    print("     language:python      - Code in Python")
    print("     language:javascript  - Code in JavaScript")
    print("     language:go          - Code in Go\n")
    
    print("  Repository Filters:")
    print("     repo:username/repo   - Search in specific repository")
    print("     org:organization     - Search in all repos of an organization")
    print("     user:username        - Search in all repos of a user\n")
    
    print("  Path Filters:")
    print("     path:src/main        - Files in src/main directory")
    print("     path:/test           - Files in root test directory")
    print("     filename:config.json - Files named config.json\n")
    
    print("  Content Size:")
    print("     size:>10             - Files larger than 10KB")
    print("     size:<100            - Files smaller than 100KB\n")
    
    print("  Other Useful Qualifiers:")
    print("     created:<2023-01-01  - Code created before 2023")
    print("     pushed:>2022-06-01   - Repos pushed after June 2022")
    print("     fork:true/only       - Include/only forked repositories")
    print("     fork:false           - Exclude forked repositories")
    print("     is:public/private    - Search public/private repositories")
    print("     NOT keyword          - Exclude a term (e.g., password NOT test)\n")
    
    print("EXAMPLES:")
    print("  1. Find AWS keys in JavaScript files:")
    print("     python gitsnipe.py \"AKIA extension:js\"")
    
    print("  2. Find database passwords in PHP files:")
    print("     python gitsnipe.py \"DB_PASSWORD extension:php\"")
    
    print("  3. Find API keys in specific organization:")
    print("     python gitsnipe.py \"api_key org:companyname\"")
    
    print("  4. Find SSH keys in config files:")
    print("     python gitsnipe.py \"BEGIN PRIVATE KEY extension:pem OR extension:key\"")
    
    print("  5. Find exact match for 'Authorization: Bearer' in header files:")
    print("     python gitsnipe.py \"Authorization: Bearer extension:h\" --exact\n")
    
    sys.exit(0)

def main():
    if len(sys.argv) < 2 or "--help" in sys.argv or "-h" in sys.argv:
        show_help()
    
    query = sys.argv[1]
    use_exact = "--exact" in sys.argv
    
    contains_or_logic = " OR " in query.upper()
    
    if contains_or_logic:
        final_query = query
    else:
        parts = query.split()
        qualifiers = ["extension:", "language:", "repo:", "org:", "user:", "path:", 
                      "filename:", "size:", "created:", "pushed:", "fork:", "is:"]
        phrase_parts = []
        filter_parts = []
        
        for part in parts:
            if any(part.startswith(q) for q in qualifiers):
                filter_parts.append(part)
            else:
                phrase_parts.append(part)
        
        if use_exact and phrase_parts:
            final_query = f"\"{' '.join(phrase_parts)}\" {' '.join(filter_parts)}".strip()
        else:
            final_query = query
            
    print(f"[*] Searching GitHub for query: {final_query}")
    
    matches = search_github_code(final_query, max_pages=2)
    print(f"[+] Found {len(matches)} matches.")
    for m in matches:
        repo = m.get("repository", {}).get("full_name", "unknown_repo")
        path = m.get("path", "unknown_path")
        html_url = m.get("html_url", "no_url")
        print(f" - {repo} :: {path}")
        print(f"   {html_url}")

if __name__ == "__main__":
    main()
