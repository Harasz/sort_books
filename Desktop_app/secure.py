# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random
import base64


class Secure(object):

    public_key = None
    private_key = None
    other_key = None

    def __init__(self):
        self._generate_key()


    def _generate_key(self):
        self.private_key = RSA.generate(1024, Random.new().read)
        self.public_key = self.private_key.publickey()


    def get_public(self):
        return self.public_key.exportKey().decode()


    def decrypt_(self, data):
        if isinstance(data, list):
            i = 0
            for value in data:
                data[i] = self.decrypt_(value).decode()
                i += 1
            return data
        else:
            return self.private_key.decrypt(base64.b64decode(data.encode()))


    def encrypt_(self, data):
        data = self.other_key.encrypt(data.encode(), 32)
        return base64.b64encode(data[0]).decode()


    def load_other_key(self, data):
        self.other_key = RSA.importKey(data)


    def encode_data(self, data):
        for key, value in data.items():
            if value is not None:
                data[key] = self.decrypt_(value)
        return data
