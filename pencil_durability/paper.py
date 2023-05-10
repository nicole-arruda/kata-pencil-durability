class Paper:
    def __init__(self):
        self._contents = ""


    def contents(self):
        return self._contents


    def write(self, new_text):
        self._contents += new_text

    def erase(self, text_to_erase):
        self._contents = ""
