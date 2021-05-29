from models.TableConsole import TableConsole
from models.TableLatex import TableLatex
from models.TableWeb import TableWeb
import sys

from models.IRender import IRender

sys.path.insert(0, 'packages/')

from zope.interface.verify import verifyObject
import eel


@eel.expose
def py_get_list():
    eel.js_returnTable()(create_table)


def create_table(cell_list):
    checked_list = cell_list[-1]
    del cell_list[-1]
    i = 0
    render_list = []
    for i, elem in enumerate(checked_list):
        if elem == 'true':
            render_list.append(create_table_object(i, cell_list))
        i += 1
    render_table(render_list)


def create_table_object(index, cell_list):
    obj = 0
    if index == 0:
        obj = TableConsole(len(cell_list), max(cell_list, key=len), cell_list)
    elif index == 1:
        obj = TableWeb(len(cell_list), max(cell_list, key=len), cell_list)
    elif index == 2:
        obj = TableLatex(len(cell_list), max(cell_list, key=len), cell_list)
    # Перевірка, чи реалізує об`єкт інтерфейс IRender
    if verifyObject(IRender, obj):
        return obj


def render_table(render_list):
    for table in render_list:
        table.render()
