import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        # Your test code here
        node1 = TextNode("First text", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_different_type(self):
        # Your test code here
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_with_url(self):
        # Your test code here
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)
        
        node3 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node3)
        
        node4 = TextNode("Link text", TextType.LINK) 
        self.assertNotEqual(node1, node4)


if __name__ == "__main__":
    unittest
