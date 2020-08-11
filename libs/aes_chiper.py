# coding=utf-8

import base64
import hashlib
from Crypto.Cipher import AES


class AESCipher(object):

    @classmethod
    def encrypt(cls, text, key="landsljklandsljk"):
        vi = '0102030405060708'
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        pad_data = pad(text)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
        encrypted_bytes = cipher.encrypt(pad_data.encode('utf8'))
        encode_str = base64.b64encode(encrypted_bytes)
        enc_text = encode_str.decode('utf8')
        return enc_text

    @classmethod
    def decrypt(cls, text, key="landsljklandsljk"):
        vi = '0102030405060708'
        encode_data = text.encode('utf8')
        encode_bytes = base64.decodebytes(encode_data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
        text_decrypted = cipher.decrypt(encode_bytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted


# md5签名
def md5sign(sign_data):
    sign_result = hashlib.md5(str(sign_data)).hexdigest()
    return sign_result.upper()


if __name__ == '__main__':
    print(AESCipher.encrypt("12345678"))
    print(AESCipher.decrypt(AESCipher.encrypt("12345678")))
