"""This module contains ready-made agents generator for mobile devices"""
from ..core.mobile import DeviceLoad
from ..core.base_device import MobileDevice
from ..core.utils import sattolo_shuffle


class Mobile:
    """class wrapper for get mobile datasets with subsequent conversion into generator Device object"""
    @staticmethod
    def _generator(seq):
        # TODO need optimisation
        while True:
            seq = sattolo_shuffle(seq)
            for d in seq:
                yield MobileDevice.generate_device(**d).agent

    @classmethod
    def random_apple(cls):
        return next(cls._generator(DeviceLoad.apple()))

    @classmethod
    def random_android(cls):
        return next(cls._generator(DeviceLoad.android()))

    @classmethod
    def random_mobile_by_key(cls, key: str):
        return next(cls._generator(DeviceLoad.by_key(key)))


RandomAndroid = Mobile.random_android
RandomApple = Mobile.random_apple
RandomMobileKey = Mobile.random_mobile_by_key
