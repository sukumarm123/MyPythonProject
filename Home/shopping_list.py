#import read_shopping and write_shopping
import function_shopping


while True:
    user_choice = input("Please enter your choice add, show, edit, complete or exit: ")
    user_choice = user_choice.strip()

    if user_choice.startswith("add"):
        shop = user_choice[4:]
        shop_list = function_shopping.read_shopping()  #read the item name from the txt file
        shop_list.append(shop + '\n')
        function_shopping.write_shopping(shop_list) #add the item name in the txt file
        print("Shopping item is added.")

    elif user_choice.startswith("show"):
        shop_list = function_shopping.read_shopping() #read the item name from the txt file

        for index, item in enumerate(shop_list): #index for numbering the items
            item = item.capitalize().strip('\n') #title to capitalize the first letter andstrip to delet the extra "\n"
            result = f"{index+1}-{item}" #"index+1" to start numbering from 1
            print(result)

    elif user_choice.startswith("edit"):
        try:
            number = int(user_choice[5:])
            index = number - 1 #to match with system numbering as start from '0'

            shop_list = function_shopping.read_shopping()

            new_shop_list = input("Enter the new item name: ")
            shop_list[index] = new_shop_list + '\n'

            function_shopping.write_shopping(shop_list)
            print("Edit successful.")

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])

            shop_list = function_shopping.read_shopping()
            index = number -1
            item_to_remove = shop_list[index].strip('\n')
            shop_list.pop(index)

            function_shopping.write_shopping(shop_list)

            message = f"Item -'{item_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number. Please try another number.")
            continue

    elif user_choice.startswith("exit"):
        break

    else: #for unknowen command
        print("Unknown Command")

print("Thank You")

