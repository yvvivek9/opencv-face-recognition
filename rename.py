import os
import random
import shutil

photos_path = os.path.join('Photos-Main', 'Suhrid Sen')
std_id = '7777'  # Vaibhav 1234 Kapil 9876 Pratham 3104 Suhrid 7777
image_paths = [os.path.join(photos_path, f) for f in os.listdir(photos_path)]

for path in image_paths:
    img_name = std_id + '.' + str(random.randint(100, 1000000)) + '.jpg'
    img_path = os.path.join('Photos', img_name)
    shutil.copy2(path, img_path)
