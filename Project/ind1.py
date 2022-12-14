# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_1(type_="max"):
    def func_2(lst):
        if type_ == "max":
            return max(lst)
        else:
            return min(lst)

    return func_2


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 65, 6]

    max_func = func_1()
    min_func = func_1("min")

    print(max_func(a))
    print(min_func(a))
