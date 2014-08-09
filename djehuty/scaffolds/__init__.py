from pyramid.scaffolds import PyramidTemplate


class ServerTemplate(PyramidTemplate):
    _template_dir = 'server'
    summary = 'djehuty server project'


class ServiceTemplate(PyramidTemplate):
    _template_dir = 'service'
    summary = 'djehuty service project'
