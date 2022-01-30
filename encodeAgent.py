## Universal, multiplatform implementation of "split" command in linux
## Author: Zachery Utt (1/29/2022)

import sys
from os.path import isfile, join

def encode():
    fileNum = 0
    try:
        with open(join("whole", "qemu-arm-img.zip"), "rb") as file:
            bytes = file.read(1000000)  # 1 MB
            while bytes:
                with open(join("parts", "{}.data".format(fileNum)), "wb") as file2:
                    file2.write(bytes)
                bytes = file.read(1000000)  # 1 MB
                fileNum += 1
    except:
        print("Please download qemu-arm-img.zip into ./whole folder")
        exit()

from os import listdir


def decode():
    parts = [f for f in listdir("parts") if isfile(join("parts", f))]
    indicies = []
    for part in parts:
        indicies.append(int(part[:part.index(".")]))
    indicies = sorted(indicies)

    with open(join("zip", "qemu-arm-img.zip"), "wb") as file:
        for index in indicies:
            with open(join("parts", "{}.data".format(index)), "rb") as file2:
                bytes = file2.read(1000000)  # 1 MB
                while bytes:
                    file.write(bytes)
                    bytes = file2.read(1000000)  # 1 MB

def verify():
    with open(join("zip", "qemu-arm-img.zip"), "rb") as file:
        with open(join("whole", "qemu-arm-img.zip"), "rb") as file2:
            bytes = file.read(1000000)  # 1 MB
            bytes2 = file2.read(1000000)  # 1 MB

            while bytes:
                if bytes != bytes2:
                    return False
                bytes = file.read(1000000)  # 1 MB
                bytes2 = file2.read(1000000)  # 1 MB
            bytes = file.read(1000000)  # 1 MB
            bytes2 = file2.read(1000000)  # 1 MB

            if bytes != bytes2:
                return False

            return True


if __name__ == "__main__":
    print(verify())