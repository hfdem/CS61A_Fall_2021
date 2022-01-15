def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        result = n
        while k > 1:
            result = result * (n - 1)
            n = n - 1
            k = k - 1
        return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    l = num_length(y)
    sum = 0 
    while l > 0:
        sum = sum + y // pow(10, l - 1) - y // pow(10, l) * 10
        l = l - 1
    return sum

def num_length(y):
    if y == 0:
        return 0
    else:
        k = 1
        while y // pow(10, k):
            k = k + 1
        return k


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    l = num_length(n)
    numOfEights = 0 
    while l > 0:
        if n // pow(10, l - 1) - n // pow(10, l) * 10 == 8:
            if n // pow(10, l - 2) - n // pow(10, l - 1) * 10 == 8:
                return True
        l = l - 1
    return False

def switch_True_and_False(x):
    if bool(x) == True:
        return False
    else:
        return True

positive = 28
while positive: # If this loops forever, just type Infinite Loop
    print("positive?")
    positive -= 3
    