def sent(text):
    a=text.count(".")
    b=text.count(",")
    c=text.count("?")
    d=text.count("!")
    res=a+b+c+d
    return res
text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
print(sent(text))

def word(w):
    return len(w.split())

def rep(list):
    counter = 0
    num = list[0]
    for i in list:
        freq = list.count(i)
        if freq > counter :
            counter = freq
            num = i
    return num
list=[1,2,3,4,5,4]
print(rep(list))

from statistics import mode
def repeated(list):
    num= mode(list)
    list.remove(num)
    num1 = mode(list)
    return num,num1
list=[1,1,2,2,2,3,4,5]
print(repeated(list))

def rem(items):
    string = []
    for item in items:
        if type(item) == str:
            string.append(item)
    return string
items = [1,'sdfsdf','d',3]
print(rem(items))
