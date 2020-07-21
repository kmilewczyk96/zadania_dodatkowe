def closest_power(base, num):
    result = 0
    powered = 0

    while powered < num:
        powered = base ** result
        result = result + 1

    if ((base ** (result - 2)) + powered) / 2 >= num:
        return result - 2

    return result - 1


if __name__ == '__main__':
    assert closest_power(3, 6) == 1
    assert closest_power(4, 12) == 2
    assert closest_power(3, 12) == 2
    assert closest_power(4, 1) == 0
