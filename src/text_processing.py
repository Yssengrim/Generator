from htmlnode import LeafNode
from enum import Enum
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        if text.count(delimiter) == 0:
            new_nodes.append(old_node)
            continue

        split_text = text.split(delimiter)

        if split_text[0]:
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
        
        for i in range(1, len(split_text)):
            if i % 2 == 1 and i < len(split_text) - 1:
                new_nodes.append(TextNode(split_text[i], text_type))
            elif i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            elif i % 2 == 1 and i == len(split_text) - 1:
                raise ValueError(f"Unclosed delimiter: {delimiter}")
            
    return new_nodes
            



                