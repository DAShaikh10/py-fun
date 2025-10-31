import math


class Calculator:
    _instance = None
    single_digit_words = {
        # English.
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        # Deutsch.
        "null": 0,
        "eins": 1,
        "zwei": 2,
        "drei": 3,
        "vier": 4,
        "fünf": 5,
        "fuenf": 5,  # Tolerate missing umlaut.
        "sechs": 6,
        "sieben": 7,
        "acht": 8,
        "neun": 9,
        "zehn": 10,
        # Spanish.
        "cero": 0,
        "uno": 1,
        "dos": 2,
        "tres": 3,
        "cuatro": 4,
        "cinco": 5,
        "seis": 6,
        "siete": 7,
        "ocho": 8,
        "nueve": 9,
        "diez": 10,
        # Russian.
        "ноль": 0,
        "один": 1,
        "два": 2,
        "три": 3,
        "четыре": 4,
        "пять": 5,
        "шесть": 6,
        "семь": 7,
        "восемь": 8,
        "девять": 9,
        "десять": 10,
        # Chinese.
        "零": 0,
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
        "十": 10,
        # Roman numerals.
        "i": 1,
        "ii": 2,
        "iii": 3,
        "iv": 4,
        "v": 5,
        "vi": 6,
        "vii": 7,
        "viii": 8,
        "ix": 9,
        "x": 10,
    }

    def __new__(self):
        if Calculator._instance is None:
            Calculator._instance = super().__new__(self)

        return Calculator._instance

    def validate(self, *args):
        result = []
        for arg in args:
            parsed_value = self.parse(arg)

            if parsed_value is None:
                raise ValueError("Invalid input for addition \\ input not supported")

            result.append(parsed_value)

        return result

    def parse(self, value: str | int):
        if isinstance(value, (int, float)):
            return value

        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                try:
                    return self.single_digit_words.get(value.strip().lower())
                except:
                    return 0

    def add(self, num1: int | str, num2: int | str) -> int:
        print(num1, num2)
        nums: list[int] = self.validate(num1, num2)

        return nums[0] + nums[1]

    def sub(self, num1: int | str, num2: int | str) -> int:
        nums: list[int] = self.validate(num1, num2)

        return nums[0] - nums[1]

    def mul(self, num1: int | str, num2: int | str) -> int:
        nums = self.validate(num1, num2)

        return nums[0] * nums[1]

    def div(self, num1: int | str, num2: int | str) -> float:
        nums = self.validate(num1, num2)

        return nums[0] / nums[1]

    def factorize(self, n: int | str) -> list[int]:
        """
        Returns a list of the prime factors of a given integer.

        Args:
            n: An integer to be factorized.

        Returns:
            A list of integers representing the prime factors of n.
            Returns an empty list if n < 2.
        """
        n = self.validate(n)[0]

        if n < 2:
            return []

        factors = []

        while n % 2 == 0:
            factors.append(2)
            n //= 2

        # n must be odd at this point. Iterate through odd numbers.
        # We only need to check up to the square root of n.
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        # If n is a prime number greater than 2, it will be left at the end.
        if n > 2:
            factors.append(n)

        return factors
