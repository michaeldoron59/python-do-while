from contextlib import contextmanager

@contextmanager
def DoWhile(f):
    def wrapper():
        if wrapper.first_time:
            wrapper.first_time = False
            return True
        else:
            return f()
    wrapper.first_time = True
    yield wrapper
