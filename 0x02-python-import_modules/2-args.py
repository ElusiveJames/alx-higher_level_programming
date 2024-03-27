#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    if len(sys.argv[1:]) == 1:
        print(f"{len(sys.argv[1:])} argument:\n1: {sys.argv[1]}")
    elif len(sys.argv[1:]) > 1:
        print(f"{len(sys.argv[1:])} arguments:")
        while count <= len(sys.argv[1:]):
            print(f"{count} : {sys.argv[count]}")
            count += 1
    else:
        print("0 arguments.")
