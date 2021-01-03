def sum_of_digits(n):
    n = abs(n)
    sum = 0
    while(n > 0):
        sum += n % 10
        n = n // 10

    return sum

def to_digits(n):
    return list(map(lambda x: int(x), list(str(n))))
 

def to_number(digits):
    res = 0
    for x in digits:
        res += x
        res *= 10
    return res//10

def count_vowels(s):
    '''The English vowels are `aeiouy`.'''
    hist = char_histogram(s)
    return hist['a'] + hist['e'] + hist['i'] + hist['u'] + hist['o'] + hist['y'] + hist['A'] + hist['E'] + hist['I'] + hist['U'] + hist['O'] + hist['Y']

def count_consonants(str):
    '''The English consonants are `bcdfghjklmnpqrstvwxz`.'''
    hist = char_histogram(str)
    return hist['b'] + hist['c'] +hist['d'] +hist['f'] +hist['g'] +hist['h'] +hist['j'] +hist['k'] +hist['l'] +hist['m'] +hist['n'] +hist['p'] + hist['q'] +hist['r'] +hist['s'] +hist['t'] +hist['v'] +hist['w'] +hist['x'] +hist['z']+ hist['B'] + hist['C'] +hist['D'] +hist['F'] +hist['G'] +hist['H'] +hist['J'] +hist['K'] +hist['L'] +hist['M'] +hist['N'] +hist['P'] + hist['Q'] +hist['R'] +hist['S'] +hist['T'] +hist['V'] +hist['W'] +hist['X'] +hist['Z']

def prime_number(n):
    is_prime = True
    x = n - 1
    while x > 1:
        if n % x == 0:
            is_prime = False
        x -= 1
    return is_prime


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


def fact_digits(n):
    '''* For example, if n = 145, we want 1! + 4! + 5!'''
    l = to_digits(n)
    sum = 0
    for x in l:
        sum += factorial(int(x))
    return sum


def fibonacci(n):
    '''* Implement a function, called `fibonacci(n)` that returns 
    a list with the first `n` members of the Fibonacci sequence.'''
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def fib_number(n):
    '''For example, if `n = 3`, the result is `112`'''
    l = fibonacci(n)
    s = ""
    i = 0
    while i < n:
        s += str(l[i])
        i += 1
    return int(s)


def palindrome(n):
    s = str(n)
    return s[::] == s[::-1]

def char_histogram(s):
    if s is None:
        raise AttributeError('Function param is None')
    if not isinstance(s, str):
        raise Exception('type is not string')
    from collections import Counter; 
    histogram = Counter(s)
    return histogram