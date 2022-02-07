import os
import sys


def get_filename_and_ext(filename:str)->str:

    path = os.path.dirname(filename)
    base = os.path.basename(filename)
    filename_without_ext,ext = os.path.splitext(base)

    return filename_without_ext,ext,path


def treat_filtername(filter_:str)->str:
    filter_treat = ""
    length_str_filter = len(filter_)

    atoz = range( ord("a"), ord("z") )
    for i in range(length_str_filter):
        if ord(filter_[i]) in atoz:
            filter_treat += filter_[i].upper()
        else :
            continue
    
    return filter_treat

def helpmsg(returnvalue:int):
    print("""Usage:python main.py FILTER ARQUIVE [path]
    Filters: 
        - Gray scale : -gray or --gray or gray
        - Blur : -blur or --blur or blur
        - Purple : -purple or --purple or purple
        - Selfia : -selfia or --selfia or selfia
        - Negative : -neg or --neg or negative
    
    example: python main.py --neg image.jpeg ./

    usage ./ for save the image in current directory""")
    sys.exit(returnvalue)
    


