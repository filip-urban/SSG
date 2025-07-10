from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def is_ordered_list(text):
    position = 1
    for line in text.split("\n"):
        if not line[:3] == f"{position}. ":
            return False
        position += 1
    return True


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(block) > 6 and block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if len(block.split("\n")) == len(
        list(filter(lambda x: x[0] == ">" if x else True, block.split("\n")))
    ):
        return BlockType.QUOTE
    if len(block.split("\n")) == len(
        list(filter(lambda x: x[:2] == "- " if x else True, block.split("\n")))
    ):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(text):
    return [block.strip() for block in text.split("\n\n") if block]
