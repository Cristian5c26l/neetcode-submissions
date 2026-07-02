from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    student_name_with_highest_score = None
    highest_score = 0
    for name, score in scores:
        if score > highest_score:
            student_name_with_highest_score = name
            highest_score = score

    return student_name_with_highest_score

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
