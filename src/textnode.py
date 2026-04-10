from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        check_text = self.text == other.text
        check_text_type = self.text_type.value == other.text_type.value
        check_url = self.url == other.url

        return check_text and check_text_type and check_url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
