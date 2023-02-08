print("UNION")
set_a = {"col", "mex", "bol"}
set_b = {"bol", "per"}
# set_c = set_a.union(set_b)
set_c = set_a | set_b
print(set_c)

print("INTERSECCIÓN")
set_c = set_a.intersection(set_b)
set_c = set_a & set_b # Con esto se hace la intersección.
print(set_c)

print("DIFFERENCE")
set_c = set_a.difference(set_b)
set_c = set_a - set_b
print(set_c)

print("SYMETRIC DIFFERENCE")
set_c = set_a.symmetric_difference(set_b)
set_c = set_a ^ set_b
print(set_c)
