"""Example, how write generator agent for tesla car"""

from random import sample
from string import ascii_lowercase, digits
from magic_agent.core.base import BaseAgent, RuleItem, RuleDevice, RuleItemGenerator
# import constants Rules
from magic_agent.agent.constants import MozillaDefault, AppleWebKit, LikeGecko, Safari, chromium_generator


# pseudo imei generator
def random_imei(): return "".join(sample(ascii_lowercase + digits, 12))


if __name__ == '__main__':
    device = RuleDevice(items=("X11", "GNU/Linux"))
    tesla = RuleItem("Tesla/2021.{}.{}-{}",
                     items=(
                         tuple(range(10, 99)),
                         tuple(range(1, 9)),
                         tuple((random_imei() for _ in range(100)))
                     ))
    # Chromium and Chrome version should be equal version values in Tesla user agent
    #
    chromium = RuleItemGenerator("Chromium/{} Chrome/{}", chromium_generator, randomize=False)
    b = BaseAgent(rules=(
        MozillaDefault,
        device,
        AppleWebKit,
        LikeGecko,
        chromium,
        Safari,
        tesla
    ))
    for _ in range(3):
        print(b.agent)
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/93.0.4577.129 Chrome/93.0.4577.129 Safari/537.36 Tesla/2021.54.2-rzxq46wot9pg
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/94.0.4606.112 Chrome/94.0.4606.112 Safari/537.36 Tesla/2021.58.7-rzxq46wot9pg
# Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/95.0.4638.75 Chrome/95.0.4638.75 Safari/537.36 Tesla/2021.21.7-rzxq46wot9pg
