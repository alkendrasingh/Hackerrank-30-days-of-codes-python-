num_test_case=int(input())

for i in range(num_test_case):
    test_string=input()
    even_index=''
    odd_index=''
    for j in range(len(test_string)):
        if j%2==0:
            even_index +=test_string[j]
        else:
            odd_index +=test_string[j]

    print('{} {}'.format(even_index,odd_index))


