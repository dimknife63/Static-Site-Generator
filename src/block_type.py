from enum import Enum
import re

class BlockType(Enum):
PARAGRAPH = "paragraph"
HEADING = "heading"
CODE = "code"
QUOTE = "quote"
UNORDERED_LIST = "unordered_list"
ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
lines = block.split("
")
if re.match(r"^#{1,6} ", lines[0]):
return BlockType.HEADING
if block.startswith("") and block.endswith(""):
return BlockType.CODE
if all(line.startswith(">") for line in lines):
return BlockType.QUOTE
if all(re.match(r"^\d+. ", line) for line in lines):
numbers = [int(re.match(r"^(\d+). ", line).group(1)) for line in lines]
if numbers == list(range(1, len(lines)+1)):
return BlockType.ORDERED_LIST
if all(line.startswith("- ") for line in lines):
return BlockType.UNORDERED_LIST
return BlockType.PARAGRAPH
