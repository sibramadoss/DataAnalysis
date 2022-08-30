# import sympy

# i = 0
# res = []

# while i>=0:
#     if sympy.isprime(i) == True:
#         res.append(i)
#     if len(res) == 20:
#         break
#     i += 1

# print(res)

def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
                if len(prime_list) == 20:
                    break
    return prime_list
 
if __name__ == '__main__':
    starting_range = 1
    ending_range = 100
    lst = prime(starting_range, ending_range)
    if len(lst) == 0:
        print("There are no prime numbers in this range")
    else:
        print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
        print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
        print(lst)