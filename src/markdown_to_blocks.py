def markdown_to_blocks(text):
    return [block.strip() for block in text.split("\n\n") if block]
