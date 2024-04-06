from typing import Union


def decrypted_instructions(instructions: str):
    steps: list[Union[int, str]] = []
    digit = 0
    decrypted_str = ''
    for elem in instructions:
        if elem.isdigit():
            digit = digit * 10 + int(elem)
        elif elem == '[':
            steps.append(decrypted_str)
            steps.append(digit)
            digit = 0
            decrypted_str = ''
        elif elem == ']':
            number = steps.pop()
            previous_string = steps.pop()
            decrypted_str = previous_string + (decrypted_str * number)
        else:
            decrypted_str += elem
    return decrypted_str


if __name__ == '__main__':
    encrypted_intrusion = input()
    print(decrypted_instructions(encrypted_intrusion))

