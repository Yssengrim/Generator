from htmlnode import LeafNode
from enum import Enum
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images

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

def split_nodes_image(old_nodes):
    result = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
            
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue
        
        remaining_text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            before, *after = remaining_text.split(image_markdown, 1)
            
            if before:
                result.append(TextNode(before, TextType.TEXT))
                
            result.append(TextNode(alt_text, TextType.IMAGE, url))
            
            remaining_text = after[0] if after else ""
        
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result

def split_nodes_link(old_nodes):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        
        remaining_text = node.text
        for text, url in links:
            link_markdown = f"[{text}]({url})"
            before, *after = remaining_text.split(link_markdown, 1)
            if before:
                result.append(TextNode(before, TextType.TEXT))
            result.append(TextNode(text, TextType.LINK, url))
            remaining_text = after[0] if after else ""
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result

            
def text_to_textnodes(text):
    if not text:
        return []
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
        
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "__", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes 

