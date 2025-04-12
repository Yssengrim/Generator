from textnode import TextNode, TextType

def main():
    # Create a sample TextNode
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the TextNode
    print(node)

if __name__ == "__main__":
    main()
