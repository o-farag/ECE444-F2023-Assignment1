class utils:
    #can only be integers > 0
    def reversed(x):
        xStr = str(x)
        if xStr.isdigit():
            return int(xStr[::-1])
        else:
            return "invalid input"
        
    def formatter(x):
        xStr = str(x)
        if xStr.isdigit():
            return bin(int(xStr)), oct(int(xStr))
        else:
            return "invalid input"
        