import os
import json
from app import app

from flask import jsonify
from config.settings import get_settings
from controllers.offers.schemas import (
    CreateOfferRequest,
    CreatePopUpOfferRequest,
    UpdateOfferRequest,
    UpdatePopUpOfferRequest,
)
from controllers.offers.service import OffersService

from signature_service import SignatureService
from utils.file import read_json_file


@app.route("/mocker/offer", methods=["POST"])
def create_offer():
    offers_file = read_json_file(
        os.path.abspath(os.path.join(os.getcwd(), get_settings().OFFERS_FILE_PATH))
    )
    create_offer_data = offers_file["create"]
    json_str = json.dumps(create_offer_data, separators=(",", ":"))
    byte_string = json_str.encode("utf-8")
    CreateOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    analytics = offers_service.create_offer(byte_string)
    return jsonify(analytics)


@app.route("/mocker/offer", methods=["PUT"])
def update_offer():
    offers_file = read_json_file(
        os.path.abspath(os.path.join(os.getcwd(), get_settings().OFFERS_FILE_PATH))
    )
    update_offer_data = offers_file["update"]
    json_str = json.dumps(update_offer_data, separators=(",", ":"))
    byte_string = json_str.encode("utf-8")
    UpdateOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    analytics = offers_service.update_offer(
        update_offer_data["publisherOfferId"],
        byte_string,
    )
    return jsonify(analytics)


@app.route("/mocker/offer/popup/daily-bonus", methods=["POST"])
def create_popUp():
    popups_file = read_json_file(
        os.path.abspath(os.path.join(os.getcwd(), get_settings().POPUPS_FILE_PATH))
    )
    create_offer_data = popups_file["create"]
    json_str = json.dumps(create_offer_data, separators=(",", ":"))
    byte_string = json_str.encode("utf-8")
    CreatePopUpOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    analytics = offers_service.create_popup(byte_string)
    return jsonify(analytics)


@app.route("/mocker/offer/popup/daily-bonus", methods=["PUT"])
def update_popUp():
    popups_file = read_json_file(
        os.path.abspath(os.path.join(os.getcwd(), get_settings().POPUPS_FILE_PATH))
    )
    update_offer_data = popups_file["update"]
    json_str = json.dumps(update_offer_data, separators=(",", ":"))
    byte_string = json_str.encode("utf-8")
    UpdatePopUpOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    analytics = offers_service.update_popup(
        update_offer_data["publisherOfferId"],
        byte_string,
    )
    return jsonify(analytics)
