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


def new_alphabet(l,p):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res = []
    if 0>= len(p) or len(a) <= len(p):
        return p

    for lletra in p:     
        res = res + list(lletra)
    pos = a.index(lletra)
    i =pos
    while i < len(a):
        if a[i] not in p:
            res = res+ list(a[i])
        i=i+1
    
    i=0
    while i < pos:
        if a[i] not in p:
            res = res+ list(a[i])
        i=i+1   
    
    return res  
    
print(new_alphabet(12,"epsilon"))

def encrypt_monoalfabetic(s,kw,alphabet):
    x = new_alphabet(0,kw)
    i =0
    aux=""
    while i < len(s):
        a = alphabet.index(s[i])
        i = i + 1
        aux = aux + x[a]
    return aux


def decrypt_monoalfabetic(s,kw,alphabet):
    x = new_alphabet(0,kw)
    aux = ""
    i = 0
    for lletra in s:
        a = x.index(s[i])
        aux = aux + alphabet[a]
        i = i +1
    return aux

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def displaced_alphabet(alphabet,i):
    pos = l[i]
    res = []
    x=i
    
    
    while i< len(alphabet):
        res = res + list(l[i])
        i += 1
    i=0
    while i < x:
        res.append(l[i])
        i+=1
   
    return res    
print(displaced_alphabet(l,3))


def create_displaced_alphabet_list(l):
    i = 0 
    res = []
    while i <= len(l) - 1:
        res.append(displaced_alphabet(l,i))
        i = i + 1
    print(res)
create_displaced_alphabet_list(["a","b","c"])

def create_dictionary(l1,l2):
    res = {}
    i = 0
    while i < len(l1):
        res[l1[i]] = l2[i]
        i += 1
    return res
print(create_dictionary(["a","b","c"],["1","2","3"]))


def create_encrypt_alphabet_dictionary(l1,l2):
    res = {}
    i = 0
    while i < len(l1):
        a = create_dictionary(l1,l2[i])
        res[l1[i]] = a 
        i = i +1
    return res
print(create_encrypt_alphabet_dictionary(['a','b','c'],[['a','b','c'],['b','c','a'],['c','a','b']]))




def create_decrypt_alphabets_dictionary(l1, l2):
    if len(l1) != len(l2):
        return {}
    d = {}
    i = 0
    while i < len(l1):
        d[l1[i]] = create_dictionary(l2[i], l1)
        i = i + 1
        return d
