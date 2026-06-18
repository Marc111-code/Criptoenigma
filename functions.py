def alphabet_list():
    abc = []
    a = 97
    while a <= 122:
        abc = abc + list(chr(a))
        a = a + 1
    return abc

def old_pos(x,n,malphabet):
    return (x-n) % malphabet
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

def decrypt_cesar(s,n,alphabet):
    fin = ""
   
    for lletra in s:
        pos = old_pos(alphabet.index(lletra),n, len(alphabet) )
        fin = fin + alphabet[pos]
        
    return fin
print(decrypt_cesar("cab",2,['a','b','c',]))
