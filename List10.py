def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i=0
    num1=0
    num2=0
    while i<len(list1):
        if list1[i]==0:
            num1+=list1[i]+1
        elif list1[i]==1:
            num2+=list1[i]
        i+=1
    return [num1,num2]
print(main([1, 0, 0, 0, 1, 0, 1, 0]))
print(main([0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]))