class Counter:
    count: int = 0

    def increment(self) -> None:
        Counter.count += 1

    def decrement(self) -> None:
        Counter.count -= 1

    def get_count(self) -> int:
        return self.count
