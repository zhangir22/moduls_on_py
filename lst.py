import random as rnd
def show_list(lst):
    for i in lst:
        print(i,end=" ,")
    print("\n")
def sorted_buble(values):
    for i in range(len(values)):
        for y in range(len(values) - 1, i ,-1):
            index = y - 1
            if values[index] > values[y]:
                values[index],values[y] = values[y],values[index]
    return values
def create_list(count_elements):
    lst = []
    max_number = 100
    for i in range(count_elements):
        lst.append(rnd.randint(1,max_number))
    return lst
def search_binary(lst,user_number):
    def cut_number(value_a, value_b):
        cut = 2
        return (value_a + value_b) // cut
    max = len(lst)
    min = 0
    id = 0
    while id<0:
        id = cut_number(max, min)
        if user_number == lst[id]:
            return user_number
        if user_number < lst[id]:
            max = id
        if user_number > lst[id]:
            min = id
    for i in range(min, max):
        if lst[i]==user_number:
            return i
