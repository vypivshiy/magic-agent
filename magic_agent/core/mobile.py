import json
from random import choice
from typing import Dict

from magic_agent.agent.mobile_keys import *
from magic_agent.crawlers.config import TMP_DEVICES


class DeviceLoad:
    """Loader devices"""
    ALL_KEYS = [ZTE, XIAOMI, WIKO, ULEFONE, TCL, SONY, SHARP, SAMSUNG, PANASONIC, OPPO, ONEPLUS, NOKIA, MOTOROLA,
                MEIZU, LG, LENOVO, HUAWEI, HTC, BLU, BLACKVIEW, BBK, ASUS, APPLE, ALCATEL]
    PATH = TMP_DEVICES

    @classmethod
    def load_devices_json(cls) -> Dict:
        with open(cls.PATH) as f:
            return json.load(f)

    @classmethod
    def by_key(cls, device_name: str) -> Dict:
        """return device by key constant"""
        if device_name in cls.ALL_KEYS:
            data = cls.load_devices_json()
            return data.get(device_name)
        raise KeyError("Json devices dataset is not include '{}' key".format(device_name))

    @classmethod
    def random(cls):
        """"return random devices list"""
        return cls.load_devices_json().get(choice(cls.ALL_KEYS))

    @classmethod
    def android(cls):
        """return random android devices list"""
        keys_ = cls.ALL_KEYS.copy()
        keys_.remove(APPLE)
        return cls.load_devices_json().get(choice(keys_))

    @classmethod
    def apple(cls):
        """return apple devices list"""
        return cls.load_devices_json().get(APPLE)
