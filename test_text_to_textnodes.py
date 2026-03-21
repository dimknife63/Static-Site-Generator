import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_plain(self):
        nodes = text_to_textnodes("hello")
        self.assertEqual(nodes, [TextNode("hello", TextType.TEXT)])

    def test_bold(self):
        nodes = text_to_textnodes("**hi**")
        self.assertEqual(nodes, [TextNode("hi", TextType.BOLD)])

    def test_italic(self):
        nodes = text_to_textnodes("_hi_")
        self.assertEqual(nodes, [TextNode("hi", TextType.ITALIC)])

    def test_code(self):
        nodes = text_to_textnodes("`hi`")
        self.assertEqual(nodes, [TextNode("hi", TextType.CODE)])

    def test_image(self):
        nodes = text_to_textnodes("![alt](url)")
        self.assertEqual(nodes, [TextNode("alt", TextType.IMAGE, "url")])

    def test_link(self):
        nodes = text_to_textnodes("[a](b)")
        self.assertEqual(nodes, [TextNode("a", TextType.LINK, "b")])

    def test_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("text", TextType.BOLD))
        self.assertEqual(nodes[3], TextNode("italic", TextType.ITALIC))
        self.assertEqual(nodes[5], TextNode("code block", TextType.CODE))
        self.assertEqual(nodes[7], TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"))
        self.assertEqual(nodes[9], TextNode("link", TextType.LINK, "https://boot.dev"))

if __name__ == "__main__":
    unittest.main()

