if __name__ == "__main__":
    import sys
    sys.path.append("../../")
import unittest
from sutil.enum_meta import EnumMeta


class EnumMetaTest(unittest.TestCase):

    def test_normal(self):
        class TestEnum(metaclass=EnumMeta):
            ENUM1 = 1
            ENUM2 = 2
        self.assertEqual(1, TestEnum.ENUM1)
        self.assertEqual(2, TestEnum.ENUM2)

    def test_duplicated_value(self):
        def do_duplicated_value():
            class TestEnum(metaclass=EnumMeta):
                ENUM1 = 1
                ENUM2 = 1
        self.assertRaises(Exception, do_duplicated_value)

    def test_instantiation(self):
        def do_instantiation():
            class TestEnum(metaclass=EnumMeta):
                ENUM1 = 1
            a = TestEnum()
        self.assertRaises(Exception, do_instantiation)

    def test_contains(self):
        class TestEnum(metaclass=EnumMeta):
            ENUM1 = 1
        self.assertTrue(1 in TestEnum)
        self.assertFalse(2 in TestEnum)

    def test_iter(self):
        class TestEnum(metaclass=EnumMeta):
            ENUM1 = 1
            ENUM2 = 2
            ENUM3 = 3
        values = set()
        for x in TestEnum:
            values.add(x)
        self.assertEqual({1, 2, 3}, values)


if __name__ == "__main__":
    unittest.main()
