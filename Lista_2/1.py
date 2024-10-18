def TamString(s):
    cont = 0
    for a in s:
        cont+=1

    return cont

def main():
    s = "Essa vida de merda é uma porra"
    print(TamString(s))

main()