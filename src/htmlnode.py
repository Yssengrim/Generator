class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, [], props)  
    
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        else:
            html = f"<{self.tag}"

            if self.props:
                html += self.props_to_html()
            html += f">{self.value}</{self.tag}>"
            
            return html
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")        
        
        if children is None or not isinstance(children, list):
            raise ValueError("ParentNode must have children.")
        
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML.")

        html = f"<{self.tag}"

        if self.props:
            html += self.props_to_html()
        html += ">"
        for child in self.children:
            html += child.to_html()  


        html += f"</{self.tag}>"

        return html
        
             

        
        

               