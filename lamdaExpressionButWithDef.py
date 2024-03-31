def reverse(s):
    return s[::-1]

reverse("Im strong")
print(reverse)

print((lambda s: s[:: -1])("Im a strong"))
