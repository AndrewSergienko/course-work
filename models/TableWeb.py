from zope.interface import implementer
import defs
import eel

from models.IRender import IRender
from models.ATable import ATable


@implementer(IRender)
class TableWeb(ATable):
    def __init__(self, rows=None, columns=None, cell_list=None):
        super(TableWeb, self).__init__(rows, columns, cell_list)

    def render(self):
        html_text = defs.get_html()