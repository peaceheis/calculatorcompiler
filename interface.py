import processtomath
test_parser = processtomath.Parser("( one thousand plus two hundred thousand ) times seven - six + two")
test_parser = test_parser.assign_multipliers()
print(test_parser.symbols)
translated = test_parser.translate()
print(eval(translated))