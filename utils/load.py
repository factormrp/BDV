from typing import Union
import json
import os

def _load_csv(path: str) -> str:
    with open(path) as f:
        lines = f.read().splitlines()
    return [l.split(",") for l in lines]

def _load_json(path: str) -> dict:
    with open(path) as f:
        j = json.load(f)
    return j

def load(path: str) -> Union[dict,str]:
    if path[-4:] == ".csv":
        return _load_csv(path)
    elif path[-5:] == ".json":
        return _load_json(path)
    else:
        raise ValueError("file extension for given path is not supported")
