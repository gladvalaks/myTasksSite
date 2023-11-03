import argon2

class Hasher():
    salt = 'THATSMYSECRETKEYHAHAHA25'
    @staticmethod
    def hash_password(password):
        return argon2.argon2_hash(password,Hasher.salt)
    @staticmethod
    def compare(password, hashed_password):
        return Hasher.hash_password(password) == hashed_password
