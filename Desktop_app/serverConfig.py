import configparser


class ServerConfig(object):

    _address = ''
    _port = ''

    def __init__(self, file='app.cfg'):
        config = configparser.ConfigParser()
        config.read(file)
        self.load_config(config)

    def load_config(self, conf):
        self._address = conf['SERVER API']['ADDRESS']
        self._port = conf['SERVER API']['PORT']

    def get_server(self):
        return 'http://' + self._address + ':' + self._port
