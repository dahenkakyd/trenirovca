from calcylator import Calculator #из файла calculator импортируй класс
calculator=Calculator()
print("start")
res = calculator.sum(4, 5)
assert res == 9
print(res)
print("finish")