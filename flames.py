global relation


def flame():
    global relation
    print('\n\t\t\t\t  F.L.A.M.E.S.')
    print('\t\t\t\t  ************\n')
    print('\t\t\t\t ______________')
    print('\t\t\t\t|              |')
    print('\t\t\t\t| F = Friend   |')
    print('\t\t\t\t| L = Love     |')
    print('\t\t\t\t| A = Affection|')
    print('\t\t\t\t| M = Marriage |')
    print('\t\t\t\t| E = Enemy    |')
    print('\t\t\t\t| S = Sibling  |')
    print('\t\t\t\t|______________|\n')
    ftname = input("\nEnter the name of person 1 : ")
    sdname = input("\nEnter the name of person 2 : ")
    n1 = list(ftname)
    n2 = list(sdname)
    n1_len = len(n1)
    n2_len = len(n2)
    lists = ['F', 'L', 'A', 'M', 'E', 'S']
    # find flames count ---> starts
    for x in range(n1_len):
        for y in range(n2_len):
            if n1[x] == n2[y]:
                n1[x] = ' '
                n2[y] = ' '
    s = set(n1+n2)
    v1 = list(s)
    length = len(v1) - 1
    # find flames count ---> end
    # remove letter using the flames count --> start
    list2 = lists * (length * length)
    print('\nYour FLAMES Count Is:', length, '\n')
    for z in range(0, 6):
        le = length - 1
        relation = list2[le]
        del list2[0:le]
        for y in list2:
            if y == relation:
                list2.remove(relation)
    # remove letter using the flames count --> end
    if relation == 'F':
        print('Relationship between', ftname, 'and', sdname, 'is : FRIENDS')
        end()
    elif relation == 'L':
        print('Relationship between', ftname, 'and', sdname, 'is : LOVE')
        end()
    elif relation == 'A':
        print('Relationship between', ftname, 'and', sdname, 'is : AFFECTION')
        end()
    elif relation == 'M':
        print('Relationship between', ftname, 'and', sdname, 'is : MARRIAGE')
        end()
    elif relation == 'E':
        print('Relationship between', ftname, 'and', sdname, 'is : ENEMY')
        end()
    elif relation == 'S':
        print('Relationship between', ftname, 'and', sdname, 'is : SIBLINGS')
        end()


def end():
    print('\n1. Retry\n2. Exit')
    opt = int(input('\nEnter your option : '))
    if opt == 1:
        flame()
    elif opt == 2:
        print('\nYou are exited...')
    else:
        print('\nPlease enter valid number...')
        end()


flame()
