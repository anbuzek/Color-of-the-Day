from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe78878762b0fefe6f0896c396683f833"
# Your Auth Token from twilio.com/console
auth_token  = "72c384d70e619a8a5b07fa420bc8a527"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17039288450",
    from_="+12028167494",
    body="boner pills h")

print(message.sid)
