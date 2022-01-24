"""
Handle the multi-language system
"""

import json
import os
from collections.abc import Iterable


class Language(dict):
    """
    Represent the strings in the proper language
    """

    def __init__(self, file: str):
        """
        Initialize the language object

        :param file: the json file containing translations
        """

        self._file = file
        with open(file, 'r', encoding="utf-8") as f:
            datas = json.loads(f.read())
        if os.name != 'posix':
            import ctypes
            import locale
            windll = ctypes.windll.kernel32
            language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        else:
            language = os.environ['LANG'].split('.')[0]

        for key, value in datas.items():
            if language in value.keys():
                self[key] = value[language]
            elif 'en_GB' in value.keys():
                self[key] = value['en_GB']
            else:
                self[key] = f'missing translation for {repr(key)}'
        super().__init__()

    def __repr__(self):
        return f"<Language object on file {repr(self._file)} : " + \
               ", ".join(f"{repr(var)}={repr(value)}" for var, value in self.items()) + '>'

    def __str__(self):
        return super().__repr__()

    def __getattr__(self, item):
        if item in self:
            return self[item]
        raise AttributeError(str(item))

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        if item in self:
            del self[item]
        raise AttributeError(str(item))

    def __dir__(self) -> Iterable[str]:
        return list(self.keys()) + list(super().__dir__())
