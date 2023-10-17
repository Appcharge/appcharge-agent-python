import os

from app import app
from flask import request, jsonify
from controllers.player.schemas import PlayerInfoSyncRequest, PlayerUpdateBalanceRequest
from controllers.player.service import PlayerService
from signature_service import SignatureService

from utils.file import read_json_file
from config.settings import get_settings


@app.route('/mocker/playerInfoSync', methods=['POST'])
def sync_info():
    PlayerInfoSyncRequest.model_validate_json(request.data)
    player_file = read_json_file(os.path.abspath(os.path.join(os.getcwd(), get_settings().PLAYER_DATASET_FILE_PATH)))
    return jsonify(player_file)


@app.route('/mocker/playerUpdateBalance', methods=['PUT'])
def update_balance():
    PlayerUpdateBalanceRequest.model_validate_json(request.data)
    player_service = PlayerService()
    signature_service = SignatureService()
    update_balance_response = player_service.update_balance(request.data,
                                                            signature_service.create_signature(request.data))
    return jsonify(update_balance_response)
