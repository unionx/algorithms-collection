#!/usr/bin/env python3

chars = 'A B C D E F G H'
n = 3
base_char_list = chars.split(' ')

def product(acc_list, cnt):
    if cnt == 1:
        return acc_list

    new_acc_list = []
    for acc in acc_list:
        for char in base_char_list:
            new_acc_list.append(acc + char)
    return product(new_acc_list, cnt-1)

if __name__ == '__main__':
    acc_list = product(base_char_list, n)
    for acc in acc_list:
        print(acc)
