import unittest
from lab5 import analyze_bracket_positions, validate_text_brackets


class TestBracketValidator(unittest.TestCase):

    def test_valid_brackets(self):
        self.assertTrue(validate_text_brackets("()"))
        self.assertTrue(validate_text_brackets("<div><p>{ test }</p></div>"))
        self.assertTrue(validate_text_brackets("text without brackets"))

    def test_invalid_brackets_raises_error(self):
        with self.assertRaises(ValueError):
            validate_text_brackets("<div><p>{ test }}</p</div>")

    def test_invalid_indices(self):
        is_valid, indices = analyze_bracket_positions("({[}")
        self.assertFalse(is_valid)
        self.assertTrue(len(indices) > 0)


if __name__ == "__main__":
    unittest.main()