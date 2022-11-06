
import modules 
car = modules.make_car('ford','escort', color='red', year=1986, tow_package=True)

from modules import make_car
car = make_car('ford','escort', color='red', year=1986, tow_package=True)

from modules import make_car as mc
car = mc('ford','escort', color='red', year=1986, tow_package=True)

import modules as md
car = md.make_car('ford','escort', color='red', year=1986, tow_package=True)

from modules import *
car = modules.make_car('ford','escort', color='red', year=1986, tow_package=True)
