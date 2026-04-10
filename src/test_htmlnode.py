import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
