import binascii
from typing import Generator, List

import numpy as np

from .common import State
from .first_step import get_all_possible_keys
from .key_expension import get_first_key
from .second_step import reduce_key_space


def attack(normal_cipher_text: str, faulty_cipher_text: str) -> List[str]:
    normal_state = _get_state(binascii.unhexlify(normal_cipher_text))
    faulty_state = _get_state(binascii.unhexlify(faulty_cipher_text))
    possible_keys = []
    for last_key in get_last_keys(normal_state, faulty_state):
        original_key = get_first_key(last_key, 11)
        original_key_str = binascii.hexlify(original_key).decode()
        possible_keys.append(original_key_str)
    return possible_keys


def get_last_keys(normal_state: State, faulty_state: State) -> Generator[bytes, None, None]:
    print("[ ] Computing all possible keys...")
    equations = get_all_possible_keys(normal_state, faulty_state)
    print("[ ] Reducing key space...")
    yield from reduce_key_space(normal_state, faulty_state, equations)
    print("[+] Finished !")


def _get_state(cipher_text: bytes) -> State:
    if len(cipher_text) != 16:
        raise ValueError(f"Wrong cipher_text length: {len(cipher_text)}")
    a = np.array(list(cipher_text), dtype=int)
    return a.reshape((4, 4), order="F")
