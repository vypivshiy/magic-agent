"""This module contains constants"""
import json
from dataclasses import dataclass
from os import PathLike
from typing import List, Union

from magic_agent.crawlers.config import TMP_WEBKIT, TMP_CHROME
from magic_agent.crawlers import Updater


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
