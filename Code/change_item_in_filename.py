filenames = ["1.bengali.txt","2.english.txt","3.geography.txt"]

for filename in filenames:
    filename=filename.replace('.','-',1)
    print(filename)