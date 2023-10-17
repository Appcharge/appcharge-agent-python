from app import app
from signature_service import SignatureService


@app.before_request
def decrypted_body():
    signature_service = SignatureService()
    signature_header = request.headers.get('signature', '')
    data = request.data
    if not signature_service.check_signature(data, signature_header):
        raise Exception(f'Wrong signature')
    request.data = json.loads(data)
