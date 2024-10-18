def print_list(lst):
    for elementes in lst:
        if isinstance(elementes, list):
            print_list(elementes)
        else:
            print(elementes)

def main():
    print_list([1, "a", 2.5, True])
    print_list([0, [1, 2], 3])
    print_list([0, 1, [2, [3, 4]], 5])

main()