from abc import ABC

from models.Cell import Cell


class ATable(ABC):
    def __init__(self, rows, columns, cell_list):
        self._rows = rows
        self._columns = columns
        self._table = []
        for row in cell_list:
            self._table.append(list(map(lambda x: Cell(x[0], x[1][0], x[1][1], x[2], x[3]), row)))

    def get_max_value(self):
        max_len = 0
        for row in self._table:
            for cell in row:
                if type(cell.content) == list:
                    cell_len = len(cell.content[0][0])
                else:
                    cell_len = len(cell.content)
                if cell_len > max_len:
                    max_len = cell_len
        return max_len
