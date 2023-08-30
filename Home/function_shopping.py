def read_shopping(filepath="shopping.txt"):
    with open(filepath, 'r') as file_local:
        readshopping = file_local.readlines()
    return readshopping


def write_shopping(shop_arg, filepath="shopping.txt"):
    with open(filepath, 'w') as file:
        file.writelines(shop_arg)