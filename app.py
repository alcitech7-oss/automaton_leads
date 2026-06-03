import requests
import time
import re

webhook_url = "https://hook.us2.make.com/1wnc6e94cx7b4b0b9st6xtasv811xvo9"

def extract_info(text):
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group(0).rstrip('.,;:') if email_match else "N/A"
    
    phone_match = re.search(r'\d[\d\s\-\(\)\.]{7,}\d', text)
    phone = phone_match.group(0) if phone_match else "N/A"
    name_match = re.search(r'(?:\.\s+|\s+)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', text)
    name = name_match.group(1) if name_match else "Cliente"
    
    return name, email, phone

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line: continue
            
            name, email, phone = extract_info(line)
            
            payload = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': line
            }
            
            try:
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 200:
                    print(f"✅ Success: {name} | {email} | {phone}")
                else:
                    print(f"⚠️ Error: {name}")
                time.sleep(1.5)
            except Exception as e:
                print(f"❌ Error: {e}")

process_file('conversas.txt')