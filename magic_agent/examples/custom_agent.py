from magic_agent.core.base import RuleItem, RuleDevice, BaseAgent
from magic_agent.core import rules

app = RuleItem(string="com.myapp.apk/{}", items=list(range(2200, 2300)))

# generate agent device information
device = RuleDevice(
    items=("Linux", "PalmOS", "My-SUPER-SMARTPHONE {}", "Build/{}"),
    rule=RuleItem(items=(
        tuple(range(100, 500)),
        tuple("ABCDEFG")
    )
    ),
    sep=", ",  # config delimiter, default "; "
)

# prepare agent object generator
b = BaseAgent(rules=(app,
                     device,
                     rules.Chrome
                     )
              )

for _ in range(5):
    print(b.agent)

# com.myapp.apk/2219 (Linux, PalmOS, My-SUPER-SMARTPHONE 335, Build/G) Chrome/93.0.4577.72
# com.myapp.apk/2204 (Linux, PalmOS, My-SUPER-SMARTPHONE 468, Build/F) Chrome/93.0.4577.58
# com.myapp.apk/2280 (Linux, PalmOS, My-SUPER-SMARTPHONE 451, Build/E) Chrome/94.0.4606.98
# com.myapp.apk/2243 (Linux, PalmOS, My-SUPER-SMARTPHONE 244, Build/E) Chrome/94.0.4606.110
# com.myapp.apk/2284 (Linux, PalmOS, My-SUPER-SMARTPHONE 373, Build/D) Chrome/92.0.4515.57
