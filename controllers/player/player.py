from app import app
import json
from flask import request, jsonify


class Purchase:
    def __init__(self, appChargePaymentId, purchaseDateAndTimeUtc, gameId, playerId, bundleName, bundleId, sku, priceInCents, currency, priceInDollar, action, actionStatus, products, publisherToken, price):
        self.appChargePaymentId = appChargePaymentId
        self.purchaseDateAndTimeUtc = purchaseDateAndTimeUtc
        self.gameId = gameId
        self.playerId = playerId
        self.bundleName = bundleName
        self.bundleId = bundleId
        self.sku = sku
        self.priceInCents = priceInCents
        self.currency = currency
        self.priceInDollar = priceInDollar
        self.price = price
        self.action = action
        self.actionStatus = actionStatus
        self.products = products
        self.publisherToken = publisherToken


@app.route('/updateBalance', methods=['POST'])
def update_balance():
    purchase = Purchase(**request.data)
    
    print(request.data)

    # TODO
    # Here goes your piece of code that is responsible for handling player update balance requests coming from appcharge systems

    return jsonify({
        # TODO change the <PURCHASE-ID> with a real purchase ID
        "publisherPurchaseId": "<PURCHASE-ID>"
    })