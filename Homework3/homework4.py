def main():
    # =============================================
    # Булевий тип данних
    my_bool = True

    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2==2
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2==2.0
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2!=2
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2==3
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2!=3
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2>2
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 2>=2
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 21>=2
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_bool = 21>=2
    print('my_bool: ', my_bool)
    new_bool = not my_bool
    print('new_bool: ', new_bool)
    print('type(new_bool): ', type(new_bool))

    my_bool = 21>=22
    print('my_bool: ', my_bool)
    new_bool = not my_bool
    print('new_bool: ', new_bool)
    print('type(new_bool): ', type(new_bool))

    my_int = 1
    print('type(my_int): ', type(my_int))
    my_bool = bool(my_int)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_int = 0
    print('type(my_int): ', type(my_int))
    my_bool = bool(my_int)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_int = None
    print('type(my_int): ', type(my_int))
    my_bool = bool(my_int)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_int = ''
    print('type(my_int): ', type(my_int))
    my_bool = bool(my_int)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_list = [False]
    print('type(my_list): ', type(my_list))
    my_bool = bool(my_list)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    my_dict = {}
    print('type(my_dict): ', type(my_dict))
    my_bool = bool(my_dict)
    print('my_bool: ', my_bool)
    print('type(my_bool): ', type(my_bool))

    #И-И
    df = 1 and False
    print('df: ', df)
    df = False and 1
    print('df: ', df)
    df = False and False
    print('df: ', df)
    df = True and False
    print(type(df))
    print('df: ', df)
    df = False and True
    print('df: ', df)
    df = False and 0
    print('df: ', df)

    df = 2 and 1
    print(f'df: {type(df)}', df)
    #ИЛИ-ИЛИ
    df = 1.2 or False
    print('df: ', df)
    df = False or True
    print('df: ', df)
    df = 1 or 2
    print('df: ', df)


    my_int = -1
    print('bool(my_int): ', bool(my_int))
    print('type(my_int): ', type(my_int))

    my_int = 0.0
    print('bool(my_int): ', bool(my_int))
    print('type(my_int): ', type(my_int))

    list_ = [1, 2, 3, 4, 5]
    print('len(list_): ', len(list_))
    list_ = None
    if not list_:
        print('список имеет значения')
    else:
        print('список не имеет значения')

    list_ = []
    print('len(list_): ', len(list_))
    if list_:
        print('список имеет значения')
    else:
        print('список не имеет значения')


    my_int = -1.7
    print('bool(my_int): ', bool(my_int))
    print('type(my_int): ', type(my_int))

    my_int = 0.
    print('bool(my_int): ', bool(my_int))
    print('type(my_int): ', type(my_int))

    # Зміна точності
    my_float = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    print('bool(my_float): ', bool(my_float))
    print('type(my_float): ', type(my_float))
    print(len('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))

    val_1 = 24.3524634576
    val_2 = 24.3524634575
    print(val_1==val_2)
    print(abs(val_1 - val_2) < 0.0000000001)

    my_str = '1'
    print('bool(my_str): ', bool(my_str))

    my_str = ''
    print('my_str: ', my_str)
    print('len(my_str): ', len(my_str))
    print('bool(my_str): ', bool(my_str))

    my_str = ' '
    print('my_str: ', my_str)
    print('len(my_str): ', len(my_str))
    print('bool(my_str): ', bool(my_str))

    my_none = None
    print('bool(my_none): ', bool(my_none))

    my_str = 'True'
    print('my_str: ', my_str)
    print('type(my_str): ', type(my_str))
    print('bool(my_str): ', bool(my_str))
    my_bool = False
    print('my_bool: ', my_bool)
    my_int = int(my_bool)
    print('my_int: ', my_int)
    print('type(my_int): ', type(my_int))
    my_str = str(my_bool)
    print('my_str: ', my_str)
    print('type(my_str): ', type(my_str))

    my_str = 'False'
    print('my_str: ', my_str)
    print('bool(my_str): ', bool(my_str))
    my_bool = False
    print('my_bool: ', my_bool)
    my_int = int(my_bool)
    print('my_int: ', my_int)
    print('type(my_int): ', type(my_int))
    my_str = str(my_bool)
    print('my_str: ', my_str)
    print('type(my_str): ', type(my_str))
    print('bool(my_str): ', bool(my_str))
    print('type(my_str): ', type(my_str))

    my_val = None
    print('bool(my_val): ', bool(my_val))

    my_val = NotImplemented
    print('type(my_val): ', type(my_val))
    print('bool(my_val): ', bool(my_val))

    my_val = Ellipsis
    print('type(my_val): ', type(my_val))
    print('bool(my_val): ', bool(my_val))


if __name__ == '__main__':
    main()
