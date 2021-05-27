from models.TableConsole import TableConsole
from models.TableLatex import TableLatex
from models.TableWeb import TableWeb

import eel


@eel.expose
def py_get_list():
    eel.js_returnTable()(create_table)


def create_table(cell_list):
    render_list = cell_list[-1]
    del cell_list[-1]
    i = 0
    while i < len(render_list):
        if render_list[i] == 'true':
            render_list[i] = create_table_object(i, cell_list)
            i += 1
        else:
            del render_list[i]
    render_table(render_list)


def create_table_object(index, cell_list):
    if index == 0:
        return TableConsole(len(cell_list), max(cell_list, key=len), cell_list)
    elif index == 1:
        return TableWeb(len(cell_list), max(cell_list, key=len), cell_list)
    elif index == 2:
        return TableLatex(len(cell_list), max(cell_list, key=len), cell_list)


def render_table(render_list):
    for table in render_list:
        table.render()
