
import PIL
import os
import os.path
from PIL import Image

f = r'C:\Users\hp\Desktop\New Projects\Food-calories\Food-Calories-Estimation-Using-Image-Processing-master\train\10'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((32,32))
    img.save(f_img)
#################################    RENAME  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  
import os
path = path=r"C:\Users\hp\Desktop\New Projects\Food-calories\Food-Calories-Estimation-Using-Image-Processing-master\train\10"
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))