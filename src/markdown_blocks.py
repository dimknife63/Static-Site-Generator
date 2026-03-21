from enum import Enum
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    return [b.strip() for b in blocks if b.strip()]

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    if lines[0].startswith("#"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line[0].isdigit() and line[1:3] == ". " for line in lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text: str):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]

def markdown_to_html_node(markdown: str) -> ParentNode:
    children_nodes = []

    for block in markdown_to_blocks(markdown):
        btype = block_to_block_type(block)

        if btype == BlockType.HEADING:
            level = len(block.split(" ")[0])
            content = block[level+1:]
            children = text_to_children(content)
            node = ParentNode(f"h{level}", children)

        elif btype == BlockType.PARAGRAPH:
            children = text_to_children(block.replace("\n", " "))
            node = ParentNode("p", children)

        elif btype == BlockType.CODE:
            code_text = block.strip("`")
            code_node = LeafNode("code", code_text)
            node = ParentNode("pre", [code_node])

        elif btype == BlockType.QUOTE:
            lines = "\n".join(line.lstrip("> ") for line in block.split("\n"))
            children = text_to_children(lines)
            node = ParentNode("blockquote", children)

        elif btype == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                line_text = line[2:]
                children = text_to_children(line_text)
                items.append(ParentNode("li", children))
            node = ParentNode("ul", items)

        elif btype == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                dot_pos = line.find(". ")
                line_text = line[dot_pos+2:]
                children = text_to_children(line_text)
                items.append(ParentNode("li", children))
            node = ParentNode("ol", items)

        else:
            continue

        children_nodes.append(node)

    return ParentNode("div", children_nodes)

def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 title found")