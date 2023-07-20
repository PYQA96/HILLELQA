def transform_with_map(val: list):
    temponary_values = list(map(lambda x: str(x) if isinstance(x, int) and not isinstance(x, bool) else x, val))
    return temponary_values


value = [1, 2, '3', 'forth', 'end', 99, True, None]
answer=transform_with_map(value)
print(answer)

