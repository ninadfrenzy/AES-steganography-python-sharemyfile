import AESify as aes
import STEGOfy as stego
import binascii
import os
import sqlite3 as sql
def create_and_store_keys():
    connection = sql.connect('keystore.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS KEYS(KEYNAME TEXT,KEYHASH TEXT);''')
    obj = cursor.execute('SELECT COUNT(*) FROM KEYS')
    if(obj.fetchone()[0] == 0):
        for num in range(480000, 480100):
            keyvalue = str(num)
            keyhash = aes.get_hash(keyvalue)
            dbitem = (keyvalue,keyhash,)
            cursor.execute('INSERT INTO KEYS VALUES(?,?)', dbitem)
    connection.commit()
    connection.close()

def encrypt_and_write(_message, _key, _imagepath, newpath=''):
    encrypted_message = aes.encrypt_AES_GCM(_message.encode('utf-8'), _key)
    # print(binascii.unhexlify((binascii.hexlify(encrypted_message[0])).decode('utf-8').encode('utf-8')) == encrypted_message[0])
    inputFile = open('input.txt', 'w')
    for item in encrypted_message:
        inputFile.write(binascii.hexlify(item).decode('utf-8'))
        inputFile.write('\n')
    inputFile.close()
    stego.hide_message('input.txt', _imagepath)
    if(newpath != ''):
        os.replace("new.png", newpath+"/encrypted_image.png")
    

def read_and_decrypt(_key, _imagepath):
    stego.extract_message(_imagepath)
    opFile = open('hidden_file.txt', 'r')
    data = list()
    for line in opFile:
        if(len(line)>1):
            data.append(binascii.unhexlify(line.strip('\n').encode('utf-8')))
    os.remove('hidden_file.txt')
    return (aes.decrypt_AES_GCM(tuple(data), _key).decode('utf-8'))
# while(True):
#     choice = int(input('1.HIDE AN ENCRYPTED MESSAGE IN IMAGE\n2.EXTRACT AND DECRYPT MESSAGE FROM IMAGE\n3.EXIT'))
#     if(choice == 1):
#         print('ensure new.png does not exist in current directory else it will be overwritten')
#         message = input('Enter the secret message to hide\n')
#         key = input('enter the password to encrypt it\n')
#         img_path = input('enter the path to the image\n')
#         if(os.path.isfile(img_path)):
#             encrypt_and_write(message, key)
#             if(os.path.isfile('new.png')):
#                 print('<existing new.png found! overwriting it now>')
#             stego.hide_message('input.txt', img_path)
#             print('SUCCESS\n')
#         else:
#             print('No file found\n')
        
#     elif(choice == 2):
#         print('<rename your file to new.png and run this command>')
#         key = input('enter your password to decrypt\n')
#         if(os.path.isfile('hidden_file.txt')):
#             os.remove('hidden_file.txt')
#         if(os.path.isfile('new.png')):
#             stego.extract_message('new.png')
#             extracted = read_and_decrypt(key)
#             print('message extracted - ', extracted.decode('utf-8'))
#         else:
#             print('no file named new.png found! make sure you follow steps correctly\n')
#     else:
#         break
