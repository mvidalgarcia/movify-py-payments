__author__ = 'mvidalgarcia'

import hashlib
from flask import Flask, render_template, request
app = Flask(__name__)

# Commerce Data
commerce_data = {
    "MERCHANT_ID": "082108630",
    "ACQUIRER_BIN": "0000554002",
    "TERMINAL_ID": "00000003",
    "CLAVE_ENCRIPTACION": "87401456",
    "TIPO_MONEDA" :"978",
    "EXPONENTE": "2",
    "URL_OK": "http://www.ceca.es",
    "URL_ERROR": "http://www.ceca.es"
}


@app.route("/")
def index():
    return "Index"


@app.route("/pay", methods=['GET', 'POST'])
def pay():
    error = None
    if request.method == 'POST':
        # Get values and compute digital signature
        operation = request.form['operation']
        price = request.form['price']
        print('Operation:', operation)
        print('Price:', price)
        return render_template('pay.html', error=error,
                               commerce_data=commerce_data,
                               numeroOperacion=operation,
                               importe=price,
                               firma=compute_signature(operation, price))
    return render_template('index.html')


def compute_signature(operation, price):
    message = commerce_data["CLAVE_ENCRIPTACION"] +\
              commerce_data["MERCHANT_ID"] +\
              commerce_data["ACQUIRER_BIN"] +\
              commerce_data["TERMINAL_ID"] +\
              operation +\
              price +\
              commerce_data["TIPO_MONEDA"] +\
              commerce_data["EXPONENTE"] +\
              "" +\
              "SHA1" +\
              commerce_data["URL_OK"] +\
              commerce_data["URL_ERROR"]
    print("Message:", message)
    my_sha = hashlib.sha1()
    print("MessageEncoded:", str.encode(message))
    my_sha.update(str.encode(message))
    print("MessageSHA:", my_sha)
    digest = my_sha.digest()
    print("MessageDigest:", digest)
    # Convert to hex string
    return ''.join('{:02x}'.format(x) for x in digest)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # TODO Not debug mode in production!