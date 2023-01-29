import os

import nacl.secret

from vkv.repository import get_key_path, create_box, get_keys


def test_if_private_key_exists():
    assert os.path.isfile(get_key_path(0))


def test_if_secret_file_exists():
    assert os.path.isfile(get_key_path(1))


def test_if_box_is_a_secret_box():
    assert isinstance(create_box(), nacl.secret.SecretBox)


def test_decrypted_key_file_is_a_dictionary():
    assert isinstance(get_keys(), dict)
