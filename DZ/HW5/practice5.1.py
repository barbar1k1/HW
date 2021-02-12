a = ["EejgKgiiGugGF", "hwgwUEGGHuewghw", "sgheHUREIHrghe"]
def operation(a,operation):
    return operation(a)
def upper(a):
    res = list(map(str.upper, a))
    return res
def lower(a):
    res = list(map(str.lower, a))
    return res
print(operation(a, upper))