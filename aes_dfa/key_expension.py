from typing import List

from .common import LOOKUP_TABLE, S_BOX

Word = bytes


def key_expension(key: bytes, rounds: int) -> List[Word]:
    if len(key) != 16:
        raise ValueError(f"Wrong key length: {len(key)}")
    expended_key = [key[i : i + len(key) // 4] for i in range(0, len(key), 4)]
    for r in range(1, rounds):
        rot = _rot_word(expended_key[-1])
        sub = _sub_word(rot)
        xored = _xor(sub, expended_key[-4])
        first_column = _xor(xored, _r_con(r))
        expended_key.append(first_column)
        for _ in range(3):
            expended_key.append(_xor(expended_key[-1], expended_key[-4]))
    return expended_key


def get_first_key(key: bytes, rounds: int) -> bytes:
    if len(key) != 16:
        raise ValueError(f"Wrong key length: {len(key)}")
    expended_key = [key[i : i + len(key) // 4] for i in range(0, len(key), 4)]
    fully_expended_key = reverse_key_expension(expended_key, rounds)
    return b"".join(fully_expended_key[:4])


def reverse_key_expension(expended_key: List[Word], rounds: int) -> List[Word]:
    for r in reversed(range(1, rounds)):
        for _ in range(3):
            expended_key.insert(0, _xor(expended_key[2], expended_key[3]))
        rot = _rot_word(expended_key[2])
        sub = _sub_word(rot)
        xored = _xor(expended_key[3], _r_con(r))
        first_column = _xor(xored, sub)
        expended_key.insert(0, first_column)
    return expended_key


def _rot_word(word: Word) -> Word:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return word[1:] + bytes([word[0]])


def _sub_word(word: Word) -> Word:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return bytes([S_BOX[b] for b in word])


def _r_con(n: int) -> Word:
    if not 0 <= n < 256:
        raise ValueError(f"Wrong n: {n}")
    return bytes([LOOKUP_TABLE[n], 0, 0, 0])


def _xor(w1: Word, w2: Word) -> Word:
    return bytes([i ^ j for i, j in zip(w1, w2)])
