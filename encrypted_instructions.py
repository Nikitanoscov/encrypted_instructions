# 111561518

def decrypted_instructions(instructions: str) -> str:
    steps = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digit = decrypted = ''
    for char in instructions:
        match char:
            case '[':
                steps.append([decrypted, int(digit)])
                digit = decrypted = ''
            case ']':
                previous, number = steps.pop()
                decrypted = previous + decrypted * number
            case _ if char in digits:
                digit += char
            case _:
                decrypted += char
    return decrypted


if __name__ == '__main__':
    print(decrypted_instructions(input()))
