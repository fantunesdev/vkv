import os

import nacl.secret

from vkv.repository import get_key_path, create_box


def test_if_private_key_exists():
    assert os.path.isfile(get_key_path(0))


def test_if_secret_file_exists():
    assert os.path.isfile(get_key_path(1))


def test_if_box_is_a_secret_box():
    assert type(create_box()) == nacl.secret.SecretBox
