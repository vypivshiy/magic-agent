from magic_agent.templates import RandomMobileKey, RandomApple, RandomAndroid
from magic_agent.core.mobile_keys import SAMSUNG


if __name__ == '__main__':
    # random apple mobile agent
    print(RandomApple().agent)
    print(RandomApple().agent)

    # any random android mobile agent
    print(RandomAndroid().agent)
    print(RandomAndroid().agent)

    # random android samsung agent
    print(RandomMobileKey(SAMSUNG).agent)
    print(RandomMobileKey(SAMSUNG).agent)

# Mozilla/5.0 (iPhone; CPU OS 13_0 like Mac OS X) AppleWebKit/602.1.32.3 (KHTML, like Gecko) Version/13.0 Mobile/A2160 Safari/602.2.14
# Mozilla/5.0 (iPad; CPU OS 12_1 like Mac OS X) AppleWebKit/612.1.2.5 (KHTML, like Gecko) Version/12.1 Mobile/A1983 Safari/600.1.4.17.8
# Mozilla/5.0 (Linux; Android 9.0; GM1901) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.49 Mobile Safari/537.36
# Mozilla/5.0 (Linux; Android 9.0; V0470UU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.58 Safari/537.36
# Mozilla/5.0 (Linux; Android 9.0; SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.42 Mobile Safari/537.36
# Mozilla/5.0 (Linux; Android 6.0; SM-J320AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.52 Safari/537.36