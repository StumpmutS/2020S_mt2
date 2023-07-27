"""Q2. A bit of fun, really.
We will pack and unpack unsigned binary
fields into 16-bit words (represented by
Python ints).

Fields are
    x in range 0..31  (5 bits)  in bits 11..15
    y in range 0..31  (5 bits)  in bits 6..10
    z in range 0..63  (6 bits)  in bits 0..5
"""

from typing import Tuple

#
def pack556(x: int, y: int, z: int) -> int:
    """Pack small integers into 1 integer.
    x is in range 0..31  (5 bits) and goes in bits 11..15
    y is in range 0..31  (5 bits) and goes in bits 6..10
    z is in range 0..63  (6 bits) and goes in bits 0..5
    """
    assert 0 <= x <= 31  # 5 bits
    assert 0 <= y <= 31  # 5 bits
    assert 0 <= z <= 63  # 6 bits
    result = (x << 11) | (y << 6) | z
    print(result)
    return result

def unpack556(w: int) -> Tuple[int, int, int]:
    """Assume w was created by 'pack556'"""
    x = (w & 0b1111100000000000) >> 11
    y = (w & 0b0000011111000000) >> 6
    z = w & 0b0000000000111111

    return x,y,z


def main():
    """Smoke test"""
    assert pack556(31,31,63) == 0b1111111111111111
    assert unpack556(pack556(31,31,63)) == (31,31,63)
    assert unpack556(pack556(3,5,9)) == (3,5,9)
    print("Passed smoke test; try test_q2.py to be more thorough")

if __name__ == "__main__":
    main()



