from itertools import combinations

def form_groups_fixed_size(student_names, interactions, group_size):
    groups = []
    students_combinations = combinations(student_names, group_size)

    for combo in students_combinations:
        valid_group = True
        for pair in combinations(combo, 2):
            try:
                if pair[1] in interactions[pair[0]] or pair[0] in interactions[pair[1]]:
                    valid_group = False
                    break
            except:pass
        if valid_group:
            groups.append(combo)

    return groups

# Example usage:
import StudentSorter
students,interactions=StudentSorter.main()

group_size = 4
result_groups = form_groups_fixed_size(students, interactions, group_size)
for i, group in enumerate(result_groups, start=1):
    print(f"Group {i}: {', '.join(group)}")

