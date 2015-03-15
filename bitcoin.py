__author__ = 'mvidalgarcia'

import requests


def bitcoin_payment(return_url, notify_url, notify_email, price, customer_name, order_number, customer_email):
    # Payment Request
    print('Payment Request')

    values = """
      {
        "settled_currency": "BTC",
        "return_url": "http://your-e-shop.com/thank-your-for-your-order",
        "notify_url": "https://your-e-shop.com/order-received",
        "notify_email": "order-received@your-e-shop.com",
        "price": 0.9,
        "currency": "BTC",
        "reference": {
          "customer_name": "Marco",
          "order_number": 111,
          "customer_email": "customer@example.com"
        }
      }
    """

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token fmzGW06lF3hQAqPZyAY8dymz'
    }

    url = 'https://private-anon-2b8feed1a-bitcoinpaycom.apiary-proxy.com/api/v1/payment/btc'

    response = requests.post(url, data=values, headers=headers)
    if response.status_code == 200:
        payment_id = response.json()['data']['payment_id']
        payment_url = response.json()['data']['payment_url']
        print(response.text)
        print('Payment URL:', payment_url)
        return payment_id


def bitcoin_payment_check(payment_id):
    # Check Payment Status

    print('Check Payment Status')

    headers = {
      'Authorization': 'Token fmzGW06lF3hQAqPZyAY8dymz'
    }

    url = 'https://private-anon-2b8feed1a-bitcoinpaycom.apiary-proxy.com/api/v1/payment/btc/'+payment_id
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payment_status = response.json()['data']['status']
        print(response.text)
        print(payment_status)

if __name__ == "__main__":

    # Example data
    return_url = "http://your-e-shop.com/thank-your-for-your-order"
    notify_url = "https://your-e-shop.com/order-received"
    notify_email = "order-received@your-e-shop.com"
    price = 0.9
    customer_name = "Movify"
    order_number = 111
    customer_email = "movify@movify.com"

    payment_id = bitcoin_payment(return_url, notify_email, notify_email,
                                 price, customer_name, order_number, customer_email)
    if payment_id is not None:
        print()
        bitcoin_payment_check(payment_id)