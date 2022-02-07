import sys
from filters import *

def main():
    if len(sys.argv)!=3:
        print("Usage: python filters.py FILTER image_path")
        sys.exit(1)
    
    file = sys.argv[2]
    filter_user = sys.argv[1]    
    
    file_without_ext,ext = get_filename_and_ext(file)
    
    match ext :
        case ".png":
            image_type = "PNG"
        case ".jpg" :
            image_type = "JPEG"
        case ".bmp":
            image_type = "BMP"

    if filter_user in ["-g","-gray","gray"]:
        image = black_and_white(file)
        image.save(file_without_ext+"_GRAY"+ext,image_type)
        
        sys.exit(0)
    
    elif filter_user in ["-s","-selfia","selfia"]:
        image = to_selfia(file)
        image.save(file_without_ext+"_SELFIA"+ext,image_type)

        sys.exit(0)
 
    elif filter_user in ["-p","-purple","purple"]:
        image = to_purple(file)
        image.save(file_without_ext+"_PURPLE"+ext,image_type)

        sys.exit(0)
    
    elif filter_user in ["-n","-neg","negative"]:
        image = to_negative(file)
        image.save(file_without_ext+"_NEG"+ext,image_type)

        sys.exit(0)
    
    elif filter_user in ["-b","-blur","blur"]:
        image = to_blur(file)
        image.save(file_without_ext+"_BLUR"+ext,image_type)

        sys.exit(0)
    
    else :
        print("error")
        sys.exit(1)

if __name__ == "__main__":
    main()
