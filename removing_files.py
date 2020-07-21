import os

def removing_files():
    print("Removing uneccessary files")

    arr_of_img_files = os.listdir("wiki-videos\\images")
    len_of_files_images = len(arr_of_img_files)
    print(len_of_files_images)
    

    if(len_of_files_images > 1):
        for _ , row_file in enumerate(arr_of_img_files):
            rel_path = "wiki-videos\\images\\"
            f_name,f_ext = os.path.splitext(rel_path + row_file)
            if(f_ext == ".jpg" or f_ext == ".jpeg" or f_ext == ".png" ):
                os.remove(rel_path + row_file)
    print("Done")