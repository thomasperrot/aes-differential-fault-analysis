import pytest

from aes_dfa.attack import _get_state
from aes_dfa.key_expension import key_expension
from aes_dfa.second_step import _is_valid_guess


@pytest.mark.parametrize("key, expected", [pytest.param(b"A" * 16, True), pytest.param(b"B" * 16, False)])
def test_is_valid_guess(key: bytes, expected: bool) -> None:
    last_key = b"".join(key_expension(key, 11)[-4:])
    normal_state = _get_state(b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9")
    faulty_state = _get_state(b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~")
    assert _is_valid_guess(normal_state, faulty_state, last_key) == (last_key, expected)
