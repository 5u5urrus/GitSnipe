<p align="center">
  <img src="gitsnipe.png" width="100%" alt="GitSnipe Banner">
</p>

# GitSnipe  
A GitHub code scanner that mimics GitHub's search bar exactly. Designed for accurate pinpoint searches. Automate GitHub searches with advanced syntax support for security research, OSINT, and data analysis. The little brother of GitBlast.

## Features
- **Exact GitHub search replication**: Uses GitHub’s API to perform searches just like the search bar.
- **Extensive search qualifiers**: Supports filters like language, repo, file type, and more.
- **Flexible syntax**: Supports `OR`, `NOT`, and exact phrase matches.
- **Optimized for secrets**: Helps uncover exposed API keys, credentials, and sensitive information.
- **Fast and scalable**: Batches results and handles pagination.
- **Lightweight**: Requires minimal dependencies and runs directly with Python.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUserName/gitsnipe.git
   ```
2. **Install Python 3.6+ and Requests**:
   ```bash
   cd gitsnipe
   pip install requests
   ```
3. **Obtain a GitHub token** (Personal Access Token):
   - Generate at [GitHub Token Settings](https://github.com/settings/tokens)
   - Copy and keep it secure.

## Usage

### Basic Search
```bash
python gitsnipe.py "password"
```
Finds code containing the word **password**.

```bash
python gitsnipe.py "companysite.com"
```
Finds code containing the company url.

### Advanced Search with Filters
```bash
python gitsnipe.py "api_key extension:json"
```
Finds JSON files containing **api_key**.

### OR Logic
```bash
python gitsnipe.py "password OR secret"
```
Finds code containing either **password** or **secret**.

### Search Specific Repositories or Orgs
```bash
python gitsnipe.py "AWS_ACCESS_KEY_ID org:myorg"
```
Finds AWS keys in all repos of an organization.

### Full Syntax
```bash
python gitsnipe.py "<query>" [--exact] [--help]
```
- `<query>`: The GitHub search query (e.g., `"password"` or `"api_key extension:json"`)
- `--exact`: Forces exact phrase matching.
- `--help`: Displays search syntax guide.

## Examples

### Search for Passwords in Python Files
```bash
python gitsnipe.py "password extension:py"
```
**Sample Output**:
```
[*] Searching GitHub for query: password extension:py
[+] Found 5 matches.
 - repo1 :: config/settings.py
   https://github.com/user/repo1/blob/main/config/settings.py
 - repo2 :: secrets.py
   https://github.com/user/repo2/blob/main/secrets.py
```

### Search for API Keys in JSON Files
```bash
python gitsnipe.py "api_key extension:json"
```

### Find Database Credentials in PHP
```bash
python gitsnipe.py "DB_PASSWORD extension:php"
```

## Configuration

- **`GITHUB_TOKEN`**: Your GitHub Personal Access Token.
- **`MAX_PAGES`**: How many pages of results to fetch per search.
- **`PER_PAGE_RESULTS`**: Number of results per API request.
- **`RATE_LIMIT_PAUSE`**: Adjusts delay between API calls to avoid hitting rate limits.

## Requirements

- **Python 3.6+**
- **Requests library** (installed via pip)
- **GitHub token** with search access

## Contributing

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YourUserName/gitsnipe.git
   ```
3. **Create** a new branch for your feature:
   ```bash
   git checkout -b feature-xyz
   ```
4. **Commit & Push Changes**:
   ```bash
   git add .
   git commit -m "Added new feature"
   git push origin feature-xyz
   ```
5. **Open a Pull Request** on GitHub.

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Author

Created by [Vahe Demirkhanyan](mailto:vdemirkhanyan@yahoo.ca)

<p align="center">
  <strong>Snipe secrets before attackers do - GitSnipe, your first line of defense.</strong>
</p>
