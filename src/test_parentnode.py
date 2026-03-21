import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_nested_parent_nodes(self):
        leaf1 = LeafNode("i", "italic")
        leaf2 = LeafNode(None, "plain")
        parent1 = ParentNode("p", [leaf1, leaf2])
        parent2 = ParentNode("div", [parent1])
        self.assertEqual(parent2.to_html(), "<div><p><i>italic</i>plain</p></div>")

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

if __name__ == "__main__":
    unittest.main()
