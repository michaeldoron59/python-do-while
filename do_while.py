from contextlib import contextmanager

@contextmanager
def DoWhile(f):
    # Code to acquire resource, e.g.:
    def wrapper():
        if wrapper.first_time:
            wrapper.first_time = False
            return True
        else:
            return f()
    wrapper.first_time = True
    yield wrapper
