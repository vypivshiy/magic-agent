import re
import unittest
from magic_agent.crawlers import Request
from magic_agent.crawlers.parsers import RE_CHROMIUM, RE_WEBKIT
from magic_agent.core.mobile_keys import SAMSUNG
from magic_agent.core.base_device import MobileDevice
from magic_agent.core.utils import sattolo_shuffle
from magic_agent.core.base import RuleItem, RuleDevice, RuleItemGenerator, BaseAgent, sequence_generator
from magic_agent.templates import WindowsChrome, LinuxChrome, RandomApple, RandomAndroid, RandomMobileKey


class Test(unittest.TestCase):
    def test_request_json(self):
        r = Request.json("https://httpbin.org/get", params={"foo space": "bar"})
        self.assertTrue(re.search(r"Python-urllib/\d", r["headers"]["User-Agent"]))
        self.assertEqual(r["url"], "https://httpbin.org/get?foo space=bar")

    def test_request_get(self):
        r = Request.get("https://httpbin.org/get")
        self.assertTrue(re.search(r"https://httpbin\.org/get", r))
        self.assertTrue(re.search(r"Python-urllib/\d", r))

    def test_quick_agent_desktop(self):
        self.assertTrue("Linux" in LinuxChrome.agent)
        self.assertTrue("Linux" in LinuxChrome.agent)
        self.assertTrue("Linux" in LinuxChrome.agent)
        self.assertTrue("Windows" in WindowsChrome.agent)
        self.assertTrue("Windows" in WindowsChrome.agent)
        self.assertTrue("Windows" in WindowsChrome.agent)
        self.assertTrue(type(WindowsChrome.agent_to_dict) is dict)
        self.assertTrue(type(LinuxChrome.agent_to_dict) is dict)

    def test_quick_agent_apple(self):
        self.assertTrue("iPad" or "iPod" or "iPone" in RandomApple().agent)
        self.assertTrue("iPad" or "iPod" or "iPone" in RandomApple().agent)
        self.assertTrue("iPad" or "iPod" or "iPone" in RandomApple().agent)

    def test_quick_agent_android(self):
        self.assertTrue("Android" in RandomAndroid().agent and "Linux" in RandomAndroid().agent)
        self.assertTrue("Android" in RandomAndroid().agent and "Linux" in RandomAndroid().agent)
        self.assertTrue("Android" in RandomAndroid().agent and "Linux" in RandomAndroid().agent)

    def test_quick_agent_android_key(self):
        # samsung device name contains SM-xxxxx identification
        self.assertTrue("SM-" in RandomMobileKey(SAMSUNG).agent)
        self.assertTrue("SM-" in RandomMobileKey(SAMSUNG).agent)
        self.assertTrue("SM-" in RandomMobileKey(SAMSUNG).agent)

    def test_custom_agent_1(self):
        b = BaseAgent(rules=(RuleItem("Test/1"), RuleDevice(items=["Test, foobar"])))
        self.assertEqual(b.agent, "Test/1 (Test, foobar)")
        self.assertEqual(b.agent, "Test/1 (Test, foobar)")
        self.assertEqual(b.agent, "Test/1 (Test, foobar)")

    def test_rule_item(self):
        self.assertEqual(RuleItem("Test/1").get(), "Test/1")
        self.assertEqual(RuleItem("Test/1").get(), "Test/1")
        self.assertEqual(RuleItem("Test/1").get(), "Test/1")

    def test_rule_generator(self):
        t = sequence_generator(["Test/1"])
        self.assertEqual(RuleItemGenerator("foo {}", t).get(), "foo Test/1")
        self.assertEqual(RuleItemGenerator("foo {}", t).get(), "foo Test/1")

    def test_parse_mobile(self):
        test_dict = \
            {"model": "Test Mobile", "model_id": ["T123"], "released": 2077, "operating_system": "Palm OS T",
             "resolution": {"height": 1, "wight": 2}, "market_regions": ["Kekistan", "SovietRussia"],
             "codename": "TestCase", "oem_id": "foobar", "platform": "Android",
             "market_countries": ["KEK", "USSR"], "battery_capacity": 99_999}
        b = MobileDevice(**test_dict)
        self.assertEqual(b.model, "Test Mobile")
        self.assertEqual(b.model_id[0], "T123")
        self.assertEqual(b.market_regions, ["Kekistan", "SovietRussia"])

    def test_device_agent(self):
        test_dict = \
            {"model": "Test Mobile", "model_id": ["T123"], "released": 2077, "operating_system": "Android 10.0",
             "resolution": {"height": 1, "wight": 2}, "market_regions": ["Kekistan", "SovietRussia"],
             "codename": "TestCase", "oem_id": "foobar", "platform": "Android",
             "market_countries": ["KEK", "USSR"], "battery_capacity": 99_999}
        b = MobileDevice(**test_dict)
        self.assertTrue("(Linux; Android 10.0; T123)" in b.agent.agent)

    def test_satollo_shuffle(self):
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        seq_2 = seq.copy()
        seq_2 = sattolo_shuffle(seq_2)
        self.assertNotEqual(seq_2, seq)

    def test_versions_parsers(self):
        resp_webkit = """
       <tr class="odd f5" id="f5">
      <td class="name">
        <span class="expander" title="..." href="/browser/webkit/tags/Safari-532.4">Safari-532.4</a>
      ...
      <td class="age" style="border-color: rgb(152,136,238)">
        ...
      </td>
        ....
        blah blah blah
        """
        resp_chrome = """
                <li class="RefList-item"><a href="/chromium/src/+/refs/tags/99.0.4817.1">99.0.4817.1</a></li>
                <li class="RefList-item"><a href="/chromium/src/+/refs/tags/fobbar">bad-string-1.0</a></li>
                ....
                blah blah blah
                """
        r = RE_CHROMIUM.findall(resp_chrome)
        self.assertEqual(r[0], '99.0.4817.1')
        self.assertEqual(len(RE_CHROMIUM.findall(resp_webkit)), 0)
        r = RE_WEBKIT.findall(resp_webkit)
        self.assertEqual(r[0], '532.4')
        self.assertEqual(len(RE_WEBKIT.findall(resp_chrome)), 0)
