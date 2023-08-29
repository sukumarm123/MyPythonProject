name = ["ram","sam","jadu","madhu"]
name.sort()

for index, item in enumerate(name):
    result = f"{index+1}. {item.capitalize()}"
    print(result)