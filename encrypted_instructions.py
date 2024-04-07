# 111526356

def decrypted_instructions(instructions: str) -> str:
    steps = []
    digit = ''
    decrypted = ''
    for char in instructions:
        match char:
            case '[':
                steps.extend([decrypted, int(digit)])
                digit = ''
                decrypted = ''
            case ']':
                number = steps.pop()
                previous = steps.pop()
                decrypted = previous + decrypted * number
            case varieble if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                digit += varieble
            case _:
                decrypted += char
    return decrypted


if __name__ == '__main__':
    print(decrypted_instructions(input()))
