import sys
import defs

sys.path.insert(0, 'packages/')

import eel

if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(500, 360))
