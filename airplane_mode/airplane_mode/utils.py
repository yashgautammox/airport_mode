import random




def create_random():
    number=random.randint(1,99)
    letter=random.choice('ABCDE')

    return f"{number}{letter}"