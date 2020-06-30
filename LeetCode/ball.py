import random

empty_count = 0


def empty_10(box):
    count = 0
    for i in box:
        if i != 1:
            count += 1
    if count == 10:
        return True
    return False


def random_choice():
    global empty_count
    ball = [i for i in range(1, 10 + 1)]
    box = {i: 0 for i in range(1, 12 + 1)}
    for _ in ball:
        choice_idx = random.randint(1, 12)
        box[choice_idx] += 1
    print(box)
    if empty_10(box):
        empty_count += 1


for _ in range(0, 100000):
    random_choice()

print(float(empty_count) / 100000)
