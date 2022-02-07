from PIL import Image

SIZE = 480

def main():
    image = makeflag(SIZE)
    image.save("Belgium.jpeg","JPEG")

def makeflag(heigth):
    width = 3 * heigth//2
    
    offset = width//3
    
    BLACK = (0,0,0)
    YELLOW = (253,218,36)
    RED=(239,51,64)

    image_flag = Image.new("RGB",(width,heigth),YELLOW)

    for i in range(offset):
       for j in range(heigth):
            image_flag.putpixel( (i,j) , BLACK)
            image_flag.putpixel( (i+2*offset,j) , RED)
    
    return image_flag

main()
