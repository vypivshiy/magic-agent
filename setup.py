from setuptools import setup

from magic_agent.crawlers.config import __version__
from magic_agent.crawlers import Updater


# check preloaded cache datasets: mobiles, webkit, chrome
Updater().cache_exist()


with open("README.MD", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='magic-agent',
    version=__version__,
    packages=['magic_agent'],
    url='https://github.com/vypivshiy/magic_agent',
    license='MIT',
    author='georgiy',
    author_email='',
    python_requires='>=3.8',
    description='Offline generator user-agent strings',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
