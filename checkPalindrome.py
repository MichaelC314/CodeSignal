def checkPalindrome(inputString):
    Length = len(inputString)
    The_Middle = int(len(inputString)/2)
    for num in range(0, The_Middle):
        if inputString[num] != inputString[Length-num-1]: return False
    return True
    
