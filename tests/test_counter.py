import unittest

from bug_hunt import Counter


class CounterTest(unittest.TestCase):

    def test_count_to_three(self) -> None:
        counter = Counter()
        counter.increment()
        counter.increment()
        counter.increment()
        self.assertEqual(3, counter.get_count())

    def test_count_to_three_and_zero(self) -> None:
        counter = Counter()
        counter.increment()
        counter.increment()
        counter.increment()
        counter.decrement()
        counter.decrement()
        counter.decrement()
        self.assertEqual(0, counter.get_count())

    def test_two_counters(self) -> None:
        counter1, counter2 = Counter(), Counter()
        counter1.increment()
        counter2.increment()
        self.assertEqual(1, counter1.get_count())
        self.assertEqual(1, counter2.get_count())


if __name__ == "__main__":
    unittest.main()
