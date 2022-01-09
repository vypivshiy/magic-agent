from ..core.utils import save_to_tmp, tmp_exist
from magic_agent.crawlers import config
from magic_agent.crawlers.http import Request
from magic_agent.crawlers import webkits_all, chromium_all


class Updater:
    """Updater constants class"""
    def __init__(self,
                 *,
                 tmp_devices: str = config.DEVICES_JSON,
                 tmp_chrome: str = config.CHROME_JSON,
                 tmp_webkit: str = config.WEBKIT_JSON,
                 devices_url: str = config.CACHE_DEVICES_URL,
                 chrome_url: str = config.CACHE_CHROME_URL,
                 webkit_url: str = config.CACHE_WEBKIT_URL):
        self.devices_url = devices_url
        self.chrome_url = chrome_url
        self.webkit_url = webkit_url
        self.tmp_devices = tmp_devices
        self.tmp_chrome = tmp_chrome
        self.tmp_webkit = tmp_webkit

    @staticmethod
    def save(data, filename):
        save_to_tmp(data, filename)

    def update_chrome(self):
        print("Download chrome versions")
        try:
            chrome_version = chromium_all()
        except Exception as e:
            print("update_webkit return {} exception, download from cache".format(e))
            chrome_version = Request.json(self.chrome_url)
        self.save(chrome_version, self.tmp_chrome)
        print("Done")

    def update_webkit(self):
        print("Download webkit versions")
        try:
            webkit_version = webkits_all()
        except Exception as e:
            print("update_webkit return {} exception, download from cache".format(e))
            webkit_version = Request.json(self.webkit_url)
        self.save(webkit_version, self.tmp_webkit)
        print("Done")

    def update_devices(self):
        print("Download mobiles dataset")
        devices = Request.json(self.devices_url)
        self.save(devices, self.tmp_devices)
        print("Done")

    def update_full(self):
        self.update_devices()
        self.update_chrome()
        self.update_webkit()

    def cache_exist(self) -> bool:
        if tmp_exist(self.tmp_chrome) and tmp_exist(self.tmp_webkit) and tmp_exist(self.tmp_devices):
            return True
        self.update_full()
        return True

    @classmethod
    def update(cls):
        cls().update_full()
