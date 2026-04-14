import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
        # props is "" by default
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

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
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">google.com</a>'
        )

    def test_leaf_to_html_valueless(self):
        node = LeafNode("a", None)
        with self.assertRaisesRegex(ValueError, "Missing value"):
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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        """
        parent - child_a - grandchild_a - great_grandchld_a
                                        - great_grandchld_a_2
               - child_b - grandchild_b
               - child_c
        """
        great_grandchld_a = LeafNode("agg", "grandchild A", {"href": "www.example.com"})
        great_grandchld_a_2 = LeafNode("agg2", "grandchild A 2")
        grandchild_a = ParentNode("ag", [great_grandchld_a, great_grandchld_a_2])
        child_a = ParentNode("ac", [grandchild_a])

        grandchild_b = LeafNode("bg", "grandchild B")
        child_b = ParentNode("bc", [grandchild_b], {"href": "www.example.com"})

        child_c = LeafNode("c", "child C")

        parent = ParentNode("p", [child_a, child_b, child_c])

        check = '<p><ac><ag><agg href="www.example.com">grandchild A</agg><agg2>grandchild A 2</agg2></ag></ac><bc href="www.example.com"><bg>grandchild B</bg></bc><c>child C</c></p>'

        self.assertEqual(parent.to_html(), check)

    def test_to_html_tag_ValueError(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaisesRegex(ValueError, "Missing tag"):
            node.to_html()

    def test_to_html_children_ValueError(self):
        node = ParentNode("div", None)
        with self.assertRaisesRegex(ValueError, "Missing children"):
            node.to_html()

    def test_to_html_child_ValueError(self):
        node = ParentNode("div", [LeafNode("p", "text"), LeafNode("p", None)])
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
