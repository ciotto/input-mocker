import os
from random import choice
from timeout_decorator import timeout_decorator, TimeoutError
import six
import sys


class InputMocker:
    def __init__(self, inputs=None, random=False):
        if inputs:
            for i in inputs:
                if not isinstance(i, six.string_types):
                    raise ValueError('%s is not allowed as input' % type(i))
                if os.linesep in i:
                    raise ValueError('Line separator char not allowed in input string')
        else:
            inputs = ['y', 'n']
        self.inputs = inputs
        self.index = 0
        self.random = random
        self.prompts = []

        self._patches = []
        self.stdin = None

    def get_input(self):
        if self.random:
            return str(choice(self.inputs))
        if self.index >= len(self.inputs):
            self.index = 0
        r = self.inputs[self.index]
        self.index += 1
        return str(r)

    def __enter__(self):
        p = self

        class FileMock:
            def readline(self):
                return p.get_input() + os.linesep
        
        self.stdin = sys.stdin
        sys.stdin = FileMock()

    def __exit__(self, *exc_info):
        sys.stdin = self.stdin
        self.stdin = None


class TimeoutTestCaseMixin:
    @property
    def _input(self):
        if sys.version_info >= (3, 0):
            return input
        else:
            return raw_input

    def run_with_timeout(self, func, timeout=0.01, raise_exception=False, args=None, kwargs=None):
        if not args:
            args = []
        if not kwargs:
            kwargs = {}

        @timeout_decorator.timeout(timeout)
        def do():
            return func(*args, **kwargs)
        try:
            return do()
        except TimeoutError as e:
            if raise_exception:
                raise e
            return e

    def assertNotTimeout(self, func, *args, **kwargs):
        result = self.run_with_timeout(func, *args, **kwargs)
        self.assertFalse(isinstance(result, TimeoutError), 'Timeout occurred in function %s' % func)
        return result

    def assertTimeout(self, func, *args, **kwargs):
        result = self.run_with_timeout(func, *args, **kwargs)
        self.assertTrue(isinstance(result, TimeoutError), 'Timeout not occurred in function %s' % func)


def patch(*args, **kwargs):
    mocker = InputMocker(*args, **kwargs)

    def patch_decorator(func):
        def func_patched(*a, **k):
            with mocker:
                func(*a, **k)
        return func_patched
    return patch_decorator

