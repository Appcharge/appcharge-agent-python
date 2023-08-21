import json
import os
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from werkzeug.wrappers import Request
from signature_service import SignatureService
from werkzeug.exceptions import HTTPException


key = os.getenv('KEY')
APP_SECRET = os.getenv('APP_SECRET')

# Check IV and KEY exists
if key is None or APP_SECRET is None:
    print('Missing KEY/APP_SECRET environment variable')
    exit()

signature_service = SignatureService(key)
app = Flask(__name__)

from controllers.player.player import *
from controllers.auth.auth import *


@app.before_request
def decrypted_body():
    signature_header = request.headers.get('signature', '')
    data = request.data
    if not signature_service.check_signature(data, signature_header):
        raise Exception(f'Wrong signature')
    request.data = json.loads(data)


@app.errorhandler(Exception)
def bad_request(error):
    print('Error:', error)
    print(str(error))
    return f'Bad Request: {str(error)}', 400
