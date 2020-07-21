def general_poly(L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10 ^0
    """
    k = len(L)
    new_list = []

    def new_function(x):
        for i in L:
            new_list.append(i*(x**(k-i)))
        return sum(new_list)

    return new_function

if __name__ == '__main__':
    assert general_poly([1, 2, 3, 4])(10) == 1234

