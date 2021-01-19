import smallestDifference
import pytest

def test_main():

   assert smallestDifference.main([-1, 5, 10, 20, 28, 3], [26,  134, 135, 15, 17]) == [28, 26]
