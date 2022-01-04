def run():
    squares = [i*4 for i in range(1,101) if i % 6 == 0 and i % 9 == 0 and i*4 - 10000 <= 0]
    # squares = [i for i in range(1,301) if i - 100 >= 0]
    print(squares)

if __name__ == '__main__':
    run()

