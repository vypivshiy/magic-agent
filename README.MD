# MAGIC AGENT
___
Offline Generator random user agents written in pure Python.

Mobile devices information parsed from [phonedb.net](https://phonedb.net) ~(3.1MiB)

Webkit, Chrome versions parsed from official repositories ~(50 KiB)

# How it work
1. During installation or updating, `magic-agent` is downloaded parsed data **to your tmp directory** (mobile 
devices from cached store, browsers versions from official repositories)
2. After installing and downloading data, `magic-agent` will generate user-agents __offline__
3. BaseAgent class accepts **Rule** objects and uses them to concatenate strings according to the required pattern
___
# Features
* Support python 3.8+ without dependencies
* Pre-parsed specifications of common mobile devices (Android, Apple) from 2016-2021 y.
* Simple parsers webkit and chrome versions from official repositories
* Templates for common user agents: chrome-based browsers for desktops, Android and Apple devices
* Creating custom templates user-agents generators 
___
# Install
`pip install https://github.com/vypivshiy/magic_agent.git`
___
# Usage
___
# 1. Generate Desktop agent based-chromium browsers

```python
from magic_agent import WindowsChrome, LinuxChrome

if __name__ == '__main__':
    # generate standard chromium based browser for win and linux OS
    print(WindowsChrome.agent)
    print(LinuxChrome.agent)

    # or return dict-like object {"User-Agent": "..."}
    print(WindowsChrome.agent_to_dict)
    print(LinuxChrome.agent_to_dict)
```
# 2. Generate Mobile useragents:

```python
from magic_agent import RandomApple, RandomAndroid
from magic_agent import RandomMobileKey  # if you need конкретная модель
from magic_agent.agent.mobile_keys import SAMSUNG

# random apple mobile agent
print(RandomApple().agent)
print(RandomApple().agent)

# any random android mobile agent
print(RandomAndroid().agent)
print(RandomAndroid().agent)

# random android samsung agent
print(RandomMobileKey(SAMSUNG).agent)
print(RandomMobileKey(SAMSUNG).agent)
```
# 3. Low-level.  I need unique user agent!
```python
"""Generator user-agent for fictional android application"""
from magic_agent.core.base import RuleItem, RuleDevice, BaseAgent
from magic_agent.agent.templates import Chrome

app = RuleItem(string="com.myapp.apk/{}", items=[i for i in range(2200, 2300)])
device = RuleDevice(items=("Linux", "PalmOS", "My-SUPER-SMARTPHONE {}", "Build/{}"),
                    rule=RuleItem(
                        items=([i for i in range(100, 500)],
                               "ABCDEFG")),
                    sep=", "
                    )

b = BaseAgent(
    rules=(app,
           device,
           Chrome
           )
)
for _ in range(3):
    print(b.agent)
# com.myapp.apk/2262 (Linux, PalmOS, My-SUPER-SMARTPHONE 255, Build/A) Chrome/94.0.4606.127
# com.myapp.apk/2276 (Linux, PalmOS, My-SUPER-SMARTPHONE 252, Build/F) Chrome/92.0.4515.65
# com.myapp.apk/2251 (Linux, PalmOS, My-SUPER-SMARTPHONE 452, Build/A) Chrome/90.0.4430.227
```
~~**How do you like that, Elon Musk???**~~
```python
"""Generator user-agent like in Tesla car!"""
from random import sample
from string import ascii_lowercase, digits
from magic_agent.core.base import BaseAgent, RuleItem, RuleDevice, RuleItemGenerator
from magic_agent.agent.constants import (Chrome, 
                                         MozillaDefault, 
                                         AppleWebKit, 
                                         LikeGecko, 
                                         Safari, 
                                         chromium_generator)

# pseudo random imei generator
def random_imei(): return "".join(sample(ascii_lowercase + digits, 12))


if __name__ == '__main__':
    print()
    device = RuleDevice(items=("X11", "GNU/Linux"))
    tesla = RuleItem("Tesla/2021.{}.{}-{}",
                     items=(
                         (*range(10, 99),),
                         (*range(1, 9),),
                         tuple((random_imei() for _ in range(20)))
                     ))

    chromium = RuleItemGenerator(string="Chromium/{} Chrome/{}", 
                                 generators=chromium_generator(),
                                 randomize=False)  # chromium and chrome versions should be equal! 
    b = BaseAgent(rules=(
        MozillaDefault, device, AppleWebKit, LikeGecko, chromium, Chrome, Safari, tesla
    ))
    for _ in range(3):
        print(b.agent)
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/93.0.4577.129 Chrome/93.0.4577.129 Safari/537.36 Tesla/2021.54.2-rzxq46wot9pg
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/94.0.4606.112 Chrome/94.0.4606.112 Safari/537.36 Tesla/2021.58.7-rzxq46wot9pg
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/95.0.4638.75 Chrome/95.0.4638.75 Safari/537.36 Tesla/2021.21.7-rzxq46wot9pg
# ...
```
