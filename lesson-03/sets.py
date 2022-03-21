# set =     collection which is unordered, unindexed. No duplicate values

from dis import dis


utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
utensils.update(dishes)

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)
