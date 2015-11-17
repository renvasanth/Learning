def greater(numbers):
    """function to return the biggest number
    
    Args:
        numbers (list) - list of numbers either int or float
    Returns:
        biggest (int/float) - biggest value in list numbers
    """
    a = 0
    b = 1
    while a < 5 and b < 5:
        if numbers[a] > numbers[b]:
            answer = numbers[a]
            b = b + 1
        else:
            answer = numbers[b]
            a = a + 1
    return answer

print greater([5, 25, 95, 3, 17])
