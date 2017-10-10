def retry(func):
    max_retries = 10

    def wrapper(*args, **kwargs):
        for i in range(max_retries, 0, -1):
            try:
                print('RETRY', i)
                return func(*args, **kwargs)
            except (Exception,)[:i - 1]:
                pass

    return wrapper


@retry
def foo():
    raise ValueError


foo()
