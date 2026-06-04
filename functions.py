def new_pos(x,n,malphabet):

    if x + n <= malphabet:
        return x + n
    else:
        a = x + n
        b = a - malphabet -1
        
    return b

def encrypt_cesar(s,n,alphabet):
    i = 0 
    fin = ""
    while i <= len(s)-1:
        pos = new_pos(i,n,len(alphabet) - 1)
        fin = fin + alphabet[pos]
        i = i + 1
    return fin    
print(encrypt_cesar("abc",2,['a','b','c']))
