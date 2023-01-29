import ast
import os

import hvac
import nacl.secret


def get_kv(program: str, key: str):
    set_env()
    url = os.getenv('URL')
    token = os.getenv('TOKEN')
    client = hvac.Client(url=url, token=token)
    value = client.secrets.kv.v1.read_secret(f'{program}/{key}')['data'][f'{key}']
    return value


def create_box():
    key_path = get_key_path(0)
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
        key_file.close()
    return nacl.secret.SecretBox(key)


def get_key_path(path_type: int):
    with open('vkv.conf', 'r') as kd_file:
        key_path = kd_file.readlines()[path_type].split('\n')[0]
        kd_file.close()
    return key_path


def get_keys():
    box = create_box()
    key_path = get_key_path(1)
    with open(key_path, 'rb') as crypt_file:
        encrypted_data = crypt_file.read()
        crypt_file.close()
    data = box.decrypt(encrypted_data).decode()
    return ast.literal_eval(data)


def set_env():
    keys = get_keys()
    os.environ['URL'] = keys['url']
    os.environ['TOKEN'] = keys['token']
