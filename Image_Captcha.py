from captcha import image
import random 
image_info = image.ImageCaptcha(width= 300, height= 150)

L1= "QWERTYUIOPASDFGHJKLZXCVBNM"
L2= "qwertyuiopasdfghjklzxcvbnm"
n = "1234567890"
upper , lower , numbers = 0,1,1
all =""
if upper: 
    all+= L1
if lower:
    all+= L2
if numbers:
    all+=n


for i in range (10):
    captcha_text ="".join(random.sample(all,5))
    source = image_info.generate(captcha_text)
    image_info.write(captcha_text, 'captcha2.png')
    ans = input("type the word  ")
    if ans == captcha_text :
        print("successful attempt")
        break
    else:
        ans= input("try again  ")
