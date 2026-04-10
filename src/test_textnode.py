import unittest
from textnode import TextType, TextNode


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


if __name__ == "__main__":
    unittest.main()
