animals = ["cow", "buffalo", "sheep"]

def reverse_len(s):
    return -len(s)

sorting = sorted(animals, key=reverse_len)

print(sorting)


# Or use lamda expression state
animals2 = ["goat", "chicken", "horse"]
sorting2 = sorted(animals2, key=lambda s: -len(s))

print(sorting2)