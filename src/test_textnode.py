import unittest
from textnode import TextType, TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.CODE, "www.example.com")
        node2 = TextNode("This is a text node", TextType.CODE, "www.example.com")
        self.assertEqual(node, node2)

    def test_not_eq_1(self):
        node = TextNode("This says one thing", TextType.TEXT, "www.example.com")
        node2 = TextNode("This says something else", TextType.TEXT, "www.example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is a text node", TextType.IMAGE, "www.example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        node = TextNode("This is a text node", TextType.IMAGE, "www.first.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "www.second.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_4(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, "not a node")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italicized text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italicized text")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props_to_html(), ' href="https://www.example.com"')

    def test_image(self):
        node = TextNode(
            "This is an image", TextType.IMAGE, "https://www.example.com/image"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props_to_html(),
            ' src="https://www.example.com/image" alt="This is an image"',
        )

    def test_invalid_text_type(self):
        node = TextNode("This node has an invalid text type", "Invalid type")
        with self.assertRaisesRegex(Exception, "Invalid text type"):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
