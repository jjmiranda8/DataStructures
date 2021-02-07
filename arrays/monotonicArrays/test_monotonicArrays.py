import monotonicArrays
import pytest

def test_main():

   assert monotonicArrays.main([1, 1, 1, 1]) ==  True

   assert monotonicArrays.main([2, 3, 3, 33, 69, 300]) == True

   assert monotonicArrays.main([1, 0, -1, -2, -3, -3, -3, -4]) == True
