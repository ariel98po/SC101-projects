# """
# this is created for practicing the note of week3
# """
#
# import random
#
# # 1
#
# s = ''
# for i in range(4):
#     roll = random.randint(1,6)
#     s += str(roll)
# print(s)
#
# # 2
# ## list
# l = []
# l = ["SC"]
# l += [1,0,1]
# print(l)
# length = len(l)
# print(length)
# print(l[1:])
# ele = l[0]
# print(ele)
#
# l.append(3.14)
# print(l)
# l.append(['Jerry'])
# print(l)
# print(len(l))
# l[0] = 'J'
# print(l)
#
#
# ## string
# s=""
# s="SC"
# s +="101"
# print(s)
# print(len(s))
# s[1:]
# eles = s[0]
# print(eles)
# s += str(3.14)
# print(s)

# stack & queue

# l = [1,2,3]
# l.pop()
# print(l)
#
# l.append(4)
# print(l)
#
# l.pop(0)
# print(l)
# l.insert(0,'Jerry')
# print(l)

"""
This program averages the input scores
"""

# CONSTANT
EXIT = -1


def main():
    print(f'This program averages the inputs, or enter {EXIT} to exit')
    lst = []

    while True:
        score = int(input('Enter the score:'))
        if score == EXIT:
            break

        lst += score

    print('The average is :', average_by_index(lst))
    print('The average is :', average_by_for_each(lst))


def average_by_index(scores):
    """
    	:param scores: (list) Containing all the scores input by user
    	:return : (float) The average of the elements in scores
    	----------------------------------------------
    	This function uses indices in for loop to calculate
    	the average of scores
    	"""
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    return total / len(scores)



def average_by_for_each():
    """
    :param scores: (list) Containing all scores input by user
    :return: (float) The average of the elements in scores
    --------------------------------------------
    This function uses for each loop to calculate
    the average of scores
    """
