from functools import partial
from typing import Dict, Generator, List, Tuple

from tqdm import tqdm

from .common import (
    LOOKUP_TABLE,
    MULTIPLICATION_BY_2,
    MULTIPLICATION_BY_3,
    MULTIPLICATION_BY_9,
    MULTIPLICATION_BY_11,
    MULTIPLICATION_BY_13,
    MULTIPLICATION_BY_14,
    REVERSE_S_BOX,
    S_BOX,
    State,
)
from .first_step import get_keys


def reduce_key_space(
    normal_state: State, faulty_state: State, equations: List[Dict[int, List[int]]]
) -> Generator[bytes, None, None]:
    _get_valid_keys_for_state = partial(_get_valid_keys, normal_state, faulty_state)
    for valid_keys in tqdm(map(_get_valid_keys_for_state, equations), total=len(equations)):
        yield from valid_keys


def _get_valid_keys(normal_state: State, faulty_state: State, equation: Dict[int, List[int]]) -> List[bytes]:
    valid_keys = []
    for key in get_keys(equation):
        _, is_valid = _is_valid_guess(normal_state, faulty_state, key)
        if is_valid:
            valid_keys.append(key)
    return valid_keys


def _is_valid_guess(normal_state: State, faulty_state: State, key: bytes) -> Tuple[bytes, bool]:
    fault = _compute_second_step_2(normal_state, faulty_state, key)
    if _compute_second_step_3(normal_state, faulty_state, key) != fault:
        return key, False
    elif _compute_second_step_1(normal_state, faulty_state, key) != MULTIPLICATION_BY_2[fault]:
        return key, False
    elif _compute_second_step_4(normal_state, faulty_state, key) != MULTIPLICATION_BY_3[fault]:
        return key, False
    return key, True


def _compute_second_step_1(normal_state: State, faulty_state: State, key: bytes) -> int:
    a = _compute_second_step_1_for_state(normal_state, key)
    b = _compute_second_step_1_for_state(faulty_state, key)
    return a ^ b


def _compute_second_step_2(normal_state: State, faulty_state: State, key: bytes) -> int:
    a = _compute_second_step_2_for_state(normal_state, key)
    b = _compute_second_step_2_for_state(faulty_state, key)
    return a ^ b


def _compute_second_step_3(normal_state: State, faulty_state: State, key: bytes) -> int:
    a = _compute_second_step_3_for_state(normal_state, key)
    b = _compute_second_step_3_for_state(faulty_state, key)
    return a ^ b


def _compute_second_step_4(normal_state: State, faulty_state: State, key: bytes) -> int:
    a = _compute_second_step_4_for_state(normal_state, key)
    b = _compute_second_step_4_for_state(faulty_state, key)
    return a ^ b


def _compute_second_step_1_for_state(state: State, key: bytes) -> int:
    a00 = REVERSE_S_BOX[state[0, 0] ^ key[0]]
    a01 = key[0] ^ S_BOX[key[13] ^ key[9]] ^ LOOKUP_TABLE[10]
    a02 = MULTIPLICATION_BY_14[a00 ^ a01]

    a10 = REVERSE_S_BOX[state[1, 3] ^ key[13]]
    a11 = key[1] ^ S_BOX[key[14] ^ key[10]]
    a12 = MULTIPLICATION_BY_11[a10 ^ a11]

    a20 = REVERSE_S_BOX[state[2, 2] ^ key[10]]
    a21 = key[2] ^ S_BOX[key[15] ^ key[11]]
    a22 = MULTIPLICATION_BY_13[a20 ^ a21]

    a30 = REVERSE_S_BOX[state[3, 1] ^ key[7]]
    a31 = key[3] ^ S_BOX[key[12] ^ key[8]]
    a32 = MULTIPLICATION_BY_9[a30 ^ a31]

    return REVERSE_S_BOX[a02 ^ a12 ^ a22 ^ a32]


def _compute_second_step_2_for_state(state: State, key: bytes) -> int:
    a00 = REVERSE_S_BOX[state[0, 3] ^ key[12]]
    a01 = key[12] ^ key[8]
    a02 = MULTIPLICATION_BY_9[a00 ^ a01]

    a10 = REVERSE_S_BOX[state[1, 2] ^ key[9]]
    a11 = key[9] ^ key[13]
    a12 = MULTIPLICATION_BY_14[a10 ^ a11]

    a20 = REVERSE_S_BOX[state[2, 1] ^ key[6]]
    a21 = key[14] ^ key[10]
    a22 = MULTIPLICATION_BY_11[a20 ^ a21]

    a30 = REVERSE_S_BOX[state[3, 0] ^ key[3]]
    a31 = key[15] ^ key[11]
    a32 = MULTIPLICATION_BY_13[a30 ^ a31]

    return REVERSE_S_BOX[a02 ^ a12 ^ a22 ^ a32]


def _compute_second_step_3_for_state(state: State, key: bytes) -> int:
    a00 = REVERSE_S_BOX[state[0, 2] ^ key[8]]
    a01 = key[8] ^ key[4]
    a02 = MULTIPLICATION_BY_13[a00 ^ a01]

    a10 = REVERSE_S_BOX[state[1, 1] ^ key[5]]
    a11 = key[9] ^ key[5]
    a12 = MULTIPLICATION_BY_9[a10 ^ a11]

    a20 = REVERSE_S_BOX[state[2, 0] ^ key[2]]
    a21 = key[10] ^ key[6]
    a22 = MULTIPLICATION_BY_14[a20 ^ a21]

    a30 = REVERSE_S_BOX[state[3, 3] ^ key[15]]
    a31 = key[11] ^ key[7]
    a32 = MULTIPLICATION_BY_11[a30 ^ a31]

    return REVERSE_S_BOX[a02 ^ a12 ^ a22 ^ a32]


def _compute_second_step_4_for_state(state: State, key: bytes) -> int:
    a00 = REVERSE_S_BOX[state[0, 1] ^ key[4]]
    a01 = key[4] ^ key[0]
    a02 = MULTIPLICATION_BY_11[a00 ^ a01]

    a10 = REVERSE_S_BOX[state[1, 0] ^ key[1]]
    a11 = key[5] ^ key[1]
    a12 = MULTIPLICATION_BY_13[a10 ^ a11]

    a20 = REVERSE_S_BOX[state[2, 3] ^ key[14]]
    a21 = key[6] ^ key[2]
    a22 = MULTIPLICATION_BY_9[a20 ^ a21]

    a30 = REVERSE_S_BOX[state[3, 2] ^ key[11]]
    a31 = key[7] ^ key[3]
    a32 = MULTIPLICATION_BY_14[a30 ^ a31]

    return REVERSE_S_BOX[a02 ^ a12 ^ a22 ^ a32]
