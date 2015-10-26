#! python3
from sys import argv, exit
from pathlib import Path
from collections import defaultdict


def extension_dict():
    return {
        'num_of_files': 0,
        'total_size_of_files': 0,
    }


extensions = defaultdict(extension_dict)

if __name__ == '__main__':
    try:
        path = argv[1]
    except IndexError:
        print('usage: ext_info <path>')
        exit()
    folder = Path(path)
    for fl in [x for x in folder.iterdir() if x.is_file()]:
        ext = fl.suffix.split('.')[-1] or '.'   # removes leading dot.
        extensions[ext]['num_of_files'] += 1
        extensions[ext]['total_size_of_files'] += fl.stat().st_size

    for ext, info in sorted([(x, y) for x, y in extensions.items()], key=lambda x: x[0]):
        print(ext, info['num_of_files'], info['total_size_of_files'])
