import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
BLOCK_SIZE = 16

class DecryptorService:
    def __init__(self, iv, key):
        self.iv = iv.encode("utf8")
        self.key = key.encode("utf8")

    def decrypt(self, encryptedText):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = unpad(cipher.decrypt(encryptedText), BLOCK_SIZE)
        decrypted_text = decrypted.decode("ascii")
        return decrypted_text.strip()