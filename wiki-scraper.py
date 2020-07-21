import wikipedia,os
from change_audio import change_text
from playsound import playsound
from image_downloader import dwnld_images
from add_audio_video import add_audio_and_video
from add_images import make_video
from removing_files import removing_files
from os import walk

import pyfiglet 
  
result = pyfiglet.figlet_format("Geronimo", font = "slant"  ) 
print(result) 

search_data = str(input("Type in a Search Term\n"))


image_links = (wikipedia.page(search_data).images)

try:
    image_links = image_links[0:30]
except:
    print("Try another term")
    

# print(image_links)
dwnld_images(image_links)



title_page = wikipedia.page(search_data).title
print(title_page)

result = (wikipedia.page(search_data).content)

finalresult = "Hey! This is an automated video made by Rohit Saha .... \n "  +  result

file_name = change_text(search_data , ("".join(list(result)[0:5000])) )

make_video('C:\\coding files\\wiki-videos\\images' , 3 )
    
add_audio_and_video("C:\\coding files\\wiki-videos\\images\\video.avi"  , file_name , "C:\\coding files\\wiki-videos\\images\\output.mp4")



removing_files()
print("Generated!!!" )
# playsound(file_name)

 


