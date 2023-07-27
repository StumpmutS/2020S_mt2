"""Q1: Height of a binary tree
What is the smallest number of branches we
must pass through to reach fruit?
"""

class BinaryFruitTree:
    """Abstract base class"""
    def min_height(self, counter: int = 0) -> int:
        """The smallest number of branches we
        must pass through to reach fruit
        """
        raise NotImplementedError("min_height must be defined")

class Fruit(BinaryFruitTree):
    """Leaf nodes bear fruit"""
    def __init__(self, fruit: str):
        self._fruit = fruit

    def min_height(self, counter=0) -> int:
        """Here it is!"""
        return counter

    def __repr__(self) -> str:
        return f'Fruit("{self._fruit}")'

    def __str__(self) -> str:
        return self._fruit


class Branch(BinaryFruitTree):
    """Branches can lead to more branches or directly to fruit"""
    def __init__(self, left: BinaryFruitTree, right: BinaryFruitTree):
        self._left = left
        self._right = right

    def __repr__(self) -> str:
        return f"Branch({repr(self._left)}, {repr(self._right)})"

    def __str__(self) -> str:
        return f"--({str(self._left)}, {str(self._right)})"

    def min_height(self, counter=0) -> int:
        """There is fruit out there somewhere!"""
        counter += 1
        return min(self._left.min_height(counter), self._right.min_height(counter))

def main():
    """Smoke test for tree height.  More in test_q1.py"""
    t = Branch(Branch(Fruit("apple"), Fruit("apple")),
               Branch(Fruit("apple"),
                      Branch(Fruit("apple"), Fruit("apple"))))
    print(t.min_height())
    assert t.min_height() == 2
    print("Passed smoke test; now try test_q1.py")

if __name__ == "__main__":
    main()