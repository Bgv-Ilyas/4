if __name__ == '__main__':
    k = int(input('Enter k from 1 to 180: '))
    pair_num = k // 2
    num = pair_num + 10
    digit_position = 0

    if k % 2 != 0:
        pair_num += 1
        digit_position = k % 2
    else:
        num -= 1
    
    k_digit = str (num)[0] if digit_position != 0 else str (num)[1]
    print (f'Pair: {pair_num}')
    print (f'Num: {num}')
    print (f'K-th digit {k_digit}')