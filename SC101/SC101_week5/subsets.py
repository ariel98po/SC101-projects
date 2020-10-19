"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists(['a', 'b', 'c', 'd', 'a'])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    list_sub_lists_helper(lst, [])


def list_sub_lists_helper(lst, chosen):
    if len(lst) == 0:
        print(chosen)

    else:
        element = lst.pop()

        # Not choose and explore
        list_sub_lists_helper(lst, chosen)

        # Choose and explore
        chosen.append(element)
        list_sub_lists_helper(lst, chosen)
        # Un-choose
        chosen.pop()
        lst.append(element)



if __name__ == '__main__':
    main()
