class Cell:
    def __init__(self, cell_id, width, height, align, content):
        self._id = cell_id
        self._width = int(width[:-2])
        self._height = int(height[:-2])
        if self._height > 40:
            self._content = [["", True] for _ in range(self._height//40)]
            if len(content) > 5:
                isl = 5*(self._width//70)
                for i, sublist in enumerate(self._content):
                    cell_content = "".join(content[i*isl: i*isl+isl])
                    sublist[0] = cell_content
                    if len(content[i*isl+isl:]) <= 5 and i+1 < len(self._content):
                        self._content[i+1][0] = content[i*isl+isl:]
                        break
                    elif i > len(self._content):
                        sublist[0] += content[i*isl+isl:]
                        break
            else:
                self._content[0][0] = content
        else:
            self._content = content
        self._align = align

    @property
    def id(self):
        return self._id

    @property
    def size(self):
        return [self._width, self._height]

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, i, j, value):
        self._content[i][j] = value

