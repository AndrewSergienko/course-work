from zope.interface import implementer
import defs
import eel

from models.IRender import IRender
from models.ATable import ATable


@implementer(IRender)
class TableWeb(ATable):
    def __init__(self, rows, columns, cell_list):
        super(TableWeb, self).__init__(rows, columns, cell_list)

    def render(self):
        eel.js_tableOut()