## Universal, multiplatform implementation of "split" command in linux
## Author: Zachery Utt (1/29/2022)

from os.path import join
from encodeAgent import decode
import zipfile
import os

def build():
    os.system("unzip " + "\"" + join("zip", "qemu-arm-img.zip") + "\"")

def sysPerms():
	os.system("chmod +x " + "\"" + join("sim", "Unix Scripts", "connect.sh") + "\"")
	os.system("chmod +x " + "\"" + join("sim", "Unix Scripts", "connect.sh") + "\"")
	os.system("chmod +x " + "\"" + join("sim", "Unix Scripts", "connect.sh") + "\"")

if __name__ == "__main__":
    decode()
    build()
    sysPerms()