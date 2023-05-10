class Paper:
    def __init__(self, text = ""):
        self._text = text


    def get_text(self):
        return self._text


    def add_text(self, text):
        self._text += text
        return self._text

    def erase_text(self, text):
        pass

