import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        check = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=props)
        self.assertEqual(check, node.props_to_html())

    def test_props_to_html_none(self):
        # props is none by default
        node = HTMLNode()
        self.assertEqual(None, node.props_to_html())

    def test_repr_all(self):
        node = HTMLNode(
            "a",
            "This is content (tm)",
            ["child 1, child 2"],
            {"href": "https://www.google.com"},
        )
        check = "Tag: a, Value: This is content (tm), Children: ['child 1, child 2'], Props: {'href': 'https://www.google.com'}"
        self.assertEqual(check, repr(node))

    def test_repr_some(self):
        node = HTMLNode(value="This is a value")
        check = "Tag: None, Value: This is a value, Children: None, Props: None"
        self.assertEqual(check, repr(node))


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_tagless(self):
        node = LeafNode(tag=None, value="This is bold text.")
        self.assertEqual(node.to_html(), "This is bold text.")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "google.com", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a>google.com</a>")

    def test_leaf_to_html_valueless(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr_all(self):
        node = LeafNode(
            "a",
            "This is content (tm)",
            {"href": "https://www.google.com"},
        )
        check = "Tag: a, Value: This is content (tm), Props: {'href': 'https://www.google.com'}"
        self.assertEqual(check, repr(node))

    def test_repr_some(self):
        node = LeafNode("p", "This is a value")
        check = "Tag: p, Value: This is a value, Props: None"
        self.assertEqual(check, repr(node))


if __name__ == "__main__":
    unittest.main()
