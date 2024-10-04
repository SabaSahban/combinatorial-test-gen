import itertools
import argparse
from typing import List, Dict, Tuple, Union


class TestGenerator:
    def __init__(self, characteristics: Dict[str, List[str]]):
        self.characteristics = characteristics

    def ACoC(self) -> List[Tuple[str, ...]]:
        values = [self.characteristics[key] for key in self.characteristics]
        return list(itertools.product(*values))

    def ECC(self) -> List[Tuple[str, ...]]:
        max_length = max(len(values) for values in self.characteristics.values())
        test_cases = [
            tuple(self.characteristics[key][i % len(self.characteristics[key])]
                  for key in self.characteristics)
            for i in range(max_length)
        ]
        return test_cases

    def BCC(self, base_choice: Dict[str, str]) -> List[Tuple[str, ...]]:
        test_cases = [tuple(base_choice[key] for key in self.characteristics)]

        for key in self.characteristics:
            original_value = base_choice[key]
            for value in self.characteristics[key]:
                if value != original_value:
                    new_choice = {k: (value if k == key else base_choice[k]) for k in self.characteristics}
                    test_cases.append(tuple(new_choice[k] for k in self.characteristics))

        return test_cases

    def MBCC(self, base_tests: List[Tuple[str, ...]]) -> List[Tuple[str, ...]]:
        test_cases = {base_test for base_test in base_tests}

        for base_test in base_tests:
            base_dict = {key: base_test[i] for i, key in enumerate(self.characteristics.keys())}
            for key in self.characteristics:
                original_value = base_dict[key]
                for value in self.characteristics[key]:
                    if value != original_value:
                        new_choice = base_dict.copy()
                        new_choice[key] = value
                        test_cases.add(tuple(new_choice[k] for k in self.characteristics))

        return list(test_cases)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test Case Generator")

    parser.add_argument(
        "characteristics",
        type=str,
        help="Characteristics and their values in the format 'char1=val1,val2 char2=val1,val2'"
    )
    parser.add_argument(
        "algorithm",
        type=str,
        choices=["ACoC", "ECC", "BCC", "MBCC"],
        help="Algorithm to use for generating test cases"
    )
    parser.add_argument(
        "--base-choice",
        type=str,
        help="Base choice for characteristics in the format 'char1=val1 char2=val2'",
        default=None
    )
    parser.add_argument(
        "--base-tests",
        type=str,
        help="Base tests for multiple base choice coverage, separated by semicolons. Each test in the format 'char1=val1,char2=val2'",
        default=None
    )

    return parser.parse_args()


def parse_characteristics(characteristics_str: str) -> Dict[str, List[str]]:
    characteristics = {}
    for item in characteristics_str.split():
        char, values = item.split('=')
        characteristics[char] = values.split(',')
    return characteristics


def parse_base_choice(base_choice_str: str) -> Dict[str, str]:
    base_choice = {}
    for item in base_choice_str.split():
        char, value = item.split('=')
        base_choice[char] = value
    return base_choice


def parse_base_tests(base_tests_str: str) -> List[Tuple[str, ...]]:
    base_tests = []
    for test in base_tests_str.split(';'):
        test_dict = {}
        for item in test.split(','):
            char, value = item.split('=')
            test_dict[char] = value
        base_tests.append(tuple(test_dict.values()))
    return base_tests


def main():
    args = parse_arguments()

    characteristics = parse_characteristics(args.characteristics)
    generator = TestGenerator(characteristics)

    if args.algorithm == "BCC":
        if not args.base_choice:
            print("Base choice must be provided for BCC algorithm.")
            return
        base_choice = parse_base_choice(args.base_choice)
        test_cases = generator.BCC(base_choice)
    elif args.algorithm == "MBCC":
        if not args.base_tests:
            print("Base tests must be provided for MBCC algorithm.")
            return
        base_tests = parse_base_tests(args.base_tests)
        test_cases = generator.MBCC(base_tests)
    elif args.algorithm == "ACoC":
        test_cases = generator.ACoC()
    elif args.algorithm == "ECC":
        test_cases = generator.ECC()
    else:
        print("Invalid algorithm choice.")
        return

    print("\nGenerated test cases:")
    for test_case in test_cases:
        print(test_case)


if __name__ == "__main__":
    main()

# python main.py "a=a1,a2 b=b1,b2,b3 c=c1,c2" ACoC
# python main.py "a=a1,a2,a3 b=b1 c=c1,c2 d=d1,d2,d3,d4,d5" ECC
# python main.py "a=a1,a2 b=b1,b2,b3 c=c1,c2" BCC --base-choice "a=a1 b=b2 c=c1"
# python main.py "a=a1,a2,a3 b=b1,b2,b3 c=c1,c2" MBCC --base-tests "a=a1,b=b1,c=c2;a=a2,b=b2,c=c1"
