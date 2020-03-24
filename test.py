from decimaltobinary import convert_decimal_to_binary
import sys

print(sys.argv[1])

print(type(sys.argv[1]))

nStr = sys.argv[1]

# nInt = int(nStr)

print(type(nStr))

# print(type(nInt))

print(convert_decimal_to_binary(nStr))