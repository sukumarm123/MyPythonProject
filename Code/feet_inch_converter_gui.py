import PySimpleGUI as py

f_label = py.Text("Enter feet")
f_input = py.Input(key="feet")

i_label = py.Text("Enter inches")
i_input = py.Input(key="inches")

convert_button = py.Button("Convert")
exit_button = py.Button("Exit")
output_label = py.Text("", key="output")

Layout = [[f_label, f_input], [i_label, i_input], [convert_button, exit_button, output_label]]

window = py.Window("Converter", layout=[Layout])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])

                result = feet * 0.3048 + inches * 0.0254
                window["output"].update(value=f"{result} m", text_color="Black")

            except ValueError:
                py.popup("Enter the blank space value.")

        case "Exit":
            py.popup("Thank You.")
            break



window.close()