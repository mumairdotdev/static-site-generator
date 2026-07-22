class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list[HTMLNode] | None = None, 
            props: dict[str, str] | None = None
        ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        html_attribute: str = ""
        for attribute in self.props:
            html_attribute += f' {attribute}="{self.props[attribute]}"'
        return html_attribute

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str | None, 
            value: str, 
            props: dict[str, str] | None = None
        ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Invalid HTML: should have value")
        if not self.tag:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"