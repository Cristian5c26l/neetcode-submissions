from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    set_str = set()
    
    for k in keys:
        set_str.add(k)

    return set_str


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    existing_keys = []
    for k in keys:
        existing_keys.append(k in hash_set)

    return existing_keys


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
