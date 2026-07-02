from typing import List, Dict

"""
Time and Space Complexity

Time complexity: 
O
(
1
)
O(1)
The zip() function returns an iterator at the beginning of the input lists, so it doesn't traverse the entire lists.

Space complexity: 
O
(
1
)
O(1)
The zip() function returns an iterator so it doesn't actually create a new list of tuples in memory.
"""

def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    students_dict = {}
    for name, score in zip(names, scores):
        students_dict[name] = score

    return students_dict



# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
