def decode(self, s):
    output = ""
    num=""
    for i in s:
        if i.isalpha():
            output+=i*int(num)
            num=""
        else:
            num+=i
    return output
def encode(m):
    enco = ""
    i = 0
    while i <= (len(m)-1):
        c = 1
        ch = m[i]
        j = i
        while j < len(m)-1:
            if m[j] == m[j+1]:
                c = c+1
                j = j+1
            else:
                break
    enco=enco+str(c)+ch
    i = j+1
    return enco
enco=encode("ABBBBCCCCCCCCAB")
print(enco)
deco=decode(enco)
print(deco)


