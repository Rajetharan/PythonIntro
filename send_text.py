from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC828a8f5f48289ffce17e9ef90d41964c"
# Your Auth Token from twilio.com/console
auth_token  = "9b0de2eba91f5890a8c68c90b538a0f5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+443573456788", 
    from_="+447532985434",
    body="Hi!")

print(message.sid)
