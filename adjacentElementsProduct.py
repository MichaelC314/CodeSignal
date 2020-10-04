def adjacentElementsProduct(inputArray):
    lst = inputArray
    Count = 1
    Largest = None
    for num in lst:
        try: Current_Sum = num * lst[Count]
        except: break
        if Count == 1: Largest = Current_Sum
        if Current_Sum >= Largest: Largest = Current_Sum
        Count += 1
    return Largest
