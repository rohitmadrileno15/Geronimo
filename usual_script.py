# import os
# os.rename(r'C:\coding files\wiki-videos\images\20.jpg',r'C:\coding files\wiki-videos\images\30.jpg')

import wikipedia,os
result = (wikipedia.page("Taylor Swift").content)
 
with open("C:\\coding files\\wiki-videos\\images\\foo.txt", "a" , encoding="utf-8") as f:
    f.write(str(result))

# f_name,f_ext = os.path.splitext("usual_script.py")
# print(f_name)
# print(f_ext)

# from os import walk

# print((os.listdir("wiki-videos")))
    
