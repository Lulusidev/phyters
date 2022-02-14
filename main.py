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
    filter_user = sys.argv[1] 
    file = sys.argv[2]
    path_file = sys.argv[3]
    
    #flagment file name in filename ext and path of file        
    file_without_ext,ext,path = get_filename_and_ext(file)
    
    #if ext == ".jpg" image_type = "JPEG" else image_type = ext[1:].upper()
    image_type = "JPEG" if ext==".jpg" else ext[1:].upper()
    
    #open menu
    if sys.argv[1] == "menu":
        filter_user = menu()

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
    
    elif filter_user in ["-spurple","--spurple","spurple"]:
        image = to_selfia_purple(file)
    
    elif filter_user in ["-lut","--lut","lut"]:
        R,G,B = get_RGB() 
        image = to_lut_hexa(file,R,G,B)
      
    elif filter_user in ["-green","--green","green"]:
        image = to_green(file) 

    else :
        print("ERROR : Filter not Found")
        helpmsg(3)

    image.save(f"{path_file}/{file_without_ext}_{str_filter}{ext}",image_type)
 
    sys.exit(0)
    
if __name__ == "__main__":
    main()
