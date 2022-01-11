"""This module contains constants"""
import json
from dataclasses import dataclass
from os import PathLike
from typing import List, Union

from ..core import base
from ..crawlers.config import TMP_WEBKIT, TMP_CHROME
from ..crawlers import Updater


def load_chromium(file: Union[PathLike, str] = TMP_CHROME) -> List[str]:
    with open(file) as f:
        return json.load(f)


def load_webkit(file: Union[PathLike, str] = TMP_WEBKIT) -> List[str]:
    with open(file) as f:
        return json.load(f)


try:
    load_webkit()
    load_chromium()
except FileNotFoundError:
    Updater.update()

webkit_generator = base.sequence_generator(load_webkit())
chromium_generator = base.sequence_generator(load_chromium())

# Desktop devices constants.
# TODO add macintosh


@dataclass(frozen=True)
class Windows:
    x64 = "WOW64"
    x64_2 = "Win64; x64"
    eleven11 = "Windows NT 11.0"
    ten10 = "Windows NT 10.0"
    eight8 = "Windows NT 6.2"
    nt72 = "Windows NT 7.2"
    nt71 = "Windows NT 7.1"
    seven7 = "Windows NT 6.1"
    vista = "Windows NT 6.0"
    xp = "Windows NT 5.1"
    server2003 = "Windows NT 5.3"
    win2000 = "Windows NT 5.0"
    win98 = "Win98"


LINUX_X11 = "X11"


@dataclass(frozen=True)
class Linux:
    default = "Linux"
    x64 = "Linux x86_64"
    amd64 = "Linux amd64"
    i686 = "Linux i686"
    ppc = "Linux ppc"
    ia64 = "Linux ia64"
    armv7l = "Linux armv7l"
    armv6l = "Linux armv6l"


# Templates for useragent strings
Chrome = base.RuleItemGenerator("Chrome/{}", chromium_generator)
MozillaDefault = base.RuleItem("Mozilla/5.0")
LikeGecko = base.RuleItem("(KHTML, like Gecko)")

# For not Apple device strings
AppleWebKit = base.RuleItem("AppleWebKit/537.36")
Safari = base.RuleItem("Safari/537.36")
SafariMobile = base.RuleItem("Mobile Safari/537.36")


# for based gecko engine browsers
Gecko = base.RuleItem("Gecko/{}", (20100625, 20100101, 20100614))
FirefoxGecko = base.RuleItem("Firefox/{}", (97.0, 96.0, 95.0, 94.0, 93.0, 92.0, 91.0, 90.0))
# for opera browsers
Opera = base.RuleItem("OPR/{}", ("80.0.4170.16", "80.0.4170.91"))

# TODO add logic for generate a REAL Safari browsers for apple devices
AppleWebkitRandom = base.RuleItemGenerator("AppleWebKit/{}", webkit_generator)
SafariMobileRandom = base.RuleItemGenerator("Mobile Safari/{}", webkit_generator)
SafariRandom = base.RuleItemGenerator("Safari/{}", webkit_generator)

# standard OS devices strings
LinuxX11_64 = base.RuleDevice(items=(LINUX_X11, Linux.x64))
LinuxX11_AMD64 = base.RuleDevice(items=(LINUX_X11, Linux.amd64))
LinuxX11 = base.RuleDevice(items=(LINUX_X11, Linux.default))
RANDOM_LINUX = base.RuleDevice(items=(LINUX_X11, "Linux {}"), rule=base.RuleItem(items=("x86_64", "amd64", "")))

WindowsXP = base.RuleDevice(items=(Windows.xp,))
WindowsXP_64 = base.RuleDevice(items=(Windows.xp, Windows.x64_2))
Windows7 = base.RuleDevice(items=(Windows.seven7,))
Windows7_64 = base.RuleDevice(items=(Windows.seven7, Windows.x64))
Windows10 = base.RuleDevice(items=(Windows.ten10,))
Windows10_64 = base.RuleDevice(items=(Windows.ten10, Windows.x64))

RANDOM_WINDOWS = base.RuleDevice(items=("Windows NT {}",), rule=base.RuleItem(items=(6.1, 6.2, 10.0, 11.0)))
