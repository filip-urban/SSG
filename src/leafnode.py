from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, html_props):
        super().__init__(tag, value, props=html_props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
