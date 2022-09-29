from pathlib import Path
from modules import results
from collections import OrderedDict

def Uniq(file):
    New_filename = results._result(file)
    print(New_filename)
    New_filename = Path(New_filename)
    with open(file, "r+", encoding="utf-8") as _file:
        no_duplicates = OrderedDict.fromkeys(line.rstrip() for line in _file)
        New_filename.write_text("\n".join(no_duplicates))