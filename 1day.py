"""
This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""


def elf_carries_report():
    result = dict()
    file = open("input-1day.txt", mode='r')
    lines = file.readlines()
    elf_no = 1
    carries = 0
    space_flag = False
    for elem in lines:
        calories = elem.strip()

        if not calories:
            if space_flag:
                continue
            space_flag = True
            result[elf_no] = carries
            elf_no += 1
            carries = 0
        else:
            space_flag = False
            carries += int(calories)
    file.close()
    return result


def top_elf_with_max_carries(elf_report):
    max_carries = max(elf_report.values())
    for elf, elf_carries in elf_report.items():
        if elf_carries == max_carries:
            return {'elf_no': elf, 'elf_carries': elf_carries}


def sum_of_top_three_elf_carries(lst):
    list_of_carries = []
    list_of_carries.extend(lst)
    list_of_carries.sort(reverse=True)
    return sum(list_of_carries[:3])


if __name__ == "__main__":
    report = elf_carries_report()

    top_elf = top_elf_with_max_carries(report)
    print(f'< The maximum amount of snacks takes Elf #{top_elf["elf_no"]}. It takes {top_elf["elf_carries"]}. >')

    print(sum_of_top_three_elf_carries(list(report.values())))

