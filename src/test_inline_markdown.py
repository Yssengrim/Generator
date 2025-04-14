import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


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
                TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
            ],
        new_nodes,
    )

    def test_split_links_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_no_links(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_at_beginning(self):
        node = TextNode("[Link](https://example.com) followed by text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Link", TextType.LINK, "https://example.com"),
            TextNode(" followed by text", TextType.TEXT)
            ], new_nodes)

    def test_split_links_at_end(self):
        node = TextNode("Text followed by [link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Text followed by ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
            ], new_nodes)
        
    def test_text_to_textnodes(self):
        text = "This is plain text"
        expected = [TextNode("This is plain text", TextType.TEXT)]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"

        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"

        text = "This is *italic* text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"

        text = "This is `code` text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"

        text = "This is __bold__ text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"
        
        text = "This is _italic_ text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),   
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"

        text = "This is an ![image](https://imgur.com/zjjcJKZ.png) in text"
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://imgur.com/zjjcJKZ.png"),
            TextNode(" in text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"
        
        text = "This is a [link](https://boot.dev) in text"
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" in text", TextType.TEXT),
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, but got {actual}"



if __name__ == "__main__":
    unittest.main()