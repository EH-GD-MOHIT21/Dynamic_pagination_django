# ("name","path")
from random import choice

filenames = [
        "img/board.png",
        "imgs/Screenshot_6.png",
        "imgs/ludo_board.png",
        "imgs/chayan.jpg",
        "imgs/chayan1.jpg",
        "imgs/instagram-share-links-on-8-ways-600_DD6EDFw.png",
    ]

someGivenRange = int(input())

with open('database.txt','w') as file:
    charARR = [chr(i) for i in range(65,91)]
    charARR1 =  [ chr(i) for i in range(97,122)]
    while someGivenRange:
        name = ""
        for i in range(6):
            name += choice(charARR)
            if i == 3:
                name += " "
            name += choice(charARR1)
        _file = choice(filenames)
        file.write(f'("{name}" , "{_file}"),')
        file.write("\n")
        someGivenRange -=1
    file.close()

