import email
import random
import string
import json

names = json.loads(open('names.json').read())

for name in names:
    extra = ''.join(random.choice(string.digits) for _ in range(6))
    username = name.lower()
    email = username + extra + '@gmail.com'

    print("Username:",username," Email:" , email)