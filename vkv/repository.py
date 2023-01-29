import ast
import os

import nacl.secret


def create_box():
    with open('vkv.conf', 'r') as kd_file:
        key_path = kd_file.readlines()[0].split('\n')[0]
        kd_file.close()
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
        key_file.close()
    return nacl.secret.SecretBox(key)


def set_env():
    box = create_box()
    with open('vkv.conf', 'r') as kd_file:
        key_path = kd_file.readlines()[1].split('\n')[0]
        kd_file.close()
    with open(key_path, 'rb') as crypt_file:
        encrypted_data = crypt_file.read()
        crypt_file.close()
    data = box.decrypt(encrypted_data).decode()
    keys = ast.literal_eval(data)
    os.environ['URL'] = keys['url']
    os.environ['TOKEN'] = keys['token']
