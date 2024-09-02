import unittest
from collections.abc import Iterator

from bug_hunt import generator


class GeneratorTest(unittest.TestCase):

    def test_generate_even_numbers_to_ten(self) -> None:
        generated: Iterator[int] = generator.generate_even_numbers(0, 10)
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(list(generated), expected)

    def test_generate_odd_numbers_to_ten(self) -> None:
        generated: list[int] = generator.generate_odd_numbers(0, 10)
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(generated, expected)


if __name__ == "__main__":
    unittest.main()
