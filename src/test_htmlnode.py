import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_one_prop(self):
        # Test with a single property
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_with_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        # Note: Since dictionaries don't guarantee order, you might need to check for both possibilities
        possible_outputs = [
            ' href="https://google.com" target="_blank"',
            ' target="_blank" href="https://google.com"'
        ]
        self.assertIn(node.props_to_html(), possible_outputs)

    def test_props_to_html_with_no_props(self):
        # Test with no properties
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    
class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child") 
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        print
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    
    def test_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")

    def test_missing_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None)
        self.assertEqual(str(context.exception), "ParentNode must have children.")

if __name__ == "__main__":
    
    unittest.main()