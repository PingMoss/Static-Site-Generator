from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        check_text = self.text == other.text
        check_text_type = self.text_type == other.text_type
        check_url = self.url == other.url

        return check_text and check_text_type and check_url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if isinstance(text_node.text_type, TextType):
        txt_type = text_node.text_type
    else:
        txt_type = "invalid"
    txt = text_node.text
    url = text_node.url

    if txt_type == TextType.TEXT:
        node = LeafNode(None, txt)
    elif txt_type == TextType.BOLD:
        node = LeafNode("b", txt)
    elif txt_type == TextType.ITALIC:
        node = LeafNode("i", txt)
    elif txt_type == TextType.CODE:
        node = LeafNode("code", txt)
    elif txt_type == TextType.LINK:
        node = LeafNode("a", txt, {"href": url})
    elif txt_type == TextType.IMAGE:
        node = LeafNode("img", "", {"src": url, "alt": txt})
    else:
        raise Exception("Invalid text type")
    return node
