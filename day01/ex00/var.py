
def print_var(var):
    print(f'{var} has a type ', type(var))

def my_var():
    var_int = 42
    print_var(var_int)
    var_str = '42'
    print_var(var_str)
    var_str2 = 'quarante-deux'
    print_var(var_str2)
    var_float = 42.0
    print_var(var_float)
    var_bool = True
    print_var(var_bool)
    var_list = [42]
    print_var(var_list)
    var_dict = {42 : 42}
    print_var(var_dict)
    var_tuple = (42,)
    print_var(var_tuple)
    var_set = set()
    print_var(var_set)

if __name__ == '__main__':
    # my_var()
    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
    #  if x % 2 == 0 фильтр
    #  if if x < 0 else x**2 фильтр

