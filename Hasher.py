import argon2

class Hasher():
    @staticmethod
    def hash_password(password):
        salt = 'THATSMYSECRETKEYHAHAHA25'
        return argon2.argon2_hash(password,salt)