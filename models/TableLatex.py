from models.IRender import IRender
from models.ATable import ATable
import sys

sys.path.insert(0, 'packages/')

from zope.interface import implementer


@implementer(IRender)
class TableLatex(ATable):
    def __init__(self, rows=None, columns=None, cell_list=None):
        super(TableLatex, self).__init__(rows, columns, cell_list)

    def render(self):
        pass
