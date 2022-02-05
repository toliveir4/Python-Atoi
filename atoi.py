import string


def pythonAtoi(s):
    i = pos_i = 0

    # in case the string only has one char, and its not a digit or the string doesnt exists
    if (len(s) == 1 and s not in string.digits) or len(s) < 1:
        return 0

    # go through the string and checks if the char is a digit or not
    while i < len(s):
        if s[i] not in string.digits and s[i] != '+' and s[i] != '-' and s[i] != ' ':
            return 0
        if s[i] in string.digits:
            pos_i = i
            break
        i += 1
    i = pos_i

    j = 0
    while j < pos_i - 1:
        if s[j] != ' ':
            return 0
        j += 1

    while i < len(s) and s[i] in string.digits:
        i += 1
    pos_f = i
    if pos_i == pos_f:
        return 0
    if pos_i - 1 >= 0 and s[pos_i - 1] == '-':
        if -int(s[pos_i:pos_f]) < -2 ** 31:
            return -2 ** 31
        return -int(s[pos_i:pos_f])
    if int(s[pos_i:pos_f]) > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return int(s[pos_i:pos_f])


if __name__ == '__main__':
    print(pythonAtoi("-1343652543"))    # prints -1343652543
    print(pythonAtoi("213433332342"))   # prints 2147483647 (2**31 - 1)
    print(pythonAtoi("-42314554353"))   # prints -2147483648 (-2**31)
