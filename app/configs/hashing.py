from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def encrypt(psw: str):
        return pwd_context.hash(psw)
    
    @staticmethod
    def verify(hashed, plain):
        return pwd_context.verify(plain, hashed)