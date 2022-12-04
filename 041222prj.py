import os
import shutil
import cv2

path = "C:/Users/rosan/Downloads/images"

size = ()
out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

listO = os.listdir(path)
images = []
for x in listO:
    name,extension = os.path.splitext(x)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        images.append(path+"/"+name+extension)

for x in range(0, len(images)):
    out.write(images[x].imread())

out.release()