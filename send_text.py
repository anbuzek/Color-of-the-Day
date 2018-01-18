from twilio.rest import Client
import os
import random

# Your Account SID from twilio.com/console
myArray = []

with open("/Users/pblack/code/sandbox/aaron/Color-of-the-Day/color_list.txt","r",encoding='utf-8', errors='ignore') as f:
        for line in f:

            if not line.strip():
                pass
            else:
                myArray.append(line.rstrip('\r\n'))

# Your Auth Token from twilio.com/console
auth_token  = "72c384d70e619a8a5b07fa420bc8a527"
account_sid = "ACe78878762b0fefe6f0896c396683f833"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17039288450",
    from_="+12028167494",
    body=random.choice(myArray)
    )

print(message.sid)
