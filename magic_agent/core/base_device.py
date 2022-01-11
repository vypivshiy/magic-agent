import re
from random import choice
from dataclasses import dataclass
from typing import Optional

from .base import RuleItem, RuleDevice, BaseAgent
from magic_agent.core.rules import (MozillaDefault,
                                    SafariMobile,
                                    Chrome,
                                    AppleWebKit,
                                    LikeGecko,
                                    SafariRandom,
                                    Safari,
                                    AppleWebkitRandom)


@dataclass(frozen=True)
class MobileDevice:
    """Base mobile device dataclass"""
    model: str
    released: int
    operating_system: str
    platform: str
    battery_capacity: int
    model_id: Optional[list[str]] = None
    market_regions: Optional[list[str]] = None
    codename: Optional[str] = None
    oem_id: Optional[str] = None
    market_countries: Optional[str] = None
    resolution: Optional[dict] = None

    @classmethod
    def generate_device(cls, **kwargs):
        """generate devices with json data"""
        return cls(**kwargs)

    @property
    def is_android(self) -> bool:
        return "android" in self.platform.lower()

    @property
    def is_apple(self) -> bool:
        return "ios" in self.platform.lower()

    @property
    def version(self) -> str:
        """return operating system version"""
        if self.is_android:
            return re.findall(r'Android (.*?) ', self.operating_system)[0]
        elif self.is_apple:
            return re.findall(r' iOS (.*?)', self.operating_system)[0]
        return ""

    @property
    def agent(self) -> BaseAgent:
        """return BaseAgent class"""
        return MobileAgent(self).agent()


class MobileAgent:
    """Convert Device class to useragent"""
    __RE_SYSTEM_VERSION = re.compile(r"([\d.]+)")

    def __init__(self, device: MobileDevice):
        self._device = device

    def agent(self, *, by_device_name: bool = True, by_model_id: bool = True) -> BaseAgent:
        """return singe device BaseAgent class"""
        if self._device.is_android:
            return self._android_agent(by_model_id, by_device_name)

        elif self._device.is_apple:
            return self._apple_agent()

    @property
    def _system_version(self) -> str:
        return self.__RE_SYSTEM_VERSION.findall(self._device.operating_system)[0]

    def _android_agent(self, by_model_id, by_device_name):
        device_items = ["Linux"]
        if self._device.operating_system:
            device_items.append(f"Android {self._system_version}")
        else:
            device_items.append("Android 10.0")

        if by_model_id and self._device.model_id:
            device_items.append(choice(self._device.model_id))

        elif by_device_name:
            device_name = " ".join(self._device.model.split(" ")[:3])
            device_items.append(device_name)

        device = RuleDevice(
            items=tuple(device_items))

        return BaseAgent(
            rules=(
                MozillaDefault,
                device,
                AppleWebKit,
                LikeGecko,
                Chrome,
                choice((Safari, SafariMobile))
            ))

    def _apple_agent(self):
        if "iPhone" in self._device.model:
            device_items = ["iPhone"]
        elif "iPad" in self._device.model:
            device_items = ["iPad"]
        elif "iPod" in self._device.model:
            device_items = ["iPod"]
        else:
            raise TypeError("Unknown apple device passed")
        o_sys = self._system_version

        if "." not in o_sys:
            apple_version = RuleItem(f"Version/{o_sys}.0")  # Version string
            o_sys += "_0"
        else:
            apple_version = RuleItem(f"Version/{o_sys}")
            o_sys = o_sys.replace(".", "_")

        device_items.append(f"CPU OS {o_sys} like Mac OS X")
        device = RuleDevice(items=tuple(device_items))
        device_build = RuleItem(f"Mobile/{self._device.model_id[0]}")
        return BaseAgent(
            rules=(
                MozillaDefault,
                device,
                AppleWebkitRandom,
                LikeGecko,
                apple_version,
                device_build,
                SafariRandom
            ))

    def __str__(self):
        return self.agent().agent
