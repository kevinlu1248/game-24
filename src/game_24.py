# Card Game of 24

import itertools

# from tqdm import tqdm

def calculate24(
    numbers: list[int], 
    n = 24,
    k = 4,
):
    """
    Given a list of k numbers, return True if it is possible to use all k numbers
    and the basic arithmetic operations (+, -, *, /) to obtain the value n.
    """
    for perm in itertools.permutations(numbers, k):
        for ops in itertools.product(['+', '-', '*', '/'], repeat=k-1): # get all possible combinations of operators
            curr = perm[0]

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
                    if curr % num != 0:
                        break
                    curr /= num
            else:
                if int(curr) == n:
                    # print(perm)
                    # print(ops)
                    return True
    return False

assert calculate24([1, 2, 3, 4]) == True
assert calculate24([1, 2, 3, 5]) == True
assert calculate24([2, 2, 6, 6]) == True
assert calculate24([3, 3, 8, 8]) == False
assert calculate24([4, 4, 4, 4]) == True
assert calculate24([1, 1, 1, 23]) == True

def check_solvable(k: int = 4):
    """
    Check probability of getting something solvable for all k cards
    """
    max_card = 13
    cards = [i for i in range(1, max_card)] * 4
    num_cards = len(cards)
    count = 0
    combinations = num_cards * (num_cards - 1) * (num_cards - 2) * (num_cards - 3) // (k * (k - 1) * (k - 2) * (k - 3))

    cache = {}
    percent = combinations // 100
    
    # for indices in tqdm(itertools.combinations(range(len(cards)), k), total=combinations):
    for i, indices in enumerate(itertools.combinations(range(len(cards)), k)):
        if i % percent == 0:
            print(f"{i}/{combinations}", end="\r")
        indices = tuple(sorted(indices))
        if indices in cache:
            count += cache[indices]
        else:
            cache[indices] = calculate24([cards[i] for i in indices])
        count += calculate24([cards[i] for i in indices])
    probability = count / combinations
    return probability

print(check_solvable())
