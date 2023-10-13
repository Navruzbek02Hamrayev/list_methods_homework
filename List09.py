def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    l=[]
    list1=[]
    i=0
    sum=0
    while i<len(fruits):
        if fruits[i]=="apple":
            sum+=1
            list1.append(i)
        i+=1
    return list1,sum
print(main( ["apple", "banana", "apple", "pear", "apple"]))
print(main(["apple", "apple", "apple", "apple", "kiwi"]))