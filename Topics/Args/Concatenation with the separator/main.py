def concat(*args, sep=" "):
    result = ""
    for i, arg in enumerate(args):
        if i != len(args) - 1:
            result += arg + sep
        else:
            result += arg
    return result
