with open('sirdecaractere.txt', 'r') as f:
    a=f.readline()
    v=eval(f.readline())
with open ('cifre.txt', 'w' ) as f:
    b=tuple(filter(lambda x: x in ('1', '2' , '3', '4', '5', '6', '7', '8', '9', '0'), v))
    f.write(str(b))
with open ('literemajuscule.txt', 'w') as f:
    c=tuple(filter(str.isupper, a))
    f.write(str(c))
with open('literemici', 'w') as f:
    d=tuple(filter(str.islower, a))
    f.write(str(d))
with open ('simboluri.txt', 'w') as f:
    e=tuple(filter(lambda y : y in ('(', ')', '{', '}', '!', '@', '$', '^', '&'), v))
with open ('operatorimate.txt', 'w') as f:
    l=tuple(filter(lambda z : z in ('+', '-', '//', '/', '*', '%', '**'), v))
    f.write(str(l))