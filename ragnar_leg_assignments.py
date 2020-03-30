# Assigning Ragnar legs with Hungarian Method library function

from scipy.optimize import linear_sum_assignment
import numpy as np
from collections import OrderedDict

def main():
    # Dictionary of runner names to preferences, empty if no preference
    runners = OrderedDict({
        "AD": [9,3,12],
        "NW": [8,6,12],
        "BS": [9,3,12],
        "JW": [6,9,10],
        "CF": [11, 7, 2],
        "AP": [],
        "NR": [6,9,10],
        "DM": [9, 1,10],
        "KB": [1,6,5],
        "AB": [7, 9, 3],
        "ST": [],
        "RM": [],
    })

    leg_arr = np.zeros((12,12))

    for name in runners.keys():
        
        index = list(runners.keys()).index(name)

        # Lower rank implies higher preference
        rank = -3

        for p in runners[name]:
            
            # subtract one to adjust leg to index
            leg_arr[index][p - 1] = rank
            rank += 1

    print(leg_arr)

    a_row, a_col = linear_sum_assignment(leg_arr)
    assignments = zip(a_row, a_col)
    assignments_asc = sorted(assignments, key=lambda a: a[1])

    for assignment in assignments_asc:
        runner_id = assignment[0]

        # re-adjust leg index to actual number
        leg_num = assignment[1] + 1
        runner_name = list(runners.items())[runner_id]

        print(f"{leg_num}: {str(runner_name)}")

if __name__ == "__main__":
    main()
    