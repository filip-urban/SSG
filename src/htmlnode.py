class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html isn't implemented")

    def props_to_html(self):
        return (
            " " + " ".join([f'{key}="{self.props[key]}"' for key in self.props])
            if self.props
            else ""
        )


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: missing tag")
        if not self.children:
            raise ValueError("invalid HTML: missing children")
        result = ""
        for node in self.children:
            result += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, html_props=None):
        super().__init__(tag, value, props=html_props)

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: missing value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
