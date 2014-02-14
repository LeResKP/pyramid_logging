pyramid_logging
===============

Advanced logger for pyramid which add data from the request.

It's very easy to use::

    import pyramid_logging
    log = pyramid_logging.getLogger(__name__)


    def view(request):
        log.debug('Hello world', request=self.request)


The output is the same as pyramid_exclog. Some data added:

    * the URL called
    * The query parameters
    * The environment variables
    * the authenticated user
