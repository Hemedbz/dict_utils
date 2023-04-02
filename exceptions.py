class KeyValueError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class IndexValueError(Exception):
    def __init__(self, msg):
        super().__init__(msg)