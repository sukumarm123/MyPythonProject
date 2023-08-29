contents = ["This is an improtant documents.",
            "This report is very improtant.",
            "The presentation was very good."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
