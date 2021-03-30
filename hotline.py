import os
from flask import Flask, request
import telnyx
from dotenv import load_dotenv

load_dotenv()

telnyx.api_key = os.environ['TELNYX_API_KEY']
TELNYX_SMS_NUMBER = os.environ['TELNYX_SMS_NUMBER']

PREPARED_REPLIES = {
    'pizza': 'Chicago pizza is the best',
    'ice cream': 'I prefer gelato'
}
DEFAULT_REPLY = "Please send either the word 'pizza' or 'ice cream' for a different response"

app = Flask(__name__)


@app.route('/webhooks', methods=['POST'])
def webhooks():
    try:
        process_webhook(request.json)
    except Exception as e:
        print("Exception raised:", e)
    finally:
        return '', 200


def process_webhook(json_body):
    event_type = json_body['data']['event_type']
    payload = json_body['data']['payload']
    msg_direction = payload['direction']

    if event_type == 'message.received' and msg_direction == 'inbound':
        sms_message = ' '.join(payload['text'].split()).lower()
        reply_to_number = payload['from']['phone_number']
        prepared_reply = PREPARED_REPLIES.get(sms_message, DEFAULT_REPLY)

        telnyx.Message.create(
            from_=TELNYX_SMS_NUMBER,
            to=reply_to_number,
            text=prepared_reply
        )


if __name__ == "__main__":
    app.run(port=5000)
