import function_shopping
import PySimpleGUI as ux
import time

ux.theme("DarkBlue3")

clock = ux.Text('', key='clock')

label = ux.Text("Enter your shopping item in the below box")
input_box = ux.InputText(tooltip="Enter an item", key="item")
add_button = ux.Button("Add")

sorted_list = sorted(function_shopping.read_shopping())
list_box = ux.Listbox(values=(sorted_list),
                      key='items',
                      font=('Times New Roman', 15),
                      enable_events=True,
                      size=[40,10])
edit_button = ux.Button("Edit")
exit_button = ux.Button("Exit")
complete_button = ux.Button("Completed")
window = ux.Window('Your Shopping List',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box],
                           [edit_button, complete_button, exit_button]],
                   font=('Times New Roman', 15))


while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("Date - %dth %b,%Y \nTime- %H:%M:%S"), font=('Times New Roman', 12))

    match event:
        case "Add":
            items = function_shopping.read_shopping()
            if values['item']:
                new_item = values['item'] + "\n"
                cap_item = new_item.title()  # capitalize the name of the item
                items.append(cap_item)  # adding to the list
                function_shopping.write_shopping(items)
                window['items'].update(values=items)
                ux.popup("Item Added Successfully.", font=('Times New Roman', 15))
            else:
                ux.popup("No Item Added. Please enter  the item name.", font=('Times New Roman', 15))

        case "Edit":
            try:
                item_to_edit=values['items'][0]
                new_item=values['item']
                cap_item = new_item.title()

                items=function_shopping.read_shopping()
                index=items.index(item_to_edit)
                items[index]=cap_item
                function_shopping.write_shopping(items)
                window['items'].update(values=items)
                ux.popup("Item Edited Successfully.", font=('Times New Roman', 15))

            except IndexError:
                ux.popup("Please select an item first.", font=('Times New Roman', 15))

        case "Completed":
            try:
                item_to_complete=values['items'][0]
                items=function_shopping.read_shopping()
                items.remove(item_to_complete)
                function_shopping.write_shopping(items)
                window['items'].update(values=items)
                window['item'].update(value="")
                ux.popup("Item Removed Successfully.", font=('Times New Roman', 15))

            except IndexError:
                ux.popup("Please select an item first.", font=('Times New Roman', 15))

        case "Exit":
            ux.popup("Thank You.", font=('Times New Roman', 10))
            break

        case ux.WIN_CLOSED:
            ux.popup("Thank You.", font=('Times New Roman', 10))
            break

window.close()