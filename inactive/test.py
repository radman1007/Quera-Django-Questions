a, b, c = map(int, input().split("?"))
print(max(
    a + b + c,
    a * b + c,
    a * (b + c),
    a * b + c,
    (a + b) * c,
    a * b * c,
))