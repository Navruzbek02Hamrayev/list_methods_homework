def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    return numbers, numbers.pop(i)
print(main( [1, 2, 3, 4, 5],2))
print(main([4, 7, 3, 2, 8],4))