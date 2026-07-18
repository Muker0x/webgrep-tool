import requests
import re
def scan_url(url,keyword):
    try:
        response = requests.get(url,timeout=5)
        text = response.text
        found = False
        lines = text.split('\n')        
        for line_num, line in enumerate(lines, 1):
             #fixed keyword search, now shows only lines that actually contain it
             if keyword.lower() in line.lower():
                 found = True
                 idx = line.lower().find(keyword.lower())
                 # dont go below 0 or past the end of the line
                 start = max(0, idx - 100)
                 end = min(len(line), idx + 100)
                 context = line[start:end].strip()
                 print(f"  [Line {line_num}] ...{context}...")        


        if not found:
            print(f"[-] keyword not found")
       
    except Exception as e:
        print(f"[ERROR] {e}")
while True:

    print("=== WebGrep - Source code scanner ===\n")
    print("Scan mode: ")
    print("[1] Single URL")
    print("[2] Multiple URLs")
    mode = input("\nChoose: ")

    keyword = input("Enter keyword: ")

    if mode == "1":
        url = input("Enter Target URL: ")
        print(f"[*] Scanning {url} \n")
        scan_url(url,keyword)

    elif mode == "2":
        urls_input = input("Enter URLs comma separated: ")
        urls = [url.strip() for url in urls_input.split(",")]
    
        for url in urls:
            print(f"\n{'='*50}")
            print(f"[TARGET] {url}")
            print(f"{'='*50}")
            scan_url(url, keyword)
    print("\n Scan completed :)\n ")
    print("[!] Note: Lines can be truncated for readability but DO contain the keyword.\n")
    ask = input("Would u like to continue ?(y/n)").lower()
    if ask == "n":
        print("Goodbye :)")
        break
    elif ask == "y":
        continue
    elif ask != "y" or "n":
        ask=input ("Please choose correct input(y/n)")
    
