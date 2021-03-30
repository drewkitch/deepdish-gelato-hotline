### The Deep Dish / Gelato Hotline

#### Requirements

- python 3.9.2 or higher

#### Setup

- [Create a Telnyx account](https://telnyx.com/sign-up)
- [Purchase a phone number from the Telnyx portal](https://portal.telnyx.com/#/app/numbers/buy-numbers)
- Run `cp .sample-env .env` in the project directory and proceed to record phone number in the `.env` file
- Record your [Telynx API Key](https://portal.telnyx.com/#/app/api-keys) in the `.env` file as well
- Run `pip install -r requirements`
- Start up the Flask app with the following command -- `python hotline.py`
- Sign up for a free account at [ngrok](https://ngrok.com/) to receive webhooks from Telnyx to your locally running Flask app.
- Follow instructions to install and run ngrok tool from local machine, replacing the port value from `80` to `5000` (the port our Flask app is listening on).
- Once the ngrok process is running, note the forwarding https address (e.g., https://4f7e5039ecb9.ngrok.io) and update your [Telnyx Messaging Profile](https://portal.telnyx.com/#/app/messaging). Set the Inbound Settings to "Send a webhook to this URL" with the recorded forwarding url along with the webhooks path appended (e.g., https://4f7e5039ecb9.ngrok.io/webhooks).
- Save the changes to the messaging profile. You should now be able to send texts to your Telnyx phone number and receive a response from the locally running Flask app.
