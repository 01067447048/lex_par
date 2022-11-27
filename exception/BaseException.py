class JSyntaxError(BaseException):
    pass

class JParseError(BaseException):
    pass

class JRuntimeError(BaseException):
    pass

class JFileReadError(BaseException):
    pass

class JFileWriteError(BaseException):
    pass

class ReturnTrigger(JRuntimeError):
    def __init__(self, value):
        self.value = value