from django.db import models
from utils.models import BaseModel
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad


class Product(BaseModel):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    marja = models.DecimalField(max_digits=10, decimal_places=3)
    package_code = models.CharField(max_length=32)
    encrypted_price = models.BinaryField()
    encrypted_marja = models.BinaryField()
    encrypted_code = models.BinaryField()

    def __str__(self):
        return self.title

    @staticmethod
    def generate_key(password, salt_length=16):
        salt = get_random_bytes(salt_length)
        key = PBKDF2(password, salt, dkLen=32)
        return key

    @staticmethod
    def encrypt_data(key, data):
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
        return cipher.iv + ciphertext

    @staticmethod
    def decrypt_data(key, encrypted_data):
        iv = encrypted_data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data[AES.block_size:])
        return unpad(decrypted_data, AES.block_size).decode()

    def save(self, *args, **kwargs):
        password = b'12345678'
        key = self.generate_key(password)

        encrypted_data1 = self.encrypt_data(key, self.encrypted_price)
        self.encrypted_price = encrypted_data1

        encrypted_data2 = self.encrypt_data(key, self.encrypted_marja)
        self.encrypted_marja = encrypted_data2

        encrypted_data3 = self.encrypt_data(key, self.encrypted_code)
        self.encrypted_code = encrypted_data3

        super().save(*args, **kwargs)

    def decrypted_field1(self):
        password = b'12345678'
        key = self.generate_key(password)
        return self.decrypt_data(key, self.encrypted_price)

    def decrypted_field2(self):
        password = b'12345678'
        key = self.generate_key(password)
        return self.decrypt_data(key, self.encrypted_marja)

    def decrypted_field3(self):
        password = b'12345678'
        key = self.generate_key(password)
        return self.decrypt_data(key, self.encrypted_code)
