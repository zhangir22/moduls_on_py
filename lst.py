import random as rnd
def show_list(lst):
    for i in lst:
        print(i,end=" | ")
    print("\n")
#
def join_array_to_dictionary(arr,arr1):
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = arr1[i]
    return d
#
def create_dictionary(array):
    values = dict()
    for i in range(len(array)):
        values[i] = array[i]
    return values
#
def show_keys(dictionary):
    for i in dictionary:
        print(i)
#
def show_dictionary(dictionary):
    for i in dictionary:
        print(f"{i} = {dictionary[i]}")
#
def __find_key(dictionary, value):
    for i in dictionary:
        if dictionary[i] == value:
            return i
#
def __check_key(dictionary,value):
    return value in dictionary
#
def find_element_dict(dictionary,value):
    for i in dictionary:
        if dictionary[i]==value:
            return True
    return False
#
def add_more_elements(lst,values):
    for i in values:
        lst.append(i)
#
def add_element(lst,value):
    lst.append(value)
#
def update_dictionary(dictionary,key,value):
    if key:
        if value:
            dictionary.update(key,value)
    else:
        return "Параметры были проигнорированы"
#
def add_inside(lst,index,value):
    if index>0 and index < len(lst):
        lst.insert(index,value)
#
def remove_element(lst,index):
    if index!=None or index>=0 and index<len(lst):
        lst.pop(index)
#
def get_key_dictionary(dictionary,key):
    for i in dictionary:
        if i == key:
            return i
    return "Такого ключа нет"
#
def get_keys_dictionary(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    return keys
#
def find_duplicate(lst,value):
    indexes = []
    for i in range(len(lst)):
        if value == lst[i]:
            indexes.append(i)
    return indexes
#
def join_list(lst,value):
    lst.extend(value)
#
def find_element(lst,value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
#
def sorted_buble(values):
    for i in range(len(values)):
        for y in range(len(values) - 1, i ,-1):
            index = y - 1
            if values[index] > values[y]:
                values[index],values[y] = values[y],values[index]
    return values
#
def sorted_chose(values):
    for i in range(len(values)):
        index = len(values)
        j = index - 1
        while index > 0 and j > 0:
            index-=1
            j -=1
            if values[index] < values[j] or values[index] == values[j]:
                values[j],values[index] = values[index],values[j]
        index-=i
    return values
#
def create_list(count_elements,min_number,max_number):
    lst = []
    for i in range(count_elements):
        lst.append(rnd.randint(min_number,max_number))
    return lst
#
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
