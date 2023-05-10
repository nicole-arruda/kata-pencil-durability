from pencil_durability.paper import Paper

if __name__ == "__main__":
    paper = Paper()

    paper.add_text("ABC")
    print(f"1: {paper.get_text()}")

    paper.add_text(" a b c ")
    print(f"2: {paper.get_text()}")

    paper.add_text("a1Ab2Bc3C")
    print(f"3: {paper.get_text()}")

    paper.erase_text("c")
    print(f"4: {paper.get_text()}")

    paper.erase_text("c")
    print(f"5: {paper.get_text()}")

    paper.erase_text("")