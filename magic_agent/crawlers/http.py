from urllib.request import urlopen
from typing import Optional
import json


class Request:
    """Primitive class wrapper for http requests"""
    @staticmethod
    def _get_params(params: dict) -> str:
        """convert dict to request get params"""
        _get_param = ""
        k: str
        v: str
        for k, v in params.items():
            k = k.replace(' ', "%20")
            v = v.replace(' ', "%20")
            _get_param += k + "=" + v + "&"

        _get_param = _get_param.rstrip("&")
        return _get_param

    @classmethod
    def get(cls, url: str, *, params: Optional[dict] = None, encoding: str = "utf8") -> str:
        """return str response"""
        if params:
            params = cls._get_params(params)
            url += "?" + params
        url = url.replace(' ', "%20")
        with urlopen(url) as response:
            return response.read().decode(encoding)

    @classmethod
    def json(cls, url: str, params: Optional[dict] = None, encoding: str = "utf8") -> [dict, list]:
        """return json response"""
        resp = cls.get(url=url, params=params, encoding=encoding)
        return json.loads(resp)
