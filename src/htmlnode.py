class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes should implement this method")

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        html_children = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
