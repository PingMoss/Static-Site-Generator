class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def create_head(self):
        return f"<{self.tag}{self.props_to_html()}>"

    def create_tail(self):
        return f"</{self.tag}>"

    def props_to_html(self):
        props = ""
        if self.props is not None:
            for key, value in self.props.items():
                props += f' {key}="{value}"'
        return props

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Missing value")
        if self.tag is None:
            return self.value
        return f"{self.create_head()}{self.value}{self.create_tail()}"

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Props: {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children")
        child_nodes = "".join((map(lambda child: child.to_html(), self.children)))
        return f"{self.create_head()}{child_nodes}{self.create_tail()}"
