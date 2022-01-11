from dataclasses import dataclass
from random import choice
from typing import Sequence, Optional, Iterable, Union, Generator, AnyStr, List
from ..core import utils
from abc import ABC, abstractmethod


@dataclass
class Rule(ABC):
    """Abstract rule object"""
    string: str = ""

    def format(self, *args):
        if args:
            return self.string.format(*args[1:])
        return self.string

    @abstractmethod
    def get(self):
        pass

    def __str__(self):
        return self.get()


@dataclass
class RuleItem(Rule):
    """Generate item"""
    string: str = ""
    items: Optional[Union[Sequence[Sequence], Sequence]] = None

    def get(self):
        if self.items:
            _count = self.string.count("{}")
            if _count > 0:
                _items = []
                while len(_items) < _count:
                    for item in self.items:
                        if len(_items) == _count:
                            break
                        if not hasattr(item, "__iter__"):  # if item is not iterable
                            _items.append(choice(self.items))
                        elif isinstance(item, Iterable) and len(item) > 0:
                            _items.append(choice(item))
                        else:
                            raise TypeError(f"{type(item)} is not allowed.")
                return self.format(self.string, *_items)
        return self.string


@dataclass
class RuleItemGenerator(Rule):
    """Generate Item with generator object"""
    string: str = ""
    generators: Optional[Union[Sequence[Generator], Generator]] = None
    randomize: bool = True

    def get(self):
        _count = self.string.count("{}")
        if self.generators and _count > 0:
            _items = []
            while len(_items) < _count:
                if isinstance(self.generators, Sequence):
                    for gen in self.generators:
                        _items.append(next(gen))
                elif self.randomize:
                    for _ in range(_count):
                        _items.append(next(self.generators))
                else:
                    item = next(self.generators)
                    for _ in range(_count):
                        _items.append(item)
            return self.format(self.string, *_items)
        return self.string


@dataclass
class RuleDevice:
    items: Sequence[AnyStr]
    sep: str = "; "
    rule: Optional[RuleItem] = None

    def get(self):
        device_str = "(" + self.sep.join((_.strip() for _ in self.items)) + ")"
        if self.rule:
            self.rule.string = device_str
            device_str = self.rule.get()
        return device_str

    def __str__(self):
        return self.get()


class BaseAgent(object):
    """Base useragent generator class"""

    def __init__(self, *, rules: Sequence[RuleItem]):
        self._rules = rules

    @property
    def agent(self) -> str:
        """Convert sequence rules to user-agent string"""
        return " ".join((r.get() for r in self._rules))

    @property
    def agent_to_dict(self):
        """Convert sequence rules to user-agent dict. Default user-agent key title-style"""
        return {"User-Agent": self.agent}


def sequence_generator(seq: List, *, shuffle: bool = True) -> Generator:
    """wrapper for create generator from list items"""
    while True:
        if shuffle:
            seq = utils.sattolo_shuffle(seq)
        yield from seq
