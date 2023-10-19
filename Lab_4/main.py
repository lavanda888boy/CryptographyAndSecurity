from bitarray import bitarray
from numpy import random
import re

def obtain_key_blocks(shifts, permuted_key, block_number: int):
    C = bitarray(permuted_key[:len(permuted_key) // 2])
    D = bitarray(permuted_key[len(permuted_key) // 2:])

    if block_number == 0:
        return C, D
    else:
        index = 0
        while index < block_number:
            if shifts[index] == 1:
                first_bit = C[0]
                C = C << shifts[index]
                C[len(C) - 1] = first_bit

                first_bit = D[0]
                D = D << shifts[index]
                D[len(D) - 1] = first_bit
            else:
                first_bit = C[0]
                second_bit = C[1]
                C = C << shifts[index]
                C[len(C) - 1] = first_bit
                C[len(C) - 2] = second_bit

                first_bit = D[0]
                second_bit = D[1]
                D = D << shifts[index]
                D[len(D) - 1] = first_bit
                D[len(D) - 2] = second_bit
            index += 1
        
        return C, D


def main():
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    permuted_key = []

    option = input('Select the option to generate K+ (randomly-r, manually-m): ')
    if option == 'r':
        permuted_key = re.sub(r'[\[\]]', r'', str(random.randint(2, size=56)))
        print(permuted_key)
    else:
        permuted_key = input('Introduce 56 bits permuted key: ')
    
    block_number = int(input('Introduce the number of block i to obtain Ci and Di: '))
    C, D = obtain_key_blocks(shifts, permuted_key, block_number)
    print(C)
    print(D)


if __name__ == '__main__':
    main()