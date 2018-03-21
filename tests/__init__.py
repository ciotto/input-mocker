import unittest
import sys
if sys.version_info >= (3, 0):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse
from .fake import _input
import input_mocker
from input_mocker import InputMocker, TimeoutTestCaseMixin
from timeout_decorator import TimeoutError


class TestInputMocker(unittest.TestCase, TimeoutTestCaseMixin):
    def test_assert_timeout(self):
        self.assertTimeout(self._input)
        self.assertTimeout(self._input, args=['Foo'])

    def test_assert_not_timeout(self):
        string = 'Foo Bar'
        result = self.assertNotTimeout(string.split, args=[' '])
        self.assertEqual(result, ['Foo', 'Bar'])
        result = self.assertNotTimeout(urlparse, args=['//foo.bar'], kwargs={'scheme': 'https'})
        self.assertEqual(result.geturl(), u'https://foo.bar')

    def test_assert_timeout_exception(self):
        string = 'Foo Bar'
        with self.assertRaises(TimeoutError):
            self.assertTimeout(self._input, raise_exception=True)

    def test_sys_stdin_readline(self):
        with InputMocker():
            results = []
            loops = 10
            for i in range(0, loops):
                result = self.assertNotTimeout(sys.stdin.readline)
                results.append(result)

            self.assertEqual(results, ['y', 'n'] * int(loops / 2))

        self.assertTimeout(self._input)

        with InputMocker(answers=['foo', 'bar']):
            results = []
            loops = 10
            for i in range(0, loops):
                result = self.assertNotTimeout(sys.stdin.readline)
                results.append(result)

            self.assertEqual(results, ['foo', 'bar'] * int(loops / 2))

        self.assertTimeout(self._input)

        with InputMocker(random=True):
            results = []
            loops = 10
            for i in range(0, loops):
                result = self.assertNotTimeout(sys.stdin.readline)
                results.append(result)

            self.assertNotEqual(results, ['y', 'n'] * int(loops / 2))

    def test_input_mocker(self):
        with InputMocker():
            results = []
            loops = 10
            for i in range(0, loops):
                result = self.assertNotTimeout(self._input)
                results.append(result)

            self.assertEqual(results, ['y', 'n'] * int(loops / 2))

        self.assertTimeout(self._input)

    def test_external_module(self):
        with InputMocker():
            results = []
            loops = 10
            for i in range(0, loops):
                result = self.assertNotTimeout(_input)
                results.append(result)

            self.assertEqual(results, ['y', 'n'] * int(loops / 2))
        self.assertTimeout(_input)

    @input_mocker.patch()
    def test_decorator(self):
        results = []
        loops = 10
        for i in range(0, loops):
            result = self.assertNotTimeout(_input)
            results.append(result)

        self.assertEqual(results, ['y', 'n'] * int(loops / 2))
