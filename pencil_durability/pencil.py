from pencil_durability.paper import Paper


class Pencil:
    def __init__(self, durability):
        self._durability = durability

    def durability(self):
        return self._durability

    def write(self, text, paper: Paper):
        paper.write(text)
        self._durability -= len(text)
