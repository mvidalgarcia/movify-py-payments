__author__ = 'mvidalgarcia'

import requests, json


def bitcoin_payment(return_url, notify_url, notify_email, price, customer_name, order_number, customer_email):
    # Payment Request
    print('Payment Request')

    values = {
        'settled_currency': "BTC",
        'return_url': return_url,
        'notify_url': notify_url,
        'notify_email': notify_email,
        'price': price,
        'currency': "BTC",
        'reference': {
            'customer_name': customer_name,
            'order_number': order_number,
            'customer_email': customer_email
        }
    }


    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token fmzGW06lF3hQAqPZyAY8dymz'
    }

    url = 'https://private-anon-2b8feed1a-bitcoinpaycom.apiary-proxy.com/api/v1/payment/btc'
    values = json.dumps(values, ensure_ascii=False)
    response = requests.post(url, data=values, headers=headers)
    print(response.text)
    if response.status_code == 200:
        payment_id = response.json()['data']['payment_id']
        payment_url = response.json()['data']['payment_url']

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
    print(response.text)
    if response.status_code == 200:
        payment_status = response.json()['data']['status']
        print(payment_status)

if __name__ == "__main__":

    # Example data
    my_return_url = "http://your-e-shop.com/thank-your-for-your-order"
    my_notify_url = "https://your-e-shop.com/order-received"
    my_notify_email = "order-received@your-e-shop.com"
    my_price = 0.9
    my_customer_name = "Movify"
    my_order_number = 111
    my_customer_email = "movify@movify.com"

    payment_id = bitcoin_payment(my_return_url, my_notify_url, my_notify_email,
                                 my_price, my_customer_name, my_order_number, my_customer_email)
    if payment_id is not None:
        print()
        bitcoin_payment_check(payment_id)