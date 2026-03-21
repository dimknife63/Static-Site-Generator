import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Hello World")
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=p, value=Hello World, children=[], props=None)"
        )

    def test_props_to_html_empty(self):
        node = HTMLNode("a", "link")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode("a", "link", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
