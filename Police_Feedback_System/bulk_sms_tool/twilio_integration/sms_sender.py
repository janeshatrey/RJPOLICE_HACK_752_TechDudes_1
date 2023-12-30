# sms_sender.py
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

def send_sms(receiver_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            to=receiver_number,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )
        print(f"Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# Example Usage:
# send_sms('+1234567890', 'Hello from Police Feedback System!')
