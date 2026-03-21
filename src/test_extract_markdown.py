import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertListEqual(extract_markdown_images(text), [("image", "https://i.imgur.com/zjjcJKZ.png")])

    def test_extract_multiple_images(self):
        text = "![img1](url1) and ![img2](url2)"
        self.assertListEqual(extract_markdown_images(text), [("img1", "url1"), ("img2", "url2")])

    def test_extract_markdown_links(self):
        text = "A link [to boot dev](https://www.boot.dev) and [to yt](https://youtube.com)"
        self.assertListEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to yt", "https://youtube.com")]
        )

    def test_links_do_not_match_images(self):
        text = "![img](img_url) and [link](link_url)"
        self.assertListEqual(extract_markdown_links(text), [("link", "link_url")])
        self.assertListEqual(extract_markdown_images(text), [("img", "img_url")])

if __name__ == "__main__":
    unittest.main()
