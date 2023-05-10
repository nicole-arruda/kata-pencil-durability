from pencil_durability.paper import Paper


def test_new_paper_is_blank():
    paper = Paper()
    assert paper.contents() == ""

def test_write_hello_makes_paper_contents_hello():
    paper = Paper()
    paper.write("Hello")
    assert paper.contents() == "Hello"

def test_write_hello_then_how_are_you():
    paper = Paper()
    paper.write("Hello")
    paper.write(" how are you")
    assert paper.contents() == "Hello how are you"

def test_write_new_line():
    paper = Paper()
    paper.write("Hello")
    paper.write("\n")
    paper.write("how are you")
    assert paper.contents() == "Hello\nhow are you"

def test_erase_hello_from_hello():
    paper = Paper()
    paper.write("Hello")
    paper.erase("Hello")
    assert paper.contents() == ""
