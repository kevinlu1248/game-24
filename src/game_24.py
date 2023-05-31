# Card Game of 24

import itertools

from tqdm import tqdm

def calculate24(
    numbers: list[int], 
    n = 24,
    allow_fraction = True
):
    """
    Given a list of k numbers, return True if it is possible to use all k numbers
    and the basic arithmetic operations (+, -, *, /) to obtain the value n.
    """
    k = len(numbers)
    for perm in itertools.permutations(numbers, k):
        for ops in itertools.product(['+', '-', '*', '/'], repeat=k-1): # get all possible combinations of operators
            curr: float = perm[0]
            for i in range(1, k):
                op = ops[i - 1]
                num = perm[i]
                if op == '+':
                    curr += num
                elif op == '-':
                    curr -= num
                elif op == '*':
                    curr *= num
                elif op == '/':
                    if allow_fraction and curr % num != 0:
                        break
                    curr /= num
            else:
                if int(curr) == n:
                    return True
    return False

assert calculate24([1, 2, 3, 4]) == True
assert calculate24([1, 2, 3, 5]) == True
assert calculate24([2, 2, 6, 6]) == True
assert calculate24([3, 3, 8, 8]) == False
assert calculate24([4, 4, 4, 4]) == True
assert calculate24([1, 1, 1, 23]) == True

def check_solvable(k: int = 4, n: int = 24):
    """
    Check probability of getting something solvable for all k cards
    """
    max_card = 13
    cards = [i for i in range(1, max_card)] * 4
    num_cards = len(cards)
    count = 0

    combinations = 1
    for i in range(k):
        combinations *= num_cards - i
        combinations //= i + 1
    
    pbar = tqdm(enumerate(itertools.combinations(range(len(cards)), k)), total=combinations)
    step = combinations // 10000
    
    for i, indices in pbar:
        if i % step == 0:
            pbar.set_description(f'Current percentage: {count}/{i}')
        count += calculate24([cards[i] for i in indices], n=n)
    probability = count / combinations
    return probability

# print(check_solvable())
print(check_solvable(6, 144))
