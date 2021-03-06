from glob import glob
from converter import Converter
import os
import shutil
directory = str(raw_input("What directory would you like to convert?"))
if directory.endswith("/"):
    files = glob(directory+"*")
else:
    files = glob(directory+"/*")

c = Converter()
if not os.path.exists("converted_files"):
    os.mkdir("converted_files")
for doc in files:
    full_path = c.real_path(doc)
    c.document_to_text(doc,full_path)
    text = doc.split("/")[-1].split(".")[0]+".txt"
    if directory.endswith("/"):
        shutil.move(directory+text,"converted_files/"+text)
    else:
        shutil.move(directory+"/"+text,"converted_files/"+text)
