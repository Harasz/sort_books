# -*- coding: utf-8 -*-

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64


class Secure(object):

	public_key = None
	private_key = None
	other_key = None

	def __init__(self):
		self._generate_key()


	def _generate_key(self):
		self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
		self.public_key = self.private_key.public_key()


	def get_private(self):
		return self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
											  format=serialization.PrivateFormat.PKCS8,
											  encryption_algorithm=serialization.NoEncryption())


	def get_public(self):
		return self.private_key.public_key().public_bytes(encoding=serialization.Encoding.PEM,
														  format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()


	def _decrypt(self, data):
		return self.private_key.decrypt(base64.b64decode(data),
										padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),
													 algorithm=hashes.SHA512(),
													 label=None)
										)


	def _encrypt(self, data, key):
		print(key)
		key = serialization.load_pem_public_key(key, default_backend())
		self.get_keya(key)
		data = key.encrypt(data,
						   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),
						   algorithm=hashes.SHA512(),
						   label=None)
						   )
		return base64.b64encode(data)

	def get_keya(self, key):
		print(key.public_bytes(encoding=serialization.Encoding.PEM,
							   format=serialization.PublicFormat.SubjectPublicKeyInfo))
