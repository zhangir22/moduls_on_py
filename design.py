def create_menu(data_dictionary,name_menu):
    print("______________________________")
    print(f"___{name_menu}___")
    for i in data_dictionary:
        print(f"'{i}'.{data_dictionary[i]}")
    print("______________________________")
def create_more_chose(data):
    for i in data:
        print(f"'{i}'{data[i]}")
    print("_-__-__-__-__-__-__-__-_")
