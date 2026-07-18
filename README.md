# webgrep

A simple Python tool I built to scan web page source code for specific keywords.

I made this after manually hunting for hardcoded credentials in HTML/JavaScript 
during a CTF challenge. Doing it by hand was slow, so I automated it.

## What it does

- Takes a URL (or multiple URLs) and a keyword
- Fetches the page source
- Returns every line containing that keyword with line numbers
- Useful for finding login endpoints, hardcoded credentials, tokens, and other 
  sensitive info hiding in source code

## Usage

```bash
python3 webgrep.py
```

Follow the prompts — enter your target URL and keyword.

## Example

=== WebGrep - Source Code Scanner ===
Scan mode:
[1] Single URL
[2] Multiple URLs
Choose: 1
Enter keyword: password
Enter Target URL: http://testphp.vulnweb.com
[Line 47] <input type="password" name="pass">

## Requirements

```bash
pip install requests
```
## Disclaimer

Only use this on sites you have permission to test.

## Screenshot
<img width="1920" height="1080" alt="Screenshot_2026-07-18_13_59_29" src="https://github.com/user-attachments/assets/4d666ea4-9d94-4076-b776-10f949b1009a" />


