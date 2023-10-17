import os
import json
from app import app

from flask import jsonify
from config.settings import get_settings
from controllers.offers.schemas import CreateOfferRequest, UpdateOfferRequest
from controllers.offers.service import OffersService

from signature_service import SignatureService
from utils.file import read_json_file


@app.route('/mocker/offer', methods=['POST'])
def create_offer():
    offers_file = read_json_file(os.path.abspath(os.path.join(os.getcwd(), get_settings().OFFERS_FILE_PATH)))
    create_offer_data = offers_file["create"]
    json_str = json.dumps(create_offer_data, separators=(',', ':'))
    byte_string = json_str.encode('utf-8')
    CreateOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    signature_service = SignatureService()
    analytics = offers_service.create_offer(byte_string, signature_service.create_signature(byte_string))
    return jsonify(analytics)


@app.route('/mocker/offer', methods=['PUT'])
def update_offer():
    offers_file = read_json_file(os.path.abspath(os.path.join(os.getcwd(), get_settings().OFFERS_FILE_PATH)))
    update_offer_data = offers_file["update"]
    json_str = json.dumps(update_offer_data, separators=(',', ':'))
    byte_string = json_str.encode('utf-8')
    UpdateOfferRequest.model_validate_json(byte_string)
    offers_service = OffersService()
    signature_service = SignatureService()
    analytics = offers_service.update_offer(update_offer_data["publisherOfferId"], byte_string,
                                            signature_service.create_signature(byte_string))
    return jsonify(analytics)
