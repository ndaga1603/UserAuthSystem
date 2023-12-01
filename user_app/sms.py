import africastalking
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Africa's Talking

africastalking.initialize(
    username=os.environ.get("AFRICASTALKING_USERNAME"),
    api_key=os.environ.get("AFRICASTALKING_API_KEY"),
)


class SendSMS:
    """This class is used to send sms to the user"""

    def __init__(self, recipient, code):
        self.sms = africastalking.SMS
        self.recipient = [recipient]
        self.code  = code

    def sending(self, user):
        """This method is used to send sms to the user. The type is used to determine the type of sms to send
        """
        message = f"Hello {user}! Your verification code is {self.code }"
        sender = "2711"

        try:
            response = self.sms.send(message, self.recipient)
            print(response)
        except Exception as e:
            print(f"Error!. {e}")
