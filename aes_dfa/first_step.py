from collections import defaultdict
from typing import Dict, Generator, List

from .common import MULTIPLICATION_BY_2, MULTIPLICATION_BY_3, REVERSE_S_BOX, State


def get_all_possible_keys(normal_state: State, faulty_state: State) -> List[Dict[int, List[int]]]:
    d1_equations = list(_compute_first_column(normal_state, faulty_state).values())
    d2_equations = list(_compute_second_column(normal_state, faulty_state).values())
    d3_equations = list(_compute_third_column(normal_state, faulty_state).values())
    d4_equations = list(_compute_fourth_column(normal_state, faulty_state).values())
    equations = []
    for eq_1 in d1_equations:
        for eq_2 in d2_equations:
            for eq_3 in d3_equations:
                for eq_4 in d4_equations:
                    equations.append({**eq_1, **eq_2, **eq_3, **eq_4})
    return equations


def get_keys(equations: Dict[int, List[int]]) -> Generator[bytes, None, None]:
    for v1 in equations[1]:
        for v2 in equations[2]:
            for v3 in equations[3]:
                for v4 in equations[4]:
                    for v5 in equations[5]:
                        for v6 in equations[6]:
                            for v7 in equations[7]:
                                for v8 in equations[8]:
                                    for v9 in equations[9]:
                                        for v10 in equations[10]:
                                            for v11 in equations[11]:
                                                for v12 in equations[12]:
                                                    for v13 in equations[13]:
                                                        for v14 in equations[14]:
                                                            for v15 in equations[15]:
                                                                for v16 in equations[16]:
                                                                    yield bytes(
                                                                        [
                                                                            v1,
                                                                            v2,
                                                                            v3,
                                                                            v4,
                                                                            v5,
                                                                            v6,
                                                                            v7,
                                                                            v8,
                                                                            v9,
                                                                            v10,
                                                                            v11,
                                                                            v12,
                                                                            v13,
                                                                            v14,
                                                                            v15,
                                                                            v16,
                                                                        ]
                                                                    )


def _compute_first_column(normal_state: State, faulty_state: State) -> Dict[int, Dict[int, List[int]]]:
    # x1
    potential_d_1: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[0, 0] ^ k] ^ REVERSE_S_BOX[faulty_state[0, 0] ^ k]
            if MULTIPLICATION_BY_2[d] == diff:
                potential_d_1[d].append(k)
    # x14
    potential_d_2: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[1, 3] ^ k] ^ REVERSE_S_BOX[faulty_state[1, 3] ^ k]
            if d == diff:
                potential_d_2[d].append(k)
    # x11
    potential_d_3: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[2, 2] ^ k] ^ REVERSE_S_BOX[faulty_state[2, 2] ^ k]
            if d == diff:
                potential_d_3[d].append(k)

    # x8
    potential_d_4: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[3, 1] ^ k] ^ REVERSE_S_BOX[faulty_state[3, 1] ^ k]
            if MULTIPLICATION_BY_3[d] == diff:
                potential_d_4[d].append(k)

    potential_d = set(potential_d_1) & set(potential_d_2) & set(potential_d_3) & set(potential_d_4)
    return {
        d: {1: potential_d_1[d], 14: potential_d_2[d], 11: potential_d_3[d], 8: potential_d_4[d]} for d in potential_d
    }


def _compute_second_column(normal_state: State, faulty_state: State) -> Dict[int, Dict[int, List[int]]]:
    # x5
    potential_d_1: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[0, 1] ^ k] ^ REVERSE_S_BOX[faulty_state[0, 1] ^ k]
            if d == diff:
                potential_d_1[d].append(k)
    # x2
    potential_d_2: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[1, 0] ^ k] ^ REVERSE_S_BOX[faulty_state[1, 0] ^ k]
            if d == diff:
                potential_d_2[d].append(k)
    # x15
    potential_d_3: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[2, 3] ^ k] ^ REVERSE_S_BOX[faulty_state[2, 3] ^ k]
            if MULTIPLICATION_BY_3[d] == diff:
                potential_d_3[d].append(k)

    # x12
    potential_d_4: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[3, 2] ^ k] ^ REVERSE_S_BOX[faulty_state[3, 2] ^ k]
            if MULTIPLICATION_BY_2[d] == diff:
                potential_d_4[d].append(k)

    potential_d = set(potential_d_1) & set(potential_d_2) & set(potential_d_3) & set(potential_d_4)
    return {
        d: {5: potential_d_1[d], 2: potential_d_2[d], 15: potential_d_3[d], 12: potential_d_4[d]} for d in potential_d
    }


def _compute_third_column(normal_state: State, faulty_state: State) -> Dict[int, Dict[int, List[int]]]:
    # x9
    potential_d_1: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[0, 2] ^ k] ^ REVERSE_S_BOX[faulty_state[0, 2] ^ k]
            if d == diff:
                potential_d_1[d].append(k)
    # x6
    potential_d_2: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[1, 1] ^ k] ^ REVERSE_S_BOX[faulty_state[1, 1] ^ k]
            if MULTIPLICATION_BY_3[d] == diff:
                potential_d_2[d].append(k)
    # x3
    potential_d_3: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[2, 0] ^ k] ^ REVERSE_S_BOX[faulty_state[2, 0] ^ k]
            if MULTIPLICATION_BY_2[d] == diff:
                potential_d_3[d].append(k)

    # x16
    potential_d_4: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[3, 3] ^ k] ^ REVERSE_S_BOX[faulty_state[3, 3] ^ k]
            if d == diff:
                potential_d_4[d].append(k)

    potential_d = set(potential_d_1) & set(potential_d_2) & set(potential_d_3) & set(potential_d_4)
    return {
        d: {9: potential_d_1[d], 6: potential_d_2[d], 3: potential_d_3[d], 16: potential_d_4[d]} for d in potential_d
    }


def _compute_fourth_column(normal_state: State, faulty_state: State) -> Dict[int, Dict[int, List[int]]]:
    # x13
    potential_d_1: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[0, 3] ^ k] ^ REVERSE_S_BOX[faulty_state[0, 3] ^ k]
            if MULTIPLICATION_BY_3[d] == diff:
                potential_d_1[d].append(k)
    # x10
    potential_d_2: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[1, 2] ^ k] ^ REVERSE_S_BOX[faulty_state[1, 2] ^ k]
            if MULTIPLICATION_BY_2[d] == diff:
                potential_d_2[d].append(k)
    # x7
    potential_d_3: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[2, 1] ^ k] ^ REVERSE_S_BOX[faulty_state[2, 1] ^ k]
            if d == diff:
                potential_d_3[d].append(k)

    # x4
    potential_d_4: Dict[int, List[int]] = defaultdict(list)
    for d in range(1, 0x100):
        for k in range(0x100):
            diff = REVERSE_S_BOX[normal_state[3, 0] ^ k] ^ REVERSE_S_BOX[faulty_state[3, 0] ^ k]
            if d == diff:
                potential_d_4[d].append(k)

    potential_d = set(potential_d_1) & set(potential_d_2) & set(potential_d_3) & set(potential_d_4)
    return {
        d: {13: potential_d_1[d], 10: potential_d_2[d], 7: potential_d_3[d], 4: potential_d_4[d]} for d in potential_d
    }
