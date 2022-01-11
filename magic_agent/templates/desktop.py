"""This module contains ready-made agents generator for desktop"""

from ..core import base
from magic_agent.core.rules import MozillaDefault, RANDOM_LINUX, RANDOM_WINDOWS, AppleWebKit, LikeGecko, Chrome, Safari


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
