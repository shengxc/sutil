if __name__ == "__main__":
    import sys
    import common
    sys.path.append(common.ROOT_DIR)
import unittest
from sutil import utils


class UtilsTest(unittest.TestCase):

    def test_clear_none_in_dict(self):
        d = {"a": 1, "b": None}
        self.assertEqual({"a": 1}, utils.clear_none_in_dict(d))
        d = {"a": 1, "b": {"c": None}}
        self.assertEqual({"a": 1, "b": {"c": None}}, utils.clear_none_in_dict(d, False))
        d = {"a": 1, "b": {"c": None}}
        self.assertEqual({"a": 1, "b": {}}, utils.clear_none_in_dict(d))

    def test_bound(self):
        self.assertEqual(3, utils.bound(10, 1, 3))
        self.assertEqual(1, utils.bound(-1, 1, 3))
        self.assertEqual(5, utils.bound(5, 1, 7))

    def test_chunk(self):
        self.assertEqual([[1], [2], [3]], list(utils.chunk([1,2,3], 1)))
        self.assertEqual([[1, 2], [3]], list(utils.chunk([1,2,3], 2)))
        self.assertEqual([[1, 2, 3]], list(utils.chunk([1,2,3], 3)))
        self.assertEqual([[1, 2, 3]], list(utils.chunk([1,2,3], 10)))


if __name__ == "__main__":
    unittest.main()
