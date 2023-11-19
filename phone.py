from twilio.rest import Client
account_sid = 'AC216734b0fbf005bbb3fa1212d37c0c60'
auth_token = 'ceb4e0576c6c41e0f9c1b59d77400222'
client = Client(account_sid, auth_token)
message = client.messages.create(
        from_='+14078095824',
        body="It 's going to rain today.Remember to take umbrella ☂",
        to='+918078024037')
print(message.status)
