from typing import List
from random import randrange
import tempfile
import os
import json


def sattolo_shuffle(seq: List):
    # Sattolo algorithm for shuffle List Sequence bigger than 2080 elements
    # https://docs.python.org/3/library/random.html#random.shuffle
    i = len(seq)
    while i > 1:
        i -= 1
        j = randrange(i)  # 0 <= j <= i-1
        seq[j], seq[i] = seq[i], seq[j]
    return seq


def save_to_tmp(data, json_name: str):
    db = os.path.join(tempfile.gettempdir(), json_name)
    with open(db, "w") as f:
        json.dump(data, f)


def tmp_exist(json_name: str):
    db = os.path.join(tempfile.gettempdir(), json_name)
    return os.path.isfile(db)
