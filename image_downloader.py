import requests,os

def dwnld_images(data_img):
    c=1
    for img in data_img:
        img_file_name = str(c) + '.jpg'
        img_data = requests.get(img).content
        with open(r'C:\\coding files\\wiki-videos\\images\\{}'.format(img_file_name), 'wb') as handler:
            handler.write(img_data)
            c+=1
            print('Saved' , img_file_name)

 