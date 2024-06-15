class Size:

    def __init__(self, size: int):
        self.b = size
        self.kb = round(self.b / 1024, 2)
        self.mb = round(self.kb / 1024, 2)
        self.gb = round(self.mb / 1024, 2)

    @property
    def proper(self) -> str:
        if self.gb > 1:
            return '<{} GB)>'.format(self.gb, self.b)
        elif self.mb > 1:
            return '<{} MB)>'.format(self.mb, self.b)
        elif self.kb > 1:
            return '<{} KB>'.format(self.kb, self.b)
        else:
            return '<{} b>'.format(self.b)

    def __repr__(self):
        return self.proper
