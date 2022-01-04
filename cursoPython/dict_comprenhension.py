def run():
    my_dict = {i : i**3 for i in range(1,101) if i % 3 != 0}
    #Challenge
    dict_challenge = {i : i**(1/2) for i in range(1,1001)}
    print(dict_challenge)

if __name__ == '__main__':
    run()

