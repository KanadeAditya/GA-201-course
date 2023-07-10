def reversestring(strr):
    newstr=''
    i=len(strr)-1
    while i>=0:
        newstr += strr[i]
        i = i-1 

    return newstr

string = reversestring("Python is Fun")
print(string)