#!/usr/bin/env python3
# Created by : Samuel Nkongolo
# Date: Dec. 11, 2022
# This program gets a random number, attaches it to a list and finds it's average.

import avg_constants
import random


def main():
    # Creating a list for math.
    num_list = []
    sum_num = 0
    for i in range(avg_constants.MAX_ARRAY_SIZE):
        # Initializing a random number and adding it to a list.
        rand_num = random.randint(avg_constants.MIN_NUM, avg_constants.MAX_NUM)
        num_list.append(rand_num)
        sum_num += num_list[i]

    # Getting the final average.
    ans_num = sum_num / avg_constants.MAX_ARRAY_SIZE
    print(f"The average of {num_list} is {ans_num}")


if __name__ == "__main__":
    main()
