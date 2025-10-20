import os
import random
for i in range (10):
    j =random.choice(["jpg","png","csv","txt"])
    with open (fr".\files\file{i}.{j}","w") as file:
        print(f"File created : file{i}.{j}")
