import os
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from werkzeug.wrappers import Request
from decryptor_service import DecryptorService
from werkzeug.exceptions import HTTPException

iv = os.getenv('IV')
key = os.getenv('KEY')
APP_SECRET = os.getenv('APP_SECRET')

# Check IV and KEY exists
if iv is None or key is None or APP_SECRET is None:
    print("Missing IV/KEY/APP_SECRET environment variable")
    exit()

decryptor = DecryptorService(iv, key)
app = Flask(__name__)

from controllers.player.player import *
from controllers.auth.auth import *


@app.before_request
def decrypted_body():
    encrypted = bytes(bytearray.fromhex(request.data.decode('ascii')))
    decrypted = decryptor.decrypt(encrypted)
    request.data = json.loads(decrypted)


@app.errorhandler(Exception)
def bad_request(error):
    print('Error:', error)
    print(str(error))
    return 'Bad Request', 400
