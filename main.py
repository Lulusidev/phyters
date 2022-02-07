#!/usr/bin/env python3

import sys
from lib import *
from utils import *

def main():
    
    for i in range(len(sys.argv)):
        if sys.argv[i] in ["-h","--help"]:
            helpmsg(2)

    if len(sys.argv)!=4:
        print("Usage: python filters.py FILTER image_path output")
        sys.exit(1)
      
    #local vars with argvs cli
    file = sys.argv[2]
    filter_user = sys.argv[1]    
    path_file = sys.argv[3]
    
    #flagment file name in filename ext and path of file        
    file_without_ext,ext,path = get_filename_and_ext(file)

    match ext :
        case ".png":
            image_type = "PNG"
        case ".jpg" :
            image_type = "JPEG"
        case ".bmp":
            image_type = "BMP"
    
    str_filter = treat_filtername(filter_user)

    if filter_user in ["-gray","--gray","gray"]:
        image = to_gray(file)
   
    elif filter_user in ["-selfia","--selfia","selfia"]:
        image = to_selfia(file)
 
    elif filter_user in ["-purple","--purple","purple"]:
        image = to_purple(file)
    
    elif filter_user in ["-neg","--neg","neg"]:
        image = to_negative(file)
    
    elif filter_user in ["-blur","--blur","blur"]:
        image = to_blur(file)
    
    else :
        print("ERROR : Filter not Found")
        helpmsg(3)

    image.save(f"{path_file}/{file_without_ext}_{str_filter}{ext}",image_type)
 
    sys.exit(0)
    
if __name__ == "__main__":
    main()
