import re
from typing import List

from magic_agent.crawlers.http import Request

"""Simple parsers actual versions chrome and webkits versions.
WARNING!!! chrome and webkit response are very large, 
(chrome ~2.1MiB, webkit ~5.1 MiB) so the response does come very slow!"""

RE_CHROMIUM = re.compile(r'<a href="/chromium/src/\+/refs/tags/[\d.]{2,}">([\d.]{2,})</a>')
RE_WEBKIT = re.compile(r">Safari-([\d.]{2,})<")

WEBKIT_REP_URL = "https://trac.webkit.org/browser/webkit/tags?action=inplace"
CHROME_REP_URL = "https://chromium.googlesource.com/chromium/src/+refs"


def chromium_last_versions(os: str) -> str:
    os_list = ["win", "linux", "ios", "cros", "mac", "mac_arm64"  "win64", "android", "webview"]
    if os not in os_list:
        raise TypeError("Operation system is not available")

    resp = Request.json("https://omahaproxy.appspot.com/all.json")
    for r in resp:
        if os == r["os"]:
            for v in r["versions"]:
                if v["channel"] == "stable":
                    return v["current_version"]


def chromium_all(*, min_major_version: int = 90, min_minor_version: int = 40) -> List[str]:
    """get chrome versions"""
    resp = Request.get(CHROME_REP_URL)
    versions = RE_CHROMIUM.findall(resp)
    versions = [v for v in versions if len(v.split(".")) > 2 and (int(v.split(".")[-1]) >= min_minor_version
                                                                  and int(v.split(".")[0]) >= min_major_version)]
    return versions


def webkits_all(*, min_major_version: int = 360, min_minor_version: int = 0,
                max_versions_num=4) -> List[str]:
    """very slow request, return over 3000 webkits versions!"""
    resp = Request.get(WEBKIT_REP_URL)  # response comes in a ~30-90 seconds!
    webkits = RE_WEBKIT.findall(resp)
    webkits = [w for w in webkits if
               2 <= len(w.split(".")) < max_versions_num and
               int(w.split(".")[0]) >= min_major_version and
               int(w.split(".")[-1]) >= min_minor_version
               ]

    return webkits
