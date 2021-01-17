if __name__ == "__main__":
    import sys
    sys.path.append("../../")
import unittest
from sutil.singleton_meta import SingletonMeta


class SingletonMetaTest(unittest.TestCase):

    def test_normal(self):
        class TestSingleton(metaclass=SingletonMeta):
            pass
        t1 = TestSingleton()
        t2 = TestSingleton()
        self.assertTrue(t1 is t2)


if __name__ == "__main__":
    unittest.main()
