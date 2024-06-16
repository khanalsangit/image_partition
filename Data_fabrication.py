import numpy as np
import random
import cv2
import os
from PIL import Image, ImageFont, ImageDraw


def generate_random_string():
    list=['*MRP Rs. 250/-', '#26/06/23 A 005', '##NET VOL.200ML']
    characters = random.choice(list).split(" ")
    
    rand_guess=random.choices([0,1],weights=(0.7,0.3))[0]
    # print(rand_guess)
    if rand_guess==0:
        guess=random.choices([0,1],weights=(0.7,0.3))[0]
        if guess==0:
            sequence_dum=random.choice(characters)
            sequence=random.choice(sequence_dum)
        else:
            sequence=random.choice(characters)
        
    else:
        choice1=random.choice(characters) 
        choice2=random.choice(characters) 

        if choice1 == choice2:
            sequence=choice1
        else:
            sequence=choice1+' '+choice2
    return  sequence


# def generate_random_string():
#     characters = '*MRP Rs. 250/-'
#     # rand_guess=random.randrange(0,2)
#     # if rand_guess==0:
#     #     sequence=random.choice(characters)
#     # else:
#     #     sequence=random.choice(characters)+' '+random.choice(characters)
#     return  characters
path="test.jpg"
ouput_text="./ouput"
for a in range(0,10):
    image = Image.open(path) 

    draw = ImageDraw.Draw(image) 
    font = ImageFont.truetype(r"D:\computervision\PaddleOCR\fonts\fonts\inkjet\MerchantCopyDoublesize-jE7R.ttf", 30) 
# img = np.array(image)
# omg=cv2.imread("pink_blank.jpg")
# cv2.imshow("image",omg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

    for i in range(0,1):
        text = generate_random_string()
        # print(text)
        
        # bbox = font.getbbox(text)    #getbbox() method returns a tuple (left, top, right, bottom)
        # text_width = bbox[2] - bbox[0]
        # text_height = bbox[3] - bbox[1]
        draw.text((50, 19+i*60), text, fill=(0, 0, 0), font = font,spacing=20)   #(84, 55, 60)
        # draw.rectangle((250-10,90+i*60,text_width+250,text_height+(10+90+i*60)),outline="yellow")
    # image.show()

    img_name=path.split(".")[0]
    
    img = np.array(image)
    img1=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    base_path=os.getcwd()
    text_path=os.path.join(base_path,ouput_text)
    # print(i)
    cv2.imwrite(text_path+f"/{img_name}_{a}.jpg",img1)
    u=f"/{img_name}_{a}.txt"
    with open(text_path+u, 'w') as file:
        file.write(f'{img_name}_{a}.jpg,"{text}"')
    # cv2.imshow("image",img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # exit()




