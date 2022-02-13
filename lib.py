from PIL import Image

def get_avg(R,G,B)->int:
    avg = round(R * 0.21 + G * 0.71 + B * 0.08)
    return avg

def to_gray(file:str)->Image:

    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_gray = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]
            
            avg = get_avg(R,G,B)      
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

def to_selfia_purple(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_spurple = Image.new("RGB",(width,height))
    
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
            
            spurple_pixel = (R,G,B)

            image_spurple.putpixel((i,j),spurple_pixel)
    
    return image_spurple


def to_purple(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_purple = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]
      
            avg = R * 0.21 + G * 0.71 + B * 0.722 

            pR = round( ( avg*0.3+R*0.7 ) * 0.8)
            pG = round( ( avg*0.3+G*0.7 ) * .54)
            pB = round( ( avg*.3+B*.7 ) * .6)
            
            R = 255 if pR > 255 else pR
            G = 255 if pG> 255 else pG
            B = 255 if pB > 255 else pB
            
            g_pxl = (R,G,B)

            image_purple.putpixel((i,j),g_pxl)
    
    return image_purple


def to_green(file:str)->Image:
    image = Image.open(file)
    
    height = image.height
    width = image.width
    
    image_green = Image.new("RGB",(width,height))
    
    for i in range(width):
        for j in range(height):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]

                
            avg = R*0.21 + G*0.71 + B*0.722
            
            gR = round(0.5*(  avg*0.3+R*0.7 ))
            gG = round(0.71*(  avg*0.3+G*0.7 ))
            gB = round(0.51*( avg*0.3+B*0.7 ))
            
            R = 255 if gR > 255 else gR
            G = 255 if gG> 255 else gG
            B = 255 if gB > 255 else gB
            
            g_pxl = (R,G,B)

            image_green.putpixel((i,j),g_pxl)
    
    return image_green



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

def to_lut_hexa(file:str,Ruser,Guser,Buser)->Image:

    image = Image.open(file)

    h,w = image.height,image.width

    image_lut = Image.new("RGB",(w,h))

    for i in range(w):
        for j in range(h):
            
            pxl = image.getpixel((i,j))
            R,G,B = pxl[0],pxl[1],pxl[2]
            avg = get_avg(R,G,B)

            lR = round(( 0.7 * R + 0.3 * avg ) * (Ruser/255) )
            lG = round(( 0.7 * G + 0.3 * avg ) * (Guser/255) )
            lB = round(( 0.7 * B + 0.3 * avg ) * (Buser/255) )
            

            R = 255 if lR > 255 else lR
            G = 255 if lG> 255 else lG
            B = 255 if lB > 255 else lB
            
            lut_pixel = (R,G,B)

            image_lut.putpixel((i,j),lut_pixel)


    return image_lut
