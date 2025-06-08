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
