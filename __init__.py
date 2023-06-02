from blockmap._types import T_OCCUPANT as T
from typing import Generic

__all__ = ['Blockmap']


class Blockmap(Generic[T]):
    def __init__(self, block_size: int = 1) -> None:
        self.block_size: int = block_size
        self.map: dict[tuple[int, int], list[T]] = {}

    def register_occupant(self, x: float, y: float, width: float,
                          height: float, occupant: T) -> None:
        min_x = int((int(x - width)) / self.block_size)
        min_y = int((int(y - height)) / self.block_size)
        max_x = int((int(x + width)) / self.block_size) + 1
        max_y = int((int(y + height)) / self.block_size) + 1

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                k = (x, y)

                if k not in self.map:
                    self.map[k] = []

                if occupant not in self.map[k]:
                    self.map[k].append(occupant)

    def query(self, left: float, top: float, right: float,
              bottom: float) -> list[T]:
        result = []

        min_x = int((int(left)) / self.block_size)
        min_y = int((int(top)) / self.block_size)
        max_x = int((int(right)) / self.block_size) + 1
        max_y = int((int(bottom)) / self.block_size) + 1

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                k = (x, y)
                if k in self.map:
                    result += self.map[k]

        return result
