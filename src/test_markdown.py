import unittest
import re
from extract_markdown import extract_markdown_images, extract_markdown_links



class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_no_images(self):
        text = "This text has no images only [a link](https://www.boot.dev)"
        self.assertListEqual([], extract_markdown_images(text))

    
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_no_links(self):
        text = "This text has no links only ![an image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertListEqual([], extract_markdown_links(text))
    
    

if __name__ == "__main__":
    unittest.main()