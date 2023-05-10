from pencil_durability.paper import Paper


def test_new_paper_is_blank():
    paper = Paper()
    assert paper.get_text() == ""


def test_add_hello_to_blank_paper_returns_hello():
    # Arrange
    paper = Paper()

    # Act
    text_after_add = paper.add_text("hello")

    # Assert
    assert text_after_add == "hello"


def test_add_world_to_paper_with_hello_returns_hello_world():
    # Arrange
    paper = Paper("hello")

    # Act
    text_after_add = paper.add_text(", world")

    # Assert
    assert text_after_add == "hello, world"