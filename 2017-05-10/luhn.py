import unittest

# regras
# 1 - Números em em casa ímpar multiplica-se por x2
# 2 - Números maiores que nove, subtrai-se 9
# 3 - (sum(numeros) % 10) == 0


def double(string):
    nums = [int(i) for i in string]

    return [n if i % 2 == 0 else 2 * n
            for i, n in enumerate(nums)]


def minus9(numbers):
    return (n if n <= 9 else n-9 for n in numbers)

    
def gensum(code):
    digits = minus9(double(code))
    return (sum(digits) * 9) % 10


def checksum(number):
    return gensum(number[:-1]) == int(number[-1])


class TestDojoMethods(unittest.TestCase):

    def test_double(self):
        self.assertEqual(double("0"), [0])
        self.assertEqual(double("0123"), [0, 2, 2, 6])
        self.assertEqual(double("3752"), [3, 14, 5, 4])

    def test_maior9(self):
        self.assertEqual(list(minus9([0])), [0])
        self.assertEqual(list(minus9([0, 2, 2, 6])), [0, 2, 2, 6])
        self.assertEqual(list(minus9([3, 14, 5, 4])), [3, 5, 5, 4])

    def test_gensum(self):
        self.assertEqual(gensum("0"), 0)
        self.assertEqual(gensum("7992739871"), 3)
        self.assertEqual(gensum("201773"), 9)

    def test_checksum(self):
        self.assertTrue(checksum("79927398713"))
        self.assertFalse(checksum("79927398712"))

    def test_generic(self):
        self.assertEqual(True, True)
        self.assertFalse(0==1)
        self.assertTrue(0==0)
if __name__ == '__main__':
    unittest.main()