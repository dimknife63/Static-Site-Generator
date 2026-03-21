from htmlnode import HTMLNode
from textnode_to_htmlnode import text_to_children, text_node_to_html_node
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


def markdown_to_html_node(markdown: str) -> HTMLNode:
    parent = HTMLNode("div")
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.HEADING:
            level = len(block.split(" ")[0])  # number of # characters
            content = block[level + 1:]       # skip "# "
            children = text_to_children(content)
            node = HTMLNode(f"h{level}", children=children)

        elif btype == BlockType.PARAGRAPH:
            children = text_to_children(block.replace("\n", " "))
            node = HTMLNode("p", children=children)

        elif btype == BlockType.CODE:
            code_text = block.strip("`")  # remove ``` around code
            text_node = HTMLNode("code", text=code_text)
            node = HTMLNode("pre", children=[text_node])

        elif btype == BlockType.QUOTE:
            lines = "\n".join(line.lstrip("> ") for line in block.split("\n"))
            children = text_to_children(lines)
            node = HTMLNode("blockquote", children=children)

        elif btype == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                line_text = line[2:]  # remove "- "
                children = text_to_children(line_text)
                items.append(HTMLNode("li", children=children))
            node = HTMLNode("ul", children=items)

        elif btype == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                dot_pos = line.find(". ")
                line_text = line[dot_pos + 2:]  # skip "1. "
                children = text_to_children(line_text)
                items.append(HTMLNode("li", children=children))
            node = HTMLNode("ol", children=items)

        else:
            continue

        parent.children.append(node)

    return parent