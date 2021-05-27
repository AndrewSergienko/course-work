from zope.interface import implementer

from models.IRender import IRender
from models.ATable import ATable


@implementer(IRender)
class TableConsole(ATable):
    def __init__(self, rows, columns, cell_list):
        super(TableConsole, self).__init__(rows, columns, cell_list)

    @staticmethod
    def format_content(content, max_value, width):
        len_spaces = (10*width//70)
        if len(content) < max_value:
            len_diff = (max_value - len(content))*(width//70)
            return " "*(len_spaces//2) + " " * (len_diff // 2) + content + " " * (len_diff - len_diff // 2) + " "*(len_spaces//2) + " "*((width//70)-1)
        else:
            len_diff = (width//70)*len(content)-len(content)
            return " "*(len_spaces//2) + " " * (len_diff // 2) + content + " " * (len_diff - len_diff // 2) + " "*(len_spaces//2) + " "*((width//70)-1)

    def change_render_flag(self, cell, j):
        for row in self._table:
            for i in row:
                if i.id == cell.id:
                    i.content[j][1] = False

    def render(self):
        max_value = self.get_max_value()
        start_line = "+"
        for cell in self._table[0]:
            if type(cell.content) == list:
                start_line += "-" * len(TableConsole.format_content(cell.content[0][0], max_value, cell.size[0])) + "+"
            else:
                start_line += "-" * len(TableConsole.format_content(cell.content, max_value, cell.size[0])) + "+"
        print(start_line)
        for row in self._table:
            content_line = "|"
            end_line = "+"
            for cell in row:
                if cell.size[1] > 40:
                    for i, content in enumerate(cell.content):
                        if content[1]:
                            content_line += TableConsole.format_content(content[0], max_value, cell.size[0]) + "|"
                            self.change_render_flag(cell, i)
                            if i+1 < len(cell.content):
                                end_line += " " * len(TableConsole.format_content(content[0], max_value, cell.size[0])) + "+"
                            else:
                                end_line += "-" * len(TableConsole.format_content(content[0], max_value, cell.size[0])) + "+"
                            break
                else:
                    content_line += TableConsole.format_content(cell.content, max_value, cell.size[0]) + "|"
                    end_line += "-" * len(TableConsole.format_content(cell.content, max_value, cell.size[0])) + "+"
            print(content_line + "\n" + end_line)

