from collections.abc import Iterator


def generate_even_numbers(start: int = 0, end: int = 100) -> Iterator[int]:
    for n in range(start, end):
        if n % 2 == 0:
            return n


def generate_odd_numbers(start: int = 0, end: int = 100) -> list[int]:
    numbers = [n for n in range(start, end)]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            del numbers[i]

    return numbers
