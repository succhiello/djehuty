# -*- coding: utf-8 -*-

import abc

from cornice import Service as CorniceService

from thoth.app import App


class Service(CorniceService):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name=None, path=None, description=None, cors_policy=None, depth=1, **kwargs):

        name = name or self.__class__.__name__.lower()

        CorniceService.__init__(
            self,
            name=name,
            path=path or u'/{}'.format(name),
            description=description or u'service for {}'.format(path),
            cors_policy=cors_policy,
            depth=depth + 1,
            validators=self.validate,
            **kwargs
        )

        self.post()(self.__post)

    def validate(self, request):
        pass

    @abc.abstractmethod
    def make_argument(self, request):
        return u''

    @abc.abstractmethod
    def make_response(self, result):
        return {}

    def __post(self, request):
        return self.make_response(App.run_and_get_result(self.make_argument(request)))

