import unittest
from textnode import TextNode, TextType
from text_processing import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        # Test when there's no delimiter in the text
        node = TextNode("This is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a text node")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_with_delimiter(self):
        # Test with a delimiter present
        node = TextNode("This is a `code block` in text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " in text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_multiple_delimiter_pairs(self):
        node = TextNode("Text with `one` and `two` code blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "Text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "one")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "two")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text, " code blocks")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_non_text_nodes(self):
        bold_node = TextNode("Bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([bold_node], "`", TextType.CODE)
    
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Bold text")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)

    def test_different_delimiters(self):
        node = TextNode("Text with **bold** content", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual

    

if __name__ == "__main__":
    unittest.main()