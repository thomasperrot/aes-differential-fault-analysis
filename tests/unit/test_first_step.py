import pytest

from aes_dfa.attack import _get_state
from aes_dfa.first_step import (
    _compute_first_column,
    _compute_fourth_column,
    _compute_second_column,
    _compute_third_column,
    get_all_possible_keys,
)
from aes_dfa.key_expension import key_expension


@pytest.mark.parametrize(
    "normal_state, faulty_state, key",
    [
        pytest.param(
            b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9",
            b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~",
            b"A" * 16,
        ),
        pytest.param(
            b"sDk\xbaJZ`\xc9A\x0c\xf3\xd8\x80[\x91\n", b"$\x00\x88e\xbd\xbc\x8308O\\\x18W\x130\x92", b"B" * 16,
        ),
    ],
)
def test_get_all_possible_keys(normal_state: bytes, faulty_state: bytes, key: bytes) -> None:
    """Assert that key[12], k[9], k[6] and k[3] are in the hypothesis."""

    last_key = b"".join(key_expension(key, 11)[-4:])
    equations = get_all_possible_keys(_get_state(normal_state), _get_state(faulty_state))
    found = False
    for eq in equations:
        if all(last_key[i] in eq[i + 1] for i in range(0x10)):
            found = True
    assert found


@pytest.mark.parametrize(
    "normal_state, faulty_state, key",
    [
        pytest.param(
            b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9",
            b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~",
            b"A" * 16,
        ),
        pytest.param(
            b"sDk\xbaJZ`\xc9A\x0c\xf3\xd8\x80[\x91\n", b"$\x00\x88e\xbd\xbc\x8308O\\\x18W\x130\x92", b"B" * 16,
        ),
    ],
)
def test_compute_first_column(normal_state: bytes, faulty_state: bytes, key: bytes) -> None:
    """Assert that key[0], k[7], k[10] and k[13] are in the hypothesis."""

    last_key = b"".join(key_expension(key, 11)[-4:])
    equations = _compute_first_column(_get_state(normal_state), _get_state(faulty_state))
    found = False
    for d, eq in equations.items():
        if last_key[0] in eq[1] and last_key[7] in eq[8] and last_key[10] in eq[11] and last_key[13] in eq[14]:
            found = True
    assert found


@pytest.mark.parametrize(
    "normal_state, faulty_state, key",
    [
        pytest.param(
            b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9",
            b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~",
            b"A" * 16,
        ),
        pytest.param(
            b"sDk\xbaJZ`\xc9A\x0c\xf3\xd8\x80[\x91\n", b"$\x00\x88e\xbd\xbc\x8308O\\\x18W\x130\x92", b"B" * 16,
        ),
    ],
)
def test_compute_second_column(normal_state: bytes, faulty_state: bytes, key: bytes) -> None:
    """Assert that key[4], k[1], k[14] and k[11] are in the hypothesis."""

    last_key = b"".join(key_expension(key, 11)[-4:])
    equations = _compute_second_column(_get_state(normal_state), _get_state(faulty_state))
    found = False
    for d, eq in equations.items():
        if last_key[4] in eq[5] and last_key[1] in eq[2] and last_key[14] in eq[15] and last_key[11] in eq[12]:
            found = True
    assert found


@pytest.mark.parametrize(
    "normal_state, faulty_state, key",
    [
        pytest.param(
            b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9",
            b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~",
            b"A" * 16,
        ),
        pytest.param(
            b"sDk\xbaJZ`\xc9A\x0c\xf3\xd8\x80[\x91\n", b"$\x00\x88e\xbd\xbc\x8308O\\\x18W\x130\x92", b"B" * 16,
        ),
    ],
)
def test_compute_third_column(normal_state: bytes, faulty_state: bytes, key: bytes) -> None:
    """Assert that key[8], k[5], k[2] and k[15] are in the hypothesis."""

    last_key = b"".join(key_expension(key, 11)[-4:])
    equations = _compute_third_column(_get_state(normal_state), _get_state(faulty_state))
    found = False
    for d, eq in equations.items():
        if last_key[8] in eq[9] and last_key[5] in eq[6] and last_key[2] in eq[3] and last_key[15] in eq[16]:
            found = True
    assert found


@pytest.mark.parametrize(
    "normal_state, faulty_state, key",
    [
        pytest.param(
            b"\x81\xd6\xcd\xc3\xbd\x16\xfb\x8dr\xb9\xbb\x88\x81\x8b[\xe9",
            b"\xef\xf95\x08c\x01\x87\xb8\xd3IN\x8bp\xe6\x88~",
            b"A" * 16,
        ),
        pytest.param(
            b"sDk\xbaJZ`\xc9A\x0c\xf3\xd8\x80[\x91\n", b"$\x00\x88e\xbd\xbc\x8308O\\\x18W\x130\x92", b"B" * 16,
        ),
    ],
)
def test_compute_fourth_column(normal_state: bytes, faulty_state: bytes, key: bytes) -> None:
    """Assert that key[12], k[9], k[6] and k[3] are in the hypothesis."""

    last_key = b"".join(key_expension(key, 11)[-4:])
    equations = _compute_fourth_column(_get_state(normal_state), _get_state(faulty_state))
    found = False
    for d, eq in equations.items():
        if last_key[12] in eq[13] and last_key[9] in eq[10] and last_key[6] in eq[7] and last_key[3] in eq[4]:
            found = True
    assert found
