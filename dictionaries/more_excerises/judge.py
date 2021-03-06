a_command = input()
total_points = {}
contest_dict = {}

while a_command != "no more time":
    user, contest, points = a_command.split(" -> ")
    points = int(points)

    if contest not in contest_dict:
        contest_dict[contest] = {}

    if user not in contest_dict[contest]:
        contest_dict[contest][user] = points
    elif user in contest_dict[contest]:
        if contest_dict[contest][user] <= points:
            contest_dict[contest][user] = points

    if user not in total_points:
        total_points[user] = {}

    if contest not in total_points[user]:
        total_points[user][contest] = points
    elif contest in total_points[user]:
        if total_points[user][contest] <= points:
            total_points[user][contest] = points

    a_command = input()

totals_for_sorted = {}

for key, points in total_points.items():
    name = key
    totals = sum(points.values())
    totals_for_sorted[key] = totals

# print(totals_for_sorted)
for key, contestant in contest_dict.items():
    print(f"{key}: {len(contestant)} participants")
    sorted_contestant = sorted(contestant.items(), key=lambda kvpt: (-kvpt[1],kvpt[0]))
    m = 0
    for val in sorted_contestant:
        m += 1
        print(f"{m}. {val[0]} <::> {val[1]}")

print("Individual standings:")
n = 0
sorted_total_points = sorted(totals_for_sorted.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
for name, points in sorted_total_points:
    n += 1
    print(f"{n}. {name} -> {points}")
