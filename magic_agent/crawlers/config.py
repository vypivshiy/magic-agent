import os
import tempfile
import re

__version__ = 0.11

WEBKIT_REP_URL = "https://trac.webkit.org/browser/webkit/tags?action=inplace"
CHROME_REP_URL = "https://chromium.googlesource.com/chromium/src/+refs"

# regular expressions for get versions in browsers engines repos
RE_CHROMIUM = re.compile(r'<a href="/chromium/src/\+/refs/tags/[\d.]{2,}">([\d.]{2,})</a>')
RE_WEBKIT = re.compile(r">Safari-([\d.]{2,})<")


DEVICES_JSON = f"magic-agent_devices_{__version__}.json"
CHROME_JSON = f"magic-agent_chrome_{__version__}.json"
WEBKIT_JSON = f"magic-agent_webkit_{__version__}.json"

TMP_DEVICES = os.path.join(tempfile.gettempdir(), DEVICES_JSON)
TMP_CHROME = os.path.join(tempfile.gettempdir(), CHROME_JSON)
TMP_WEBKIT = os.path.join(tempfile.gettempdir(), WEBKIT_JSON)

# TODO create cache server and delete this repo
CACHE_DEVICES_URL = "https://raw.githubusercontent.com/vypivshiy/magic-agent_cache/main/mobiles.json"
CACHE_CHROME_URL = "https://raw.githubusercontent.com/vypivshiy/magic-agent_cache/main/chromium.json"
CACHE_WEBKIT_URL = "https://raw.githubusercontent.com/vypivshiy/magic-agent_cache/main/webkits.json"
