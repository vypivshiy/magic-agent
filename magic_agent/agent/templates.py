"""Ready-made templates for generating user agents"""

from magic_agent.core import base
from magic_agent.agent.constants import MozillaDefault, RANDOM_LINUX, RANDOM_WINDOWS, AppleWebKit, LikeGecko, Chrome, Safari
from magic_agent.core.mobile import DeviceLoad
from magic_agent.core.base_device import BaseDevice
from magic_agent.core.utils import sattolo_shuffle

LinuxChrome = base.BaseAgent(
    rules=(
        MozillaDefault,
        RANDOM_LINUX,
        AppleWebKit,
        LikeGecko,
        Chrome,
        Safari
    ))

WindowsChrome = base.BaseAgent(
    rules=(
        MozillaDefault,
        RANDOM_WINDOWS,
        AppleWebKit,
        LikeGecko,
        Chrome,
        Safari
    ))

# need refactoring this calls


class Mobile:

    @staticmethod
    def _generator(seq):
        # TODO need optimisation
        while True:
            seq = sattolo_shuffle(seq)
            for d in seq:
                yield BaseDevice.generate_device(**d).agent

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
