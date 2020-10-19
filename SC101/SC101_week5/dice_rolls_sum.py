"""
File: dice_rolls_sum.py
Name:
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8
count = 0

def main():
    dice_sum(TOTAL)
    print(count)

def dice_sum(target_sum):

    dice_sum_helper(target_sum, [])

def dice_sum_helper(target_sum, current_dice):
    global count
    count += 1

    if sum(current_dice) == target_sum:
        print(current_dice)

    else:
        if sum(current_dice) <= target_sum:
            for die in [1, 2, 3, 4, 5, 6]:
                if target_sum - sum(current_dice) >= die:
                    # Choose
                    current_dice.append(die)
                    # Explore
                    dice_sum_helper(target_sum, current_dice)
                    # Un-choose
                    current_dice.pop()
                else:
                    return




if __name__ == '__main__':
    main()
