# 1. Slice off the last digit.  That is the **check digit**.
# 2. Reverse the digits.
# 3. Double every other element in the reversed list.
# 4. Subtract nine from numbers over nine.
# 5. Sum all values.
# 6. Take the second digit of that sum.
# 7. If that matches the check digit, the whole card number is valid.

def is_bool(ccnum):
    ccnumber = [int(x) for x in ccnum]
    check_digit = ccnumber.pop(-1)
    ccnumber2 = ccnumber[::-1]
    ccnumber3 = [ccnumber2[x]*2 if x%2 == 0 else ccnumber2[x] for x in range(len(ccnumber2))]
    ccnumber4 = [ccnumber3[x]-9 if ccnumber3[x]>9 else ccnumber3[x] for x in range(len(ccnumber3))]
    ccnumber5 = sum(ccnumber4)
    ccnumber6 = int(str(ccnumber5)[-1])
    if check_digit == ccnumber6:
        print('VALID CC')
    else:
        print('NOT A GOOD CARD!')


is_bool('4266841445325473')
