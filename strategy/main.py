from strategy import AddStrategy, SubtractStrategy, MultiplyStrategy, Context

f = {"add_strategy": AddStrategy, "subtract_strategy": SubtractStrategy, "multiply_strategy": MultiplyStrategy}

for key, value in f.items():
    a, b = 5, 3
    print(key)
    context = Context(value(), a, b)
    print(context(None, None))
