#!/user/bin/env python

import random

def asciiart():
    r1 = """
 #######   ######   ######     ###    ########          ########
##     ## ##    ## ##    ##   ## ##   ##     ##         ##
##     ## ##       ##        ##   ##  ##     ##         ##
##     ##  ######  ##       ##     ## ########  ####### ######
##     ##       ## ##       ######### ##   ##           ##
##     ## ##    ## ##    ## ##     ## ##    ##          ##
 #######   ######   ######  ##     ## ##     ##         ##

 """
    r2 = """
..#######...######...######.....###....########..........########
.##.....##.##....##.##....##...##.##...##.....##.........##......
.##.....##.##.......##........##...##..##.....##.........##......
.##.....##..######..##.......##.....##.########..#######.######..
.##.....##.......##.##.......#########.##...##...........##......
.##.....##.##....##.##....##.##.....##.##....##..........##......
..#######...######...######..##.....##.##.....##.........##......
"""
    r3 = """
======================================================================
===    =====      =====     ======  =====       =============        =
==  ==  ===  ====  ===  ===  ====    ====  ====  ============  =======
=  ====  ==  ====  ==  =========  ==  ===  ====  ============  =======
=  ====  ===  =======  ========  ====  ==  ===   ============  =======
=  ====  =====  =====  ========  ====  ==      ====        ==      ===
=  ====  =======  ===  ========        ==  ====  ============  =======
=  ====  ==  ====  ==  ========  ====  ==  ====  ============  =======
==  ==  ===  ====  ===  ===  ==  ====  ==  ====  ============  =======
===    =====      =====     ===  ====  ==  ====  ============  =======
======================================================================
"""

    r4 = """
.------..------..------..------..------..------..------.
|O.--. ||S.--. ||C.--. ||A.--. ||R.--. ||-.--. ||F.--. |
| :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: || ()() |
| '--'O|| '--'S|| '--'C|| '--'A|| '--'R|| '--'-|| '--'F|
`------'`------'`------'`------'`------'`------'`------'
"""
    r5 = """
               .-')                ('-.     _  .-')
              ( OO ).             ( OO ).-.( \( -O )
 .-'),-----. (_)---\_)   .-----.  / . --. / ,------.             ,------.
( OO'  .-.  '/    _ |   '  .--./  | \-.  \  |   /`. '   .-')  ('-| _.---'
/   |  | |  |\  :` `.   |  |('-..-'-'  |  | |  /  | | _(  OO) (OO|(_/
\_) |  |\|  | '..`''.) /_) |OO  )\| |_.'  | |  |_.' |(,------./  |  '--.
  \ |  | |  |.-._)   \ ||  |`-'|  |  .-.  | |  .  '.' '------'\_)|  .--'
   `'  '-'  '\       /(_'  '--'\  |  | |  | |  |\  \            \|  |_)
     `-----'  `-----'    `-----'  `--' `--' `--' '--'            `--'

"""

    r6 = """
 _______  _______  _______  _______  ______           _______
|       ||       ||       ||   _   ||    _ |         |       |
|   _   ||  _____||       ||  |_|  ||   | ||   ____  |    ___|
|  | |  || |_____ |       ||       ||   |_||_ |____| |   |___
|  |_|  ||_____  ||      _||       ||    __  |       |    ___|
|       | _____| ||     |_ |   _   ||   |  | |       |   |
|_______||_______||_______||__| |__||___|  |_|       |___|
"""
    r7 = """
 OOO   SSS   CCC  AA  RRRR      FFFF
O   O S     C    A  A R   R     F
O   O  SSS  C    AAAA RRRR  --- FFF
O   O     S C    A  A R R       F
 OOO  SSSS   CCC A  A R  RR     F

"""

    r8 = """
01001111 01010011 01000011 01000001 01010010 00101101 01000110
"""

    r9 = """

 ###   #### #   #   #   ####        #
#   # #     #   #  # #  #   #      ###
#   # #      #### ##### ####  ### # # #
#   # #         # #   # #          ###
 ###   ####     # #   # #           #   
"""
    pick = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
    print(random.choice(pick))
