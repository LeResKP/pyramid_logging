import unittest
import logging
from pyramid import testing
import pyramid_logging
import StringIO


class TestPyramidLogging(unittest.TestCase):

    def test_logging(self):
        request = testing.DummyRequest(environ={'SERVER_NAME': 'servername'})
        log = pyramid_logging.getLogger('test')

        stream = StringIO.StringIO()
        handler = logging.StreamHandler(stream)
        _log = logging.getLogger('test')
        _log.addHandler(handler)

        log.debug('Hello world')
        self.assertEqual(stream.getvalue(), 'Hello world\n')
        stream.seek(0)
        log.debug('Hello world', request=request)
        self.assertNotEqual(stream.getvalue(), 'Hello world\n')
        self.assertTrue('Hello world\n' in stream.getvalue())
        self.assertTrue('ENVIRONMENT' in stream.getvalue())
        handler.close()
