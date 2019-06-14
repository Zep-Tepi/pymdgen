import py.test

from pymdgen import (
    doc_func,
    doc_class,
    doc_module,
    )

def func_a(a,b=None,**kwargs):
    """ this is test function a """
    return

class class_a(object):
    """ this is test class a """
    def method_a(self, a, b=None, **kwargs):
        """ this is test method a """
        return

def test_doc_func():
    output = doc_func("func_a", func_a)
    assert output == ['#### func_a', '', '```', 'func_a(a, b=None, **kwargs)', '```', '', 'this is test function a ', '', '---']

def test_doc_class():
    output = doc_class("class_a", class_a)
    assert output == ['### class_a', '', '```', 'class_a(builtins.object)', '```', '', 'this is test class a ', '', '#### method_a', '', '```', 'method_a(self, a, b=None, **kwargs)', '```', '', 'this is test method a ', '', '---', '']

def test_doc_module():
    output = doc_module("pymdgen.test_module")
    assert output == ['### dummy', '', '```', 'dummy(builtins.object)', '```', '', 'this is a dummy class ', '', '#### dummy_method', '', '```', 'dummy_method(self)', '```', '', 'this is a dummy func ', '', '---', '', '### dummy_func', '', '```', 'dummy_func()', '```', '', 'this is a dummy func ', '', '---']
