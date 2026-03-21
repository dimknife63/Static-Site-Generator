import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " text")

    def test_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

    def test_unmatched(self):
        node = TextNode("This is `bad text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
