from PIL import Image
import os.path

dir = r"D:\MachineOnJS\kimtaenim.github.io\mult"

files = os.listdir(dir)
print(files)

for file in files :
    image = Image.open(f'D:\MachineOnJS\kimtaenim.github.io\mult\{file}')
    print(image.filename)
    print(image.size)
    
    image=image.resize((128, 128))
    image.save(f'D:\MachineOnJS\kimtaenim.github.io\mult\{file}')
    print(image.size)
    image.close()