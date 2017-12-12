class Program:
    def __init__(self, id):
        self.id = int(id)
        self.links = []

    def add_link(self, prog):
        if prog.id is not self.id:
            self.links.append(prog)

    def connected(self, id, ignore=[]):
        if self.id == id:
            return True, ignore
        else:
            for link in self.links:
                if link is not self:
                    if link.id not in ignore:
                        ig = ignore[:]
                        ig.append(self.id)
                        connected, ig = link.connected(id, ig)
                        if connected:
                            return True, ig

        return False, ignore

    def __str__(self):
        return "Id: " + str(self.id)