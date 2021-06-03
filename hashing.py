from jose import jwt


class Token():
    def encode(target: any):
        return jwt.encode(target, 'ocr', algorithm='HS256')

    def decode(token: str):
        return jwt.decode(token, 'ocr', algorithms=['HS256'])
