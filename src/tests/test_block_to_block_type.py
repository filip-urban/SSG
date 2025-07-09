import unittest
import sys

sys.path.append("src")

from blocktype import block_to_block_type, BlockType


class Testblock_to_block_type(unittest.TestCase):
    def test_block_to_block_type(self):
        heading1 = "# heading"
        heading2 = "## heading"
        code = "```some code```"
        code_multi_line = """```
some code
```"""
        quote = ">some quote"
        u_list = """- first item
- second item
- third item"""
        o_list = """1. first item
2. second item
3. third item"""
        self.assertEqual(block_to_block_type(heading1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(heading2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        self.assertEqual(block_to_block_type(code_multi_line), BlockType.CODE)
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(u_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(o_list), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main
