import timeit

def add_binary1(a, b):
    s = ""
    c, i, j = 0, len(a) - 1, len(b) - 1
    zero = ord('0')
    while i >= 0 or j >= 0 or c == 1:
        if i >= 0:
            c += ord(a[i]) - zero
            i -= 1
        if j >= 0:
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s
        c //= 2

    return s


def add_binary2(a, b):
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    else:
        a = '0' * (len(b) - len(a)) + a
    carry, res, i, length = 0, '', 0, len(a)
    while i < length:
        num = int(a[length - i - 1]) + int(b[length - i - 1]) + carry
        carry = int(num / 2)
        res = str(num % 2) + res
        i += 1
    if i == length and carry:
        res = '1' + res
    return res


def add_binary3(a, b):
    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        # r can be 0,1,2,3 (carry + a[i] + b[i])
        # and among these, for r==1 and r==3 you will have result bit = 1
        # for r==2 and r==3 you will have carry = 1

        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

def add_binary4(a, b):
    sum = int(a, 2) + int(b, 2)
    if sum == 0:
        return "0"

    out = ''

    while sum > 0:
        res = int(sum) % 2
        out += str(res)
        sum = int(sum/2)

    return out[::-1]


start = timeit.default_timer()
add_binary1('1101', '10011001')
end = timeit.default_timer()
print(str(end-start))

start = timeit.default_timer()
add_binary2('1101', '10011001')
end = timeit.default_timer()
print(str(end-start))

start = timeit.default_timer()
add_binary3('1101', '10011001')
end = timeit.default_timer()
print(str(end-start))

start = timeit.default_timer()
add_binary4('1101', '10011001')
end = timeit.default_timer()
print(str(end-start))