from models.IRender import IRender
from models.ATable import ATable
import sys

sys.path.insert(0, 'packages/')

import eel
from zope.interface import implementer


@implementer(IRender)
class TableWeb(ATable):
    def __init__(self, rows, columns, cell_list):
        super(TableWeb, self).__init__(rows, columns, cell_list)

    def render(self):
        eel.show("webout.html")
