#  Author: Francisco Jose Contreras Cuevas
#  Office: Senior VFX Compositor & 3D FX Artist
#  Website: videovina.com

import json
import os
import random
import string
import subprocess


def sh(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode(), err


def fwrite(file, date):
    f = open(file, "w")
    f.write(date)
    f.close()


def fread(file):
    f = open(file, "r")
    readed = str(f.read().strip())
    f.close()

    return readed

def jread(file):
    return json.loads(fread(file))


def jwrite(file, data):
    info = json.dumps(
        data,
        indent=4,
    )

    fwrite(file, info)


def hash_generator(keyLen):
    def base_str():
        return (string.ascii_letters + string.digits)

    keylist = [random.choice(base_str()) for _ in range(keyLen)]
    return ("".join(keylist))


def makedirs(_dir):
    if not os.path.isdir(_dir):
        os.makedirs(_dir)


def makedir(_dir):
    if not os.path.isdir(_dir):
        os.mkdir(_dir)
