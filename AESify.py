from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
    secretKey = get_secret(secretKey)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    secretKey = get_secret(secretKey)
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext
def get_secret(key):
    h = SHA256.new()
    h.update(key.encode('utf-8'))
    return h.digest()
def get_hash(key):
    h = SHA256.new()
    h.update(key.encode('utf-8'))
    return h.hexdigest()
# pwd = input('enter pwd')
# h = SHA256.new()
# h.update(pwd.encode('utf-8'))
# print(h.digest())
# secretKey = h.digest() # 256-bit random encryption key
# print("Encryption key:", binascii.hexlify(secretKey))

# msg = input('Enter a message').encode('utf-8')
# encryptedMsg = encrypt_AES_GCM(msg, secretKey)
# print("encryptedMsg", {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'aesIV': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2])
# })

# decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
# print("decryptedMsg", decryptedMsg)











