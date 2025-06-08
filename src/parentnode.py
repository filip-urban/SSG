from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: missing tag")
        if not self.children:
            raise ValueError("invalid HTML: missing children")
        result = ""
        for node in self.children:
            result += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
