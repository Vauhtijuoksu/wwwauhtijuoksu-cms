import os
from sys import argv

cwd = os.getcwd()
content = os.listdir(cwd)
me = argv[0].split("/")[-1]
if me in content:
    content.remove(me)
images = []
for file in content:
    if file.endswith(".png"):
        images.append(file)
print(",".join(images))
