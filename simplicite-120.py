# return string without spaces
def erase(cc):
    
    s1 = ""

    if (len(cc) > 1) :
        if (cc[0] != ' ' or cc[0] == ' ' and cc[1] == ' ') :
            s1 += "".join(cc[0])
    i = 1
    
    
    while (i < len(cc) - 1) :
        if (cc[i] != ' ' or (cc[i - 1] == ' ' or cc[i + 1] == ' ')) :
            s1 += "".join(cc[i])
        i += 1
        
        
    if (len(cc) > 1) :
        if (cc[len(cc) - 1] != ' ' or cc[len(cc) - 2] == ' ') :
            s1 += "".join(cc[len(cc) - 1])

    return s1      
