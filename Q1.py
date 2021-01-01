def reverse1(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1


def reverse2(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    s2=''
    length2 = len(s1)-1
    temp = len(s1)
    while length2 >=-1:
        if(s1[length2]==' 'or length2==-1):
            s2=s2+s1[length2+1:temp]
            s2=s2+' '
            temp = length2
        length2=length2-1
    return s2
