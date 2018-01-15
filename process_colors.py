#C:\Users\Aaron\Desktop\Progs\Python 3.6

import os
import random


with open(r"C:\Users\Aaron\Desktop\Progs\Python 3.6\color_list.txt") as f:
        for line in f:
            print (random.choice(line))

