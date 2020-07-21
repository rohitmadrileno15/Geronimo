from os import listdir
from os.path import isfile, join
import os
import cv2
import numpy as np
import math

def make_video(input_img_folder = "C:\\coding files\\wiki-videos\\images" , output_inbetween_frame_delay = 3):
    # setup variables from comman line arguments
     
    output_frame_width = 1024
    output_frame_height = 1024
    output_frame_background_colour = '000000'

    output_initial_frame_delay = 2

    output_final_frame_delay = 2

    output_video_format = str("mp4v")
    output_video_filename = "C:\\coding files\\wiki-videos\\images\\video.avi"
    output_video_fps = 0.07

    print('Constructing video ...')

    # get the images and sort into order
    imgs = [f for f in listdir(input_img_folder) if isfile(join(input_img_folder, f))]
    imgs.sort()

    # setup the video write
    fourcc = cv2.VideoWriter_fourcc(*output_video_format) 
    video = cv2.VideoWriter(output_video_filename, fourcc, output_video_fps, (output_frame_width, output_frame_height))

    # setup for telling the user what the nearest 10% of the video construction is done - 10%, 20% etc
    percent_marks_used = dict()
    for pm in np.linspace(10, 100, 10):
        percent_marks_used[int(pm)] = 0

    for img_counter in range(len(imgs)):
        try:
            # 'ui' for telling the user what the nearest 10% of the video construction is done - 10%, 20% etc
            percent_done = (float(img_counter+1) / float(len(imgs))) * 100
            ten_percent_floor = int(math.floor(percent_done / 10))*10
            if ten_percent_floor in percent_marks_used and percent_marks_used[ten_percent_floor] == 0:
                print(str(ten_percent_floor) + '%')
                percent_marks_used[ten_percent_floor] = 1

            # read the next image to create a new frame
            img = cv2.imread(input_img_folder + '\\' + imgs[img_counter],1)
            img_height, img_width, c = img.shape

            # find the image's largest dimension size (either width or height)
            # and the corresponding dimensions size for the frame that's about to be constructed from the image
            img_largest_dimension_size = img_width
            output_frame_corresponding_dimension_size = output_frame_width
            if img_height > img_width:
                img_largest_dimension_size = img_height
                output_frame_corresponding_dimension_size = output_frame_height

            # determine the ratio between these two sizes and use the ratio to resize the original image 
            # so that it will fit inside the frame
            ratio = (float(img_largest_dimension_size) / float(output_frame_corresponding_dimension_size))
            img_new_width = math.floor(float(img_width) / float(ratio))
            img_new_height = math.floor(float(img_height) / float(ratio))
            img_resize = cv2.resize(img, (img_new_width, img_new_height)) 
            
            # create a blank frame and fill with whatever frame background colour as been provided
            frame = np.zeros(shape=[output_frame_width, output_frame_height, 3], dtype=np.uint8)
            rgb = tuple(int(output_frame_background_colour[i:i+2], 16) for i in (0, 2, 4))
            frame[:,:] = (rgb[2], rgb[1], rgb[0]) # B G R

            # the resized image may not fit perfectly inside the video frame
            # work out the x and y offsets that are needed to centre the resized image within the frame
            img_resize_offset_x = int(math.floor(float(output_frame_width) / float(2)) - (float(img_resize.shape[1]) / float(2)))
            img_resize_offset_y = int(math.floor(float(output_frame_height) / float(2)) - (float(img_resize.shape[0]) / float(2)))

            # copy the resized image into the frame, using the offsets to centre
            frame[img_resize_offset_y:img_resize.shape[0]+img_resize_offset_y, img_resize_offset_x:img_resize.shape[1]+img_resize_offset_x] = img_resize[:,:]
            
            # fake any of the delays by just writing the frame multiple times to the video
            if img_counter == 0:
                for i in range(0, output_initial_frame_delay):
                    video.write(frame)
            elif img_counter == len(imgs) - 1:
                for i in range(0, output_final_frame_delay):
                    video.write(frame)
            else:
                for i in range(0, output_inbetween_frame_delay):
                    video.write(frame)
            
        except:
            print("error")
        

    # tidy the video and output
    cv2.destroyAllWindows()
    video.release()

    print('... completed')

# make_video()        
