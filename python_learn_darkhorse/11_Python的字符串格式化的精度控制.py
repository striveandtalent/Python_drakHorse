"""
我们可以使用辅助符号"m.n"来控制数据的宽度和精度
 m :控制宽度,要求是数字(很少使用) ,设置的宽度小于数字自身，不生效
.n :控制小数点精度,要求是数字,会进行小数的四舍五入
%5d:表示将整数的宽度控制在5位，如数字11,被设置为5d,就会变成: [空格][空格][空格]11,用三个空格补足宽度。
%5.2f:表示将宽度控制为5，将小数点精度设置为2

※※※小数点和小数部分也算入宽度计算※※※
如，对11.345设置了%7.2f后，结果是: [空格][空格]11.35。 2个空格补足宽度,小数部分限制2位精度后，四舍五入为11.35
"""

name2 = "传播智客"
set_up_year = 2006
stock_price = 19.99
message2 = "我是：%s，我成立于：%d，我今天的股价是：%5.2f" % (name2, set_up_year, stock_price)
message3 = "我是：%s，我成立于：%d，我今天的股价是：%.4f" % (name2, set_up_year, stock_price)
print(message2)
print(message3)
