class Paper:
    def __init__(self):
        self._contents = ""


    def contents(self):
        return self._contents


    def write(self, new_text):
        self._contents += new_text

    def erase(self, text_to_erase):
        found_index = self._contents.rfind(text_to_erase)
        print(f"FOUND AT INDEX: {found_index}")

        first_part = self._contents[0:found_index]
        second_part = self._contents[found_index:len(self._contents)]
        new_second_part = second_part.replace(text_to_erase, "     ")

        self._contents = first_part + new_second_part
