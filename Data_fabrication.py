import numpy as np
import random
import cv2
import os
from PIL import Image, ImageFont, ImageDraw


def generate_random_string():
    # list=['*MRP NPR 200', '20 off - NPR 180/-', '4 Nos x 100g=400g', 'SAVE NPR 20 on 4Nos', '#16/06/24 B1']
    line1=f'*MRP NPR {random.randrange(200,250)}'
    line2=f'#{random.randrange(1,30)}/{random.randrange(1,12)}/24 B1'
    line3=f'a'
    list=[line1,line2,line3]
    characters = random.choice(list).split(" ")
    # print(characters)
    
    rand_guess=random.choices([0,1],weights=(0.6,0.4))[0]  #randomness control parameter with weights assigned
    
    if rand_guess==0:
        guess=random.choices([0,1],weights=(0.6,0.4))[0]
        if guess==0:
            sequence_dum=random.choice(characters)
            sequence=random.choice(sequence_dum)   #responsible for single character print
            
        else:
            sequence=random.choice(characters)     #responsible for single chunks of character print 
        
    else:
        choice1=random.choice(characters) 
        choice2=random.choice(characters)
        choice3=random.choice(characters) 

        if choice1 == choice2 or choice1 == choice3 or choice2 == choice3:
            sequence=choice1
        else:
            rand_gues=random.choices([0,1],weights=(0.8,0.2))[0]
            if rand_gues==0:
                sequence=choice1+' '+choice2           #responsible for double chunks of character print 
            else:
                sequence=choice1+' '+choice2+' '+choice3   #responsible for triple chunks of character print 
    return  sequence


# def generate_random_string():
#     characters = '*MRP Rs. 250/-'
#     # rand_guess=random.randrange(0,2)
#     # if rand_guess==0:
#     #     sequence=random.choice(characters)
#     # else:
#     #     sequence=random.choice(characters)+' '+random.choice(characters)
#     return  characters

path="test.jpg"    #blank image path
ouput_text="./ouput"  #output folder for result
for a in range(0,10):
    image = Image.open(path) 

    draw = ImageDraw.Draw(image) 
    font = ImageFont.truetype(r"D:\computervision\PaddleOCR\fonts\fonts\inkjet\MerchantCopyDoublesize-jE7R.ttf", 30)
    #font=(text_font,text_size)

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
        draw.text((50, 19+i*60), text, fill=(0, 0, 0), font = font,spacing=20)   #place for display text
        # draw.rectangle((250-10,90+i*60,text_width+250,text_height+(10+90+i*60)),outline="yellow")
    # image.show()

    img_name=path.split(".")[0]
    
    img = np.array(image)
    img1=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    base_path=os.getcwd()
    text_path=os.path.join(base_path,ouput_text)
    # print(i)
    cv2.imwrite(text_path+f"/{img_name}_{a}.jpg",img1)
    # u=f"/{img_name}_{a}.txt"
    u=f"/{img_name}.txt"
    with open(text_path+u, 'a') as file:
        file.write(f'{img_name}_{a}.jpg,"{text}"\n')
    # cv2.imshow("image",img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # exit()




