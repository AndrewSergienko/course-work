from zope.interface import implementer

from models.IRender import IRender
from models.ATable import ATable


@implementer(IRender)
class TableLatex(ATable):
    def __init__(self, rows=None, columns=None, cell_list=None):
        super(TableLatex, self).__init__(rows, columns, cell_list)

    def render(self):
        pass
