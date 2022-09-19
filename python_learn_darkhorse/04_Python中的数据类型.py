# 方式1：使用print直接输出类型信息
print(type("123"))
print(type(123))
print(type(123.123))

# 方式2：使用变量存储typr存储的结果
string_type = type("123")
int_type = type(123)
float_type = type(123.123)
print(string_type)
print(int_type)
print(float_type)

# 方式3：使用type()语句查看变量中存储的数据类型数据
name = "123"
name_type = type(name)
print(name_type)
