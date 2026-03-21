import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_type(self):
        node1 = TextNode("Same text", TextType.TEXT)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_property(self):
        node1 = TextNode("link text", TextType.LINK, "https://example.com")
        node2 = TextNode("link text", TextType.LINK, "https://example.com")
        node3 = TextNode("link text", TextType.LINK, None)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

if __name__ == "__main__":
    unittest.main()
