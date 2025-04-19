
first = input("python")
second = input("Programming language")


second_set = set(second)


result = ''.join(dict.fromkeys(c for c in first if c not in second_set))

