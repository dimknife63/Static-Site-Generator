import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link

class TestSplitNodesMarkdown(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Here is a [link](https://boot.dev) and another [yt](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("yt", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
