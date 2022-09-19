# 将数字转换成字符串(任何类型都能完美转换成字符串)
num_str = str(123)
print(type(num_str), num_str)

float_str = str(123.123)
print(type(float_str), float_str)

# 将字符串转换成数字
num = int("123")
print(type(num), num)

num2 = float("123.123")
print(type(num2), num2)

# 错误示例，想要将字符申转换成数字，必须要求字符申内的内容都是数字
# num3 = int("黑马程序员")
# print(type(num3), num)

# 整数转浮点数
num4 = float(11)
print(type(num4), num4)

# 浮点数转整数(丢失小数部分)
num5 = int(123.456)
print(type(num5), num5)
