def sum_list(numbers):
    return sum(numbers)

def count_negatives(numbers):
    return sum(1 for x in numbers if x < 0)
