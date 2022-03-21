# dictionary =  A changable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Poland": "Warsaw"}

capitals.update({"Germany": "Berlin"})

print(capitals["Poland"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)
