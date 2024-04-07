# 111565121

import string


def decrypted_instructions(instructions: str) -> str:
    steps = []
    multiplier = decrypted = ''
    for char in instructions:
        match char:
            case '[':
                steps.append((decrypted, int(multiplier)))
                multiplier = decrypted = ''
            case ']':
                prev_decrypted, prev_multiplier = steps.pop()
                decrypted = prev_decrypted + decrypted * prev_multiplier
            case _ if char in string.digits:
                multiplier += char
            case _:
                decrypted += char
    return decrypted


if __name__ == '__main__':
    print(decrypted_instructions(input()))
