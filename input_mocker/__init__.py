from random import choice
from timeout_decorator import timeout_decorator, TimeoutError
import sys


class InputMocker:
    def __init__(self, answers=None, random=False):
        if not answers:
            answers = ['y', 'n']
        self.answers = answers
        self.index = 0
        self.random = random
        self.prompts = []

        self._patches = []
        self.stdin = None

    def get_answer(self):
        if self.random:
            return choice(self.answers)
        if self.index >= len(self.answers):
            self.index = 0
        r = self.answers[self.index]
        self.index += 1
        return r

    def __enter__(self):
        p = self

        class FileMock:
            def readline(self):
                return p.get_answer()
        
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

