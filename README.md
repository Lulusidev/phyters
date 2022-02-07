# Phyters

## A program which aply filters in images scripted in python

## Available Filters:

- Src image

![src](testimages/srcimage/neymarnevou.jpg)

- Grey Scale 

![src](testimages/outimage/neymarnevou_GRAY.jpg)

- Selfia Filter 

![src](testimages/outimage/neymarnevou_SELFIA.jpg)

- Blur Filter 

![src](testimages/outimage/neymarnevou_BLUR.jpg)

- Purple Filter

![src](testimages/outimage/neymarnevou_PURPLE.jpg)

- Negative Filter

![src](testimages/outimage/neymarnevou_NEG.jpg)

## How Install

Install using git clone

```sh
        git clone https://github.com/lulusidev/phyters/
```

Is only this,lol

## How Usage

- Pass for main.py the filter ,the path image and the output path for filtered-image

```sh
        Usage:python main.py --filter image path/
```

- or pass chmod for main.py ,the exec wihtout the python "prefix"

```sh
        chmod +x ./main.py
        Usage:./main.py --filter image path/
```

- Filters Flags:
    - Grey scale : -gray or --gray or gray
    - Blur : -blur or --blur or blur
    - Purple : -purple or --purple or purple
    - Selfia : -selfia or --selfia or selfia
    - Negative : -neg or --neg or negative


- example: python main.py --neg image.jpeg ./

- obs: Usage ./ with path for save the image in currrent directory
