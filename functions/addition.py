def add(x, y):
    try:
        return int(x) + int(y)
    except Exception:
        return 'invalid input'