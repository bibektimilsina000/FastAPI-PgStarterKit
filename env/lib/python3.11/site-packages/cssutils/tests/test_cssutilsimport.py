"""Testcase for cssutils imports"""

import cssutils


class CSSutilsImportTestCase:
    def test_import_all(self):
        "from cssutils import *"
        namespace = {}
        exec('from cssutils import *', namespace)
        del namespace['__builtins__']
        exp = {
            'CSSParser': cssutils.CSSParser,
            'CSSSerializer': cssutils.CSSSerializer,
            'css': cssutils.css,
            'stylesheets': cssutils.stylesheets,
        }
        assert namespace == exp
