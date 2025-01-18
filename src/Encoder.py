from typing import List
import ConwaysGameOfLife as CGoL


def text_to_binary(input_string):
    binary_list: List[List[int]] = [[int(bit) for bit in format(ord(char), '016b')] for char in input_string]
    return binary_list


def binary_to_text(binary_list):
    ascii_string = ''.join(chr(int(''.join(map(str, bits)), 2)) for bits in binary_list)
    return ascii_string


if __name__ == "__main__":
    string = input("Your sentence: ")
    msg = text_to_binary(string)
    for i in range(10):
        msg = CGoL.iterate_board(msg)
        CGoL.draw_board(msg)
    print("Encoded string: ", binary_to_text(msg))


