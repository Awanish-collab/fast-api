from passlib.context import CryptContext

pw_contxt = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

class Hash:
    def encrypt_password(password: str):
        hashed_password = pw_contxt.hash(password)
        return hashed_password
    
    def verify(plain_password, hashed_password):
        return pw_contxt.verify(plain_password, hashed_password)