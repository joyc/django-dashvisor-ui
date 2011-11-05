from django.conf import settings

from dashvisor.server import Server



class Backend(object):
    def __init__(self):
        self.servers = {}
        fp = open(settings.DASHVISOR_CONFIG_FILE)
        for line in fp.xreadlines():
            server = Server(line.strip())
            self.servers[server.name] = server
        fp.close()

    def refresh(self):
        for s in self.servers.values():
            s.refresh()

