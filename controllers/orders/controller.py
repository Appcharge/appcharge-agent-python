from app import app
from flask import request, jsonify

from controllers.orders.schemas import GetOrdersRequestSchema, GetOrdersResponseSchema
from controllers.orders.service import OrdersService


@app.route("/mocker/orders", methods=["POST"])
def get_orders():
    GetOrdersRequestSchema.model_validate_json(request.data)
    orders_service = OrdersService()
    orders = orders_service.get_orders(request.data)
    GetOrdersResponseSchema.model_validate(orders)
    return jsonify(orders)
