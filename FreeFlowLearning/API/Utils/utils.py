from FreeFlowLearning.API.Errors.errors import Error


def attempt(func, error, level):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except error as e:
            Error(e, level)
    return inner


def string_quotes(string):
    if type(string) != str:
        return string
    return f"'{string}'"
