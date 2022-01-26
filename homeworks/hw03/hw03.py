HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if pos == 0:
        return 0
    else:
        return num_eights(pos // 10) + last_is_eight(pos)


def last_is_eight(n):
    """
    >>> last_is_eight(1)
    0
    >>> last_is_eight(18)
    1
    """
    return 1 if n % 10 == 8 else 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if n == 1:
        return 1
    else:
        return pingpong(n - 1) + pingpong_one(n - 1)


def pingpong_one(n):
    if n == 1:
        return 1
    elif n % 8 == 0 or num_eights(n):
        return -pingpong_one(n - 1)
    else:
        return pingpong_one(n - 1)


def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n // 10 == 0:
        return 0
    elif n % 10 > n // 10 % 10 + 1:
        return missing_digits(n // 10) + n % 10 - n // 10 % 10 - 1
    else:
        return missing_digits(n // 10)


def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


from itertools import count


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    """First way, using function ascending_coin"""
    return count_coins_with_ascending_coin(change, 1)
    """Second way, using function descending_coin
    return count_coins_with_descending_coin(change, 25)"""


def count_coins_with_ascending_coin(change, limit):
    """Reference:
    http://composingprograms.com/pages/17-recursive-functions.html#example-partitions"""
    if change == 0:
        return 1
    elif change < 0:
        return 0
    elif limit == None:
        return 0
    else:
        with_limit = count_coins_with_ascending_coin(change - limit, limit)
        without_limit = count_coins_with_ascending_coin(change, ascending_coin(limit))
        return with_limit + without_limit


def count_coins_with_descending_coin(change, limit):
    """Reference:  
    http://composingprograms.com/pages/17-recursive-functions.html#example-partitions"""
    if change == 0:
        return 1
    elif change < 0:
        return 0
    elif limit == None:
        return 0
    else:
        with_limit = count_coins_with_descending_coin(change - limit, limit)
        without_limit = count_coins_with_descending_coin(change, descending_coin(limit))
        return with_limit + without_limit


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if start + end == 3:
        by = 3
    elif start + end == 4:
        by = 2
    else:
        by = 1
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n - 1, start, by)
        move_stack(1, start, end)
        move_stack(n - 1, by, end)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    """
    fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
    s and f -> fact, lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1)))
    v and n -> variables, like 5
    """
    return (lambda s: lambda v: s(s, v))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))