# pip install requests
import requests
import time
before = time.time()
response = requests.get("https://www.google.com/?safe=active&ssui=on")
after = time.time()
print(f'Google: The difference is {after-before}')

before = time.time()
response = requests.get("https://www.chat-gpt-israel.com/")
after = time.time()
print(f'ChatGPT: The difference is {after-before}')

before = time.time()
response = requests.get("https://www.instagram.com/")
after = time.time()
print(f'Instagram: The difference is {after-before}')

before = time.time()
response = requests.get("https://www.reddit.com/")
after = time.time()
print(f'Reddit: The difference is {after-before}')
