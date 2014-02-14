import logging
from pprint import pformat
from pyramid.security import unauthenticated_userid


def _get_url(request):
    try:
        url = request.url
    except UnicodeDecodeError:
        # do the best we can
        url = (request.host_url +
               request.environ.get('SCRIPT_NAME') +
               request.environ.get('PATH_INFO'))
        qs = request.environ.get('QUERY_STRING')
        if qs:
            url += '?' + qs
        url = 'could not decode url: %r' % url
    return url

_MESSAGE_TEMPLATE = """

%(url)s

ENVIRONMENT

%(env)s


PARAMETERS

%(params)s


UNAUTHENTICATED USER

%(usr)s

"""


def _get_message(request):
    url = _get_url(request)
    unauth = unauthenticated_userid(request)

    try:
        params = request.params
    except UnicodeDecodeError:
        params = 'could not decode params'

    return _MESSAGE_TEMPLATE % dict(
        url=url,
        env=pformat(request.environ),
        params=pformat(params),
        usr=unauth if unauth else '')


class PyramidLoggingAdapter(logging.LoggerAdapter):
    """We get the data from the request to have a complete message
    """
    def process(self, msg, kw):
        if 'request' not in kw:
            return msg, kw
        message = _get_message(kw.pop('request'))
        return '%s %s' % (message, msg), kw


def getLogger(name):
    """Create an adapter on the logger and returns it.
    """
    log = logging.getLogger(name)
    adapter = PyramidLoggingAdapter(log, {})
    return adapter
