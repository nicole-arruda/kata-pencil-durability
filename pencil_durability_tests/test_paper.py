from pencil_durability.paper import Paper


def test_new_paper_is_blank():
    paper = Paper()
    assert paper.contents() == ""
