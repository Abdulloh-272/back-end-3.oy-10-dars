def open_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())  
    except FileNotFoundError:
        print('FileNotFoundError: Fayl topilmadi!')

open_file('Student.txt')  
open_file('Students.txt')  

def get_value_from_dict(my_dict, key):
    try:
        print(my_dict[key])  
    except KeyError:
        print('KeyError: Lug\'atda bunday kalit yo\'q!')

my_dict = {'a': 1, 'b': 2}
get_value_from_dict(my_dict, 'c') 
get_value_from_dict(my_dict, 'b')