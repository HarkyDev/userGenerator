import email
import random
import string
import json

names = json.loads(open('names.json').read())

for name in names:
    extra = ''.join(random.choice(string.digits) for _ in range(6))
    username = name.lower()
    emailLink = ['@gmail.com', '@yahoo.com', '@hotmail.com','@hotmail.co.uk', '@outlook.co.uk', '@outlook.com']
    emailLink = random.choice(emailLink)
    email = username + extra + emailLink
    password = extra

    def object():
     d = dict()
     d['username'] = username
     d['email'] = email
     d['password'] = password
     return d
    print(json.dumps(object()))

    f = open("demofile.txt", "a")
    f.write(json.dumps(object()) + "\n")
    f.close()

    f = open("demofile.txt", "r")
    print(f.read())

    


