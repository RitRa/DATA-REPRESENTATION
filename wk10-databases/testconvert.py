colnames=["id", "name", "age"]
result = (1, "Mary", 21)
item = {}

for i, colname in enumerate(colnames):
    value = result[i]
    item[colname] = value

print(item)