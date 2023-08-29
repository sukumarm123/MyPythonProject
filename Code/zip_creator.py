import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)
            #filepath = pathlib.Path(filepath)
            #archive.write(filepath, arcname=filepath.name)



if __name__ == "_main__":
    make_archive(filepaths=["ex2.py", "ex3.py"], dest_dir="dest")