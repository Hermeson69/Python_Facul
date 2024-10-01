def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input('Digite: '))
    num2 = int(input('Digite: '))

    for n in range(num, num2 + 1):
        print(primo(n))

main()