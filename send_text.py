# When you import something, you are
from twilio.rest import Client
from dotenv import load_dotenv
from random import choice
from os import path, environ

def get_twilio_client():
    # Get the path to the current directory
    app_dir = path.dirname(__file__)

    # The dotenv library will look for the file passed in and load these variables into the environment
    # Ask about what the environment and environment variables are!
    load_dotenv("".join([app_dir, ".env"]))

    auth_token = environ.get('AUTH_TOKEN')
    account_sid = environ.get('ACCOUNT_SID')

    client = Client(account_sid, auth_token)

    return client

def parse_color_file():
    colors = []
    with open("/Users/pblack/code/sandbox/aaron/Color-of-the-Day/color_list.txt","r",encoding='utf-8', errors='ignore') as f:
            for line in f:

                if not line.strip():
                    pass
                else:
                    colors.append(line.rstrip('\r\n'))

    return colors


def send_text(client,random_color):
    message = client.messages.create(
        to="+17039288450",
        from_="+12028167494",
        body=random_color
        )

colors = parse_color_file()
client = get_twilio_client()
send_text(client, choice(colors))
