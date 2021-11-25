
def print_file(file):
    with open(file, "r") as f:
        f = list(f.read().split(','))
        for x in f:
            print(x)

if __name__ == "__main__":
    print_file("numbers.txt")