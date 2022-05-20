class Logger:
    prefix = ""

    def __init__(self, prefix):
        self.prefix = prefix

    def log(self, msg, **kwargs):
        print("[%s]" % self.prefix, msg, **kwargs)

