import unittest
from main import TestGenerator


class TestTestGenerator(unittest.TestCase):
    def setUp(self):
        self.characteristics = {
            "a": ["a1", "a2"],
            "b": ["b1", "b2", "b3"],
            "c": ["c1", "c2"]
        }
        self.generator = TestGenerator(self.characteristics)

    def test_ACoC(self):
        expected = [
            ('a1', 'b1', 'c1'), ('a1', 'b1', 'c2'), ('a1', 'b2', 'c1'), ('a1', 'b2', 'c2'),
            ('a1', 'b3', 'c1'), ('a1', 'b3', 'c2'), ('a2', 'b1', 'c1'), ('a2', 'b1', 'c2'),
            ('a2', 'b2', 'c1'), ('a2', 'b2', 'c2'), ('a2', 'b3', 'c1'), ('a2', 'b3', 'c2')
        ]
        result = self.generator.ACoC()
        self.assertCountEqual(result, expected)  # Using assertCountEqual to ignore order

    def test_ECC(self):
        expected = [
            ('a1', 'b1', 'c1'), ('a2', 'b2', 'c2'), ('a1', 'b3', 'c1')
        ]
        result = self.generator.ECC()
        self.assertEqual(result, expected)

    def test_BCC(self):
        base_choice = {"a": "a1", "b": "b1", "c": "c1"}
        expected = [
            ('a1', 'b1', 'c1'), ('a2', 'b1', 'c1'), ('a1', 'b2', 'c1'), ('a1', 'b3', 'c1'), ('a1', 'b1', 'c2')
        ]
        result = self.generator.BCC(base_choice)
        self.assertEqual(result, expected)

    def test_MBCC(self):
        base_tests = [
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2')
        ]
        expected = [
            ('a1', 'b1', 'c1'), ('a2', 'b2', 'c2'), ('a2', 'b1', 'c1'), ('a1', 'b2', 'c1'),
            ('a1', 'b1', 'c2'), ('a1', 'b3', 'c1'), ('a1', 'b2', 'c2'), ('a2', 'b1', 'c2'),
            ('a2', 'b3', 'c2'), ('a2', 'b2', 'c1')
        ]
        result = self.generator.MBCC(base_tests)
        self.assertCountEqual(result, expected)  # Using assertCountEqual to ignore order

    def test_empty_characteristics(self):
        generator = TestGenerator({})
        expected = [()]
        result = generator.ACoC()
        self.assertEqual(result, expected)

    def test_single_element_characteristics(self):
        characteristics = {"a": ["a1"], "b": ["b1"], "c": ["c1"]}
        generator = TestGenerator(characteristics)
        expected = [('a1', 'b1', 'c1')]
        result = generator.ACoC()
        self.assertEqual(result, expected)

    def test_invalid_base_choice(self):
        base_choice = {"x": "invalid"}
        with self.assertRaises(KeyError):
            self.generator.BCC(base_choice)

    def test_single_characteristic(self):
        characteristics = {"a": ["a1", "a2"]}
        generator = TestGenerator(characteristics)
        expected = [('a1',), ('a2',)]
        result = generator.ACoC()
        self.assertEqual(result, expected)

    def test_ECC_with_single_characteristic(self):
        characteristics = {"a": ["a1", "a2", "a3"]}
        generator = TestGenerator(characteristics)
        expected = [('a1',), ('a2',), ('a3',)]
        result = generator.ECC()
        self.assertEqual(result, expected)

    def test_BCC_with_missing_key(self):
        base_choice = {"a": "a1", "b": "b1"}
        with self.assertRaises(KeyError):
            self.generator.BCC(base_choice)

    def test_MBCC_with_single_base_test(self):
        base_tests = [
            ('a1', 'b1', 'c1')
        ]
        expected = [
            ('a1', 'b1', 'c1'), ('a2', 'b1', 'c1'), ('a1', 'b2', 'c1'), ('a1', 'b3', 'c1'),
            ('a1', 'b1', 'c2')
        ]
        result = self.generator.MBCC(base_tests)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
