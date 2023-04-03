from Calculator import calc


def main():
    my_primer = input("Введите выражение: ").split()
    print(my_primer)

    while "*" in my_primer or "/" in my_primer:
        for i in range(1, len(my_primer), 2):
            if my_primer[i] in ("*", "/"):
                my_primer[i-1] = calc(my_primer[i-1],
                                      my_primer.pop(i+1), my_primer.pop(i))
                break


    while "+" in my_primer or "-" in my_primer:
        for i in range(1, len(my_primer), 2):
            if my_primer[i] in ("+", "-"):
                my_primer[i-1] = calc(my_primer[i-1],
                                    my_primer.pop(i+1), my_primer.pop(i))
            break
    print(my_primer)

if __name__ == "__main__":
    main()
