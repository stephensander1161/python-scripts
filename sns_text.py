#lambda

from twilio.rest import Client 

def send(event=None, context=None):
    
    # Define your body 
    my_body='EC2 Instance Stopped Working '
    # define client 
    client = Client('ACCOUNT SSID','SECRET')
    client.messages.create(to='+YOUR PHONE ',
    from = '+TWILIO NUMBER ',
    body=my_body)

    return "Sent Message"