from magic_agent.agent import WindowsChrome, LinuxChrome


if __name__ == '__main__':
    # generate standart chromium based browser for win and linux OS
    print(WindowsChrome.agent)
    print(LinuxChrome.agent)

    # or return dict-like object
    print(WindowsChrome.agent_to_dict)
    print(LinuxChrome.agent_to_dict)

# Mozilla/5.0 (Windows NT 11.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.59 Safari/537.36
# Mozilla/5.0 (X11; Linux ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.143 Safari/537.36
# {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.89 Safari/537.36'}
# {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.46 Safari/537.36'}