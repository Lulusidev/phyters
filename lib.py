from PIL import Image

def to_gray(file:str)->Image:

    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_gray = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]
            
            avg = (pxl[0]+pxl[1]+pxl[2])//3      
            gray_pixel = (avg,avg,avg)
            
            image_gray.putpixel((i,j),gray_pixel)
    
    return image_gray

def to_selfia(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_selfia = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]

            sR = round(0.393*R + 0.769*G + 0.189*B)
            sG = round(0.349*R + 0.686*G + 0.168*B)
            sB = round(0.272*R + 0.534*G + 0.131*B)
            
            R = 255 if sR > 255 else sR
            G = 255 if sG> 255 else sG
            B = 255 if sB > 255 else sB
            
            selfia_pixel = (R,G,B)

            image_selfia.putpixel((i,j),selfia_pixel)
    
    return image_selfia

def to_purple(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_purple = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]

            sR = round(0.393*R + 0.769*G + 0.189*B)
            sB = round(0.349*R + 0.686*G + 0.168*B)
            sG = round(0.272*R + 0.534*G + 0.131*B)
            
            R = 255 if sR > 255 else sR
            G = 255 if sG> 255 else sG
            B = 255 if sB > 255 else sB
            
            purple_pixel = (R,G,B)

            image_purple.putpixel((i,j),purple_pixel)
    
    return image_purple



def to_negative(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_neg = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]

            nR = 255 - R
            nG = 255 - G 
            nB = 255 - B
            
            neg_pixel = (nR,nG,nB)

            image_neg.putpixel((i,j),neg_pixel)
    
    return image_neg

def to_blur(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_blur = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]
            
            bR,bG,bB,count = 0,0,0,0
            for k in (-1,1):
                for l in range(-1,1):
                    if (i+k >= width or i+k < 0 or j+l >= height or j+l < 0):
                        continue 
                    
                    bR += image.getpixel((k+i,l+j))[0]
                    bG += image.getpixel((k+i,l+j))[1]  
                    bB += image.getpixel((k+i,l+j))[2]
                    count +=1

            R = bR//count
            G = bG//count
            B = bB//count

            blur_pixel = (R,G,B)

            image_blur.putpixel((i,j),blur_pixel)
    

    return image_blur

