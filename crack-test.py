from crack import crack

#TESTS

def print_args(crack):
    print(crack.config)

def main():
    c = crack()
    print_args(c)

if __name__ == "__main__":
    main()
